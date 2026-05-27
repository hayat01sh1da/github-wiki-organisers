import glob
import os
import re
from typing import Any


class Application:
    """Base class for the wiki-organising commands. Loads the wiki tree
    under base_path, groups it by Owner or Category in either English or
    Japanese, and exposes the resulting maps to its subclasses."""

    class NotImplementedError(Exception):
        pass

    NO_DECLARATION = {
        ('Owner', 'English'): 'Unowned',
        ('Owner', 'Japanese'): 'Owner記名なし',
        ('Category', 'English'): 'Uncategorised',
        ('Category', 'Japanese'): 'Category記載なし',
    }

    TARGET_REGEXP = {
        'Owner': re.compile(r'[Oo]wner:\s?'),
        'Category': re.compile(r'[Cc]ategory:\s?'),
    }

    _cached_wiki_maps: dict[str, list[str]]

    @classmethod
    def run(cls, base_path: str = os.path.join('..', '..'),
            group_by: str = 'Owner', language: str = 'English',
            home_overflow: str | bool = 'false') -> Any:
        instance = cls(
            base_path=base_path, group_by=group_by,
            language=language, home_overflow=home_overflow,
        )
        instance.validate()
        return instance._run()

    def __init__(self, base_path: str, group_by: str, language: str,
                 home_overflow: str | bool) -> None:
        self._base_path = base_path
        self._group_by = group_by
        self._language = language
        self._home_overflow = self._parse_home_overflow(home_overflow)
        self._path_to_home = os.path.join(base_path, 'Home.md')
        self._path_to_sidebar = os.path.join(base_path, '_Sidebar.md')
        self._path_to_github_wiki_organisers = sorted(glob.glob(
            os.path.join(base_path, 'github-wiki-organisers', '**', '*.md'),
            recursive=True))
        self._path_to_wikis_by_owner = sorted(glob.glob(
            os.path.join(base_path, 'wikis-by-owner', '*.md')))
        self._paths_to_wikis = sorted(glob.glob(
            os.path.join(base_path, '**', '*.md'), recursive=True))

    def validate(self) -> None:
        if self._group_by not in ('Owner', 'Category'):
            raise ValueError(f'Invalid group_by: `{self._group_by}`')
        if self._language not in ('English', 'Japanese'):
            raise ValueError(f'Invalid language: `{self._language}`')
        if self._home_overflow not in (True, False):
            raise ValueError(
                f'Invalid home_overflow: `{self._home_overflow}` '
                'must be boolean')

    # private

    def _run(self) -> Any:
        raise self.NotImplementedError(
            'This method must be implemented in each subclass.')

    @staticmethod
    def _parse_home_overflow(raw: str | bool) -> str | bool:
        match raw:
            case 'true':
                return True
            case 'false':
                return False
            case _:
                return raw

    def _target_paths(self) -> list[str]:
        excluded = {self._path_to_home, self._path_to_sidebar}
        excluded.update(self._path_to_github_wiki_organisers)
        excluded.update(self._path_to_wikis_by_owner)
        return [p for p in self._paths_to_wikis if p not in excluded]

    def _target_regexp(self) -> re.Pattern[str]:
        return self.TARGET_REGEXP.get(self._group_by, re.compile(''))

    def _no_declaration(self) -> str:
        return self.NO_DECLARATION.get(
            (self._group_by, self._language), '')

    def _wiki_maps_with_namespace(self) -> dict[str, list[str]]:
        if hasattr(self, '_cached_wiki_maps'):
            return self._cached_wiki_maps
        named: dict[str, list[str]] = {}
        uncategorised: dict[str, list[str]] = {}
        for target_path in self._target_paths():
            self._populate_namespace(target_path, named, uncategorised)
        result = dict(sorted(named.items()))
        result.update(uncategorised)
        self._cached_wiki_maps = result
        return result

    def _populate_namespace(self, target_path: str,
                            named: dict[str, list[str]],
                            uncategorised: dict[str, list[str]]) -> None:
        if not os.path.isfile(target_path):
            return
        with open(target_path) as f:
            wiki = os.path.basename(target_path)
            namespace = self._namespace_for(f)
        target = uncategorised if namespace == self._no_declaration() \
            else named
        target.setdefault(namespace, []).append(wiki)

    def _namespace_for(self, file: Any) -> str:
        declaration = file.readline()
        if not declaration or not self._target_regexp().match(declaration):
            return self._no_declaration()
        return re.sub(self._target_regexp(), '', declaration.rstrip('\n'))

    def _owned_wiki_maps(self) -> dict[str, list[str]]:
        return {
            namespace: wikis
            for namespace, wikis in self._wiki_maps_with_namespace().items()
            if '@' in namespace
        }

    def _plain_wiki_maps(self) -> dict[str, list[str]]:
        return {
            namespace: wikis
            for namespace, wikis in self._wiki_maps_with_namespace().items()
            if '@' not in namespace
        }
