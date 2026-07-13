import os
import re
from importlib.resources import files
from typing import Any

import yaml

CONFIG_FILENAME = '.spreen.yml'
DEFAULT_EXCLUDED_DIRS = ['github-wiki-organisers', 'wikis-by-owner']

# Built-in labels: how the first line of a wiki page is parsed (regexp),
# which namespace collects pages without a declaration (no_declaration),
# which namespaces the count report covers (unknown_namespaces) and which
# namespace the LLM export targets (llm_target_namespace). A config file
# can override any of these, add languages or add group_by criteria.
DEFAULT_LABELS: dict[str, Any] = {
    'Owner': {
        'regexp': r'[Oo]wner:\s?',
        'languages': {
            'English': {
                'no_declaration': 'Unowned',
                'unknown_namespaces': [
                    'Unknown Owner nor Necessity',
                    'Unowned but Necessary',
                    'Unowned',
                ],
                'llm_target_namespace': 'Unknown Owner nor Necessity',
            },
            'Japanese': {
                'no_declaration': 'Owner記名なし',
                'unknown_namespaces': [
                    'Ownerチームが不明だが必要なページ群',
                    'Ownerチーム・要or不要が不明なページ群',
                    'Owner記名なし',
                ],
                'llm_target_namespace': 'Ownerチーム・要or不要が不明なページ群',
            },
        },
    },
    'Category': {
        'regexp': r'[Cc]ategory:\s?',
        'languages': {
            'English': {
                'no_declaration': 'Uncategorised',
                'unknown_namespaces': ['Uncategorised'],
                'llm_target_namespace': 'Uncategorised',
            },
            'Japanese': {
                'no_declaration': 'Category記載なし',
                'unknown_namespaces': ['Category記載なし'],
                'llm_target_namespace': 'Category記載なし',
            },
        },
    },
}


def default_template_dir() -> str:
    """The `templates/` directory shipped with this package."""
    return str(files(__package__).joinpath('templates'))


def _presence(value: str | None) -> str | None:
    """Treats empty strings the same as None so that callers can pass
    values straight from optional environment variables or CLI flags."""
    return value if value else None


def _deep_merge(base: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    merged = dict(base)
    for key, new_value in override.items():
        old_value = merged.get(key)
        if isinstance(old_value, dict) and isinstance(new_value, dict):
            merged[key] = _deep_merge(old_value, new_value)
        else:
            merged[key] = new_value
    return merged


class Configuration:
    """Resolves the runtime configuration for a wiki checkout. Every value
    is looked up with the same precedence: explicit keyword argument, then
    the `.spreen.yml` file under base_path (or config_path), then
    the ORGANISATION_NAME environment variable (organisation only), then
    the built-in defaults."""

    def __init__(self, base_path: str, config_path: str | None = None,
                 organisation: str | None = None,
                 repository: str | None = None,
                 wiki_url: str | None = None,
                 owner_base_url: str | None = None,
                 excluded_dirs: list[str] | None = None,
                 template_dir: str | None = None) -> None:
        self._file = self._load_file(
            config_path or os.path.join(base_path, CONFIG_FILENAME))
        self.organisation = self._resolve_organisation(organisation)
        self.repository = self._resolve(repository, 'repository')
        self.wiki_url = (self._resolve(wiki_url, 'wiki_url')
                         or self._default_wiki_url())
        self.owner_base_url = (self._resolve(owner_base_url, 'owner_base_url')
                               or self._default_owner_base_url())
        self.excluded_dirs: list[str] = (
            excluded_dirs if excluded_dirs is not None
            else self._file.get('exclude', DEFAULT_EXCLUDED_DIRS))
        self.template_dir: str = (
            template_dir or self._file.get(
                'template_dir', default_template_dir()))
        self._labels = _deep_merge(
            DEFAULT_LABELS, self._file.get('labels', {}))

    def group_bys(self) -> list[str]:
        return list(self._labels.keys())

    def languages(self, group_by: str) -> list[str]:
        return list(self._label_for(group_by).get('languages', {}).keys())

    def target_regexp(self, group_by: str) -> re.Pattern[str]:
        return re.compile(self._label_for(group_by).get('regexp', ''))

    def no_declaration(self, group_by: str, language: str) -> str:
        value: str = self._language_labels(group_by, language).get(
            'no_declaration', '')
        return value

    def unknown_namespaces(self, group_by: str,
                           language: str) -> list[str]:
        value: list[str] = self._language_labels(group_by, language).get(
            'unknown_namespaces', [])
        return value

    def llm_target_namespace(self, group_by: str, language: str) -> str:
        value: str = self._language_labels(group_by, language).get(
            'llm_target_namespace', '')
        return value

    def path_to_template(self, group_by: str, language: str) -> str:
        return os.path.join(self.template_dir, group_by.lower(),
                            f'{language.lower()}.md')

    # private

    @staticmethod
    def _load_file(path: str) -> dict[str, Any]:
        if not os.path.isfile(path):
            return {}
        with open(path, encoding='utf-8') as f:
            return yaml.safe_load(f) or {}

    def _resolve(self, explicit: str | None, key: str) -> str | None:
        return _presence(explicit) or _presence(self._file.get(key))

    def _resolve_organisation(self, explicit: str | None) -> str | None:
        return (self._resolve(explicit, 'organisation')
                or _presence(os.environ.get('ORGANISATION_NAME')))

    def _default_wiki_url(self) -> str | None:
        if self.organisation and self.repository:
            return (f'https://github.com/{self.organisation}'
                    f'/{self.repository}/wiki')
        return None

    def _default_owner_base_url(self) -> str | None:
        if self.organisation:
            return f'https://github.com/orgs/{self.organisation}/teams/'
        return None

    def _label_for(self, group_by: str) -> dict[str, Any]:
        label: dict[str, Any] = self._labels.get(group_by, {})
        return label

    def _language_labels(self, group_by: str,
                         language: str) -> dict[str, Any]:
        labels: dict[str, Any] = self._label_for(group_by).get(
            'languages', {}).get(language, {})
        return labels
