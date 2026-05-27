import os
import sys

sys.path.append('./src')

from application import Application  # noqa: E402


class Sidebar(Application):
    """Generates the wiki _Sidebar.md as a nested list of owners/categories
    and their wiki pages."""

    def __init__(self, base_path: str = '', group_by: str = '',
                 language: str = '',
                 home_overflow: str | bool = 'false') -> None:
        super().__init__(
            base_path=base_path, group_by=group_by,
            language=language, home_overflow=home_overflow,
        )
        self._base_owner_url = (
            f'https://github.com/orgs/'
            f'{os.environ.get("ORGANISATION_NAME", "hayat01sh1da")}/teams/'
        )
        self._wiki_list: list[str] = []

    # private

    def _run(self) -> None:
        self._update_wiki_list()
        with open(self._path_to_sidebar, 'w') as f:
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
        if owned:
            url = self._base_owner_url + namespace.replace('@', '')
            return f'- [{namespace}]({url})'
        return f'- {namespace}'
