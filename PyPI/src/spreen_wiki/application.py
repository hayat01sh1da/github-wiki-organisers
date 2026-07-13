import glob
import os
import re
from typing import Any

from .configuration import Configuration


class Application:
    """Base class for the wiki-organising commands. Loads the wiki tree
    under base_path, groups it by Owner or Category in either English or
    Japanese, and exposes the resulting maps to its subclasses. Grouping
    criteria, languages and labels are resolved through Configuration and
    can be extended via a `.spreen.yml` file."""

    class NotImplementedError(Exception):
        pass

    _cached_wiki_maps: dict[str, list[str]]

    @classmethod
    def run(cls, base_path: str | None = None, group_by: str = 'Owner',
            language: str = 'English',
            home_overflow: str | bool = 'false',
            **options: Any) -> Any:
        instance = cls(
            base_path=base_path, group_by=group_by,
            language=language, home_overflow=home_overflow, **options,
        )
        instance.validate()
        return instance._run()

    def __init__(self, base_path: str | None = None,
                 group_by: str = 'Owner', language: str = 'English',
                 home_overflow: str | bool = 'false',
                 config: Configuration | None = None,
                 **options: Any) -> None:
        self._base_path = base_path if base_path is not None else os.getcwd()
        self._group_by = group_by
        self._language = language
        self._home_overflow = self._parse_home_overflow(home_overflow)
        self._config = config or Configuration(
            base_path=self._base_path, **options)
        self._path_to_home = os.path.join(self._base_path, 'Home.md')
        self._path_to_sidebar = os.path.join(self._base_path, '_Sidebar.md')
        self._paths_to_wikis = sorted(glob.glob(
            os.path.join(self._base_path, '**', '*.md'), recursive=True))
        self._excluded_paths = {
            path
            for excluded_dir in self._config.excluded_dirs
            for path in glob.glob(
                os.path.join(self._base_path, excluded_dir, '**', '*.md'),
                recursive=True)
        }

    def validate(self) -> None:
        if self._group_by not in self._config.group_bys():
            raise ValueError(f'Invalid group_by: `{self._group_by}`')
        if self._language not in self._config.languages(self._group_by):
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
        excluded.update(self._excluded_paths)
        return [p for p in self._paths_to_wikis if p not in excluded]

    def _target_regexp(self) -> re.Pattern[str]:
        return self._config.target_regexp(self._group_by)

    def _no_declaration(self) -> str:
        return self._config.no_declaration(self._group_by, self._language)

    def _wiki_maps_with_namespace(self) -> dict[str, list[str]]:
        if hasattr(self, '_cached_wiki_maps'):
            return self._cached_wiki_maps
        named: dict[str, list[str]] = {}
        undeclared: dict[str, list[str]] = {}
        for target_path in self._target_paths():
            self._populate_namespace(target_path, named, undeclared)
        result = dict(sorted(named.items()))
        result.update(undeclared)
        self._cached_wiki_maps = result
        return result

    def _populate_namespace(self, target_path: str,
                            named: dict[str, list[str]],
                            undeclared: dict[str, list[str]]) -> None:
        if not os.path.isfile(target_path):
            return
        with open(target_path, encoding='utf-8') as f:
            wiki = os.path.basename(target_path)
            namespace = self._namespace_for(f)
        target = undeclared if namespace == self._no_declaration() \
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
