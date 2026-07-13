import os
from typing import Any

from .application import Application

DEFAULT_OUTPUT_FILENAME = 'unknown_wiki_count_list_by_namespace.txt'


class UnknownWikiCountListExporter(Application):
    """Writes a sorted text report of how many wikis exist under each of
    the configured "unknown owner/category" namespaces."""

    _cached_counts: list[str]

    def __init__(self, output: str | None = None, **options: Any) -> None:
        super().__init__(**options)
        self._path_to_export = os.path.join(
            self._base_path, output or DEFAULT_OUTPUT_FILENAME)

    # private

    def _run(self) -> tuple[list[str], str]:
        counts = self._count_list_by_namespace()
        with open(self._path_to_export, 'wb') as f:
            f.write(('\n'.join(counts) + '\n').encode())
        return counts, self._path_to_export

    def _namespace_list(self) -> list[str]:
        return self._config.unknown_namespaces(self._group_by,
                                               self._language)

    def _missing_count_list_by_namespace(self) -> list[str]:
        plain_keys = set(self._plain_wiki_maps().keys())
        return [
            f'{namespace}: 0'
            for namespace in self._namespace_list()
            if namespace not in plain_keys
        ]

    def _count_list_by_namespace(self) -> list[str]:
        if hasattr(self, '_cached_counts'):
            return self._cached_counts
        plain = self._plain_wiki_maps()
        counts = [
            f'{namespace}: {len(plain[namespace])}'
            for namespace in self._namespace_list()
            if namespace in plain
        ]
        self._cached_counts = sorted(
            counts + self._missing_count_list_by_namespace())
        return self._cached_counts
