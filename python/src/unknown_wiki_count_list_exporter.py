import os
import sys

sys.path.append('./src')

from application import Application  # noqa: E402


class UnknownWikiCountListExporter(Application):
    """Writes a sorted text report of how many wikis exist under each of
    the well-known "unknown owner/category" namespaces."""

    NAMESPACE_LIST = {
        ('Owner', 'English'): [
            'Unknown Owner nor Necessity',
            'Unowned but Necessary',
            'Unowned',
        ],
        ('Owner', 'Japanese'): [
            'Ownerチームが不明だが必要なページ群',
            'Ownerチーム・要or不要が不明なページ群',
            'Owner記名なし',
        ],
        ('Category', 'English'): ['Uncategorised'],
        ('Category', 'Japanese'): ['Category記載なし'],
    }

    _cached_counts: list[str]

    def __init__(self, base_path: str = '', group_by: str = '',
                 language: str = '',
                 home_overflow: str | bool = 'false') -> None:
        super().__init__(
            base_path=base_path, group_by=group_by,
            language=language, home_overflow=home_overflow,
        )
        self._path_to_export = os.path.join(
            base_path, 'unknown_wiki_count_list_by_namespace.txt')

    # private

    def _run(self) -> tuple[list[str], str]:
        counts = self._count_list_by_namespace()
        with open(self._path_to_export, 'wb') as f:
            f.write(('\n'.join(counts) + '\n').encode())
        return counts, self._path_to_export

    def _namespace_list(self) -> list[str]:
        return self.NAMESPACE_LIST.get((self._group_by, self._language), [''])

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
