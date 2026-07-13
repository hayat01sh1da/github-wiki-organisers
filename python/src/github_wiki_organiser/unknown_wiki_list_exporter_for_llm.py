import os
from typing import Any

from .application import Application

DEFAULT_OUTPUT_FILENAME = 'unknown_wiki_list_for_llm.txt'


class UnknownWikiListExporterForLLM(Application):
    """Writes a flat list of the wikis under the configured "unknown
    owner/category" namespace in a form suitable for feeding to an LLM."""

    _cached_unknown: list[str]

    def __init__(self, output: str | None = None, **options: Any) -> None:
        super().__init__(**options)
        self._path_to_export = os.path.join(
            self._base_path, output or DEFAULT_OUTPUT_FILENAME)

    # private

    def _run(self) -> str:
        wikis = self._unknown_wiki_list_for_llm()
        with open(self._path_to_export, 'wb') as f:
            f.write(('\n'.join(wikis) + '\n').encode())
        return self._path_to_export

    def _target_namespace(self) -> str:
        return self._config.llm_target_namespace(self._group_by,
                                                 self._language)

    def _unknown_wiki_list_for_llm(self) -> list[str]:
        if hasattr(self, '_cached_unknown'):
            return self._cached_unknown
        plain = self._plain_wiki_maps()
        target = self._target_namespace()
        self._cached_unknown = list(plain.get(target, []))
        return self._cached_unknown
