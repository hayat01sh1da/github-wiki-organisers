import os
import sys

sys.path.append('./src')

from application import Application  # noqa: E402


class UnknownWikiListExporterForLLM(Application):
    """Writes a flat list of the wikis under the "unknown owner/category"
    namespace in a form suitable for feeding to an LLM."""

    TARGET_NAMESPACE = {
        ('Owner', 'English'): 'Unknown Owner nor Necessity',
        ('Owner', 'Japanese'): 'Ownerチーム・要or不要が不明なページ群',
        ('Category', 'English'): 'Uncategorised',
        ('Category', 'Japanese'): 'Category記載なし',
    }

    def __init__(self, base_path: str = '', group_by: str = '',
                 language: str = '',
                 home_overflow: str | bool = 'false') -> None:
        super().__init__(
            base_path=base_path, group_by=group_by,
            language=language, home_overflow=home_overflow,
        )
        self._path_to_export = os.path.join(
            base_path, 'unknown_wiki_list_for_llm.txt')

    # private

    def _run(self) -> str:
        wikis = self._unknown_wiki_list_for_llm()
        with open(self._path_to_export, 'wb') as f:
            f.write(('\n'.join(wikis) + '\n').encode())
        return self._path_to_export

    def _target_namespace(self) -> str:
        return self.TARGET_NAMESPACE.get(
            (self._group_by, self._language), '')

    def _unknown_wiki_list_for_llm(self) -> list[str]:
        if hasattr(self, '_cached_unknown'):
            return self._cached_unknown
        plain = self._plain_wiki_maps()
        target = self._target_namespace()
        self._cached_unknown = list(plain.get(target, []))
        return self._cached_unknown
