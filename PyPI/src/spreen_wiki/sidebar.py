from typing import Any

from .application import Application


class Sidebar(Application):
    """Generates the wiki _Sidebar.md as a nested list of owners/categories
    and their wiki pages."""

    def __init__(self, **options: Any) -> None:
        super().__init__(**options)
        self._wiki_list: list[str] = []

    # private

    def _run(self) -> None:
        self._update_wiki_list()
        with open(self._path_to_sidebar, 'w', encoding='utf-8') as f:
            f.write(''.join(self._wiki_list))

    def _update_wiki_list(self) -> None:
        for namespace, wikis in self._owned_wiki_maps().items():
            self._append_section(namespace, wikis, owned=True)
        for namespace, wikis in self._plain_wiki_maps().items():
            self._append_section(namespace, wikis, owned=False)

    def _append_section(self, namespace: str, wikis: list[str],
                        owned: bool) -> None:
        self._wiki_list.append(
            f'{self._section_heading(namespace, owned=owned)}\n')
        for wiki in wikis:
            self._wiki_list.append(f'  - [[{wiki.replace(".md", "")}]]\n')

    def _section_heading(self, namespace: str, owned: bool) -> str:
        owner_base_url = self._config.owner_base_url
        if owned and owner_base_url:
            url = owner_base_url + namespace.replace('@', '')
            return f'- [{namespace}]({url})'
        return f'- {namespace}'
