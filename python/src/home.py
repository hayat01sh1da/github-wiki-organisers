import os
import shutil
import sys

sys.path.append('./src')

from application import Application  # noqa: E402


HOME_URL = (
    f'https://github.com/'
    f'{os.environ.get("ORGANISATION_NAME", "hayat01sh1da")}'
    f'/github-wiki-organisers/wiki'
)


class Home(Application):
    """Generates the wiki Home page, optionally splitting per-owner content
    out into `wikis-by-owner/<owner>.md` when home_overflow is enabled."""

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
        self._path_to_wikis_by_owner_dir = os.path.join(
            base_path, 'wikis-by-owner')

    # private

    def _run(self) -> str:
        if self._home_overflow:
            self._write_concise_home_passage()
        else:
            self._write_home_passage()
        return HOME_URL

    def _path_to_home_template(self) -> str:
        return os.path.join(
            '..', 'home_template', self._group_by.lower(),
            f'{self._language.lower()}.md',
        )

    def _home_passage(self) -> list[str]:
        if not hasattr(self, '_cached_home_passage'):
            with open(self._path_to_home_template()) as f:
                self._cached_home_passage = f.readlines() + ['\n']
        return self._cached_home_passage

    def _write_home_passage(self) -> None:
        if os.path.exists(self._path_to_wikis_by_owner_dir):
            shutil.rmtree(self._path_to_wikis_by_owner_dir)
        passage = self._home_passage()
        for namespace, wikis in self._owned_wiki_maps().items():
            self._append_block(passage, namespace, wikis, owned=True)
        for namespace, wikis in self._plain_wiki_maps().items():
            self._append_block(passage, namespace, wikis, owned=False)
        with open(self._path_to_home, 'w') as f:
            f.write(''.join(passage).rstrip('\n') + '\n')

    def _write_concise_home_passage(self) -> None:
        os.makedirs(self._path_to_wikis_by_owner_dir, exist_ok=True)
        self._write_per_namespace_files()
        self._write_home_table_of_contents()

    def _write_per_namespace_files(self) -> None:
        for namespace, wikis in self._owned_wiki_maps().items():
            self._write_overflow_block(namespace, wikis, owned=True)
        for namespace, wikis in self._plain_wiki_maps().items():
            self._write_overflow_block(namespace, wikis, owned=False)

    def _write_home_table_of_contents(self) -> None:
        passage = self._home_passage()
        for namespace in (list(self._owned_wiki_maps().keys())
                          + list(self._plain_wiki_maps().keys())):
            passage.append(f'- [[{namespace}]]\n')
        passage.append('\n')
        with open(self._path_to_home, 'w') as f:
            f.write(''.join(passage).rstrip('\n') + '\n')

    def _append_block(self, passage: list[str], namespace: str,
                      wikis: list[str], owned: bool) -> None:
        passage.append(f'{self._heading_for(namespace, owned=owned)}\n')
        passage.append('\n')
        for wiki in wikis:
            passage.append(f'- [[{wiki.replace(".md", "")}]]\n')
        passage.append('\n')

    def _write_overflow_block(self, namespace: str, wikis: list[str],
                              owned: bool) -> None:
        scratch: list[str] = []
        self._append_block(scratch, namespace, wikis, owned=owned)
        filename = os.path.join(
            self._path_to_wikis_by_owner_dir, f'{namespace}.md')
        with open(filename, 'w') as f:
            f.write(''.join(scratch).rstrip('\n') + '\n')

    def _heading_for(self, namespace: str, owned: bool) -> str:
        if owned:
            url = self._base_owner_url + namespace.replace('@', '')
            return f'## [{namespace}]({url})'
        return f'## {namespace}'
