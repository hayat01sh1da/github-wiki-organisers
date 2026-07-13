import os
import shutil

from .application import Application


class Home(Application):
    """Generates the wiki Home page, optionally splitting per-owner content
    out into `wikis-by-owner/<owner>.md` when home_overflow is enabled.
    Returns the configured wiki URL (if any) so callers can point at the
    result."""

    _cached_home_passage: list[str]

    # private

    def _run(self) -> str | None:
        if self._home_overflow:
            self._write_concise_home_passage()
        else:
            self._write_home_passage()
        return self._config.wiki_url

    def _path_to_wikis_by_owner_dir(self) -> str:
        return os.path.join(self._base_path, 'wikis-by-owner')

    def _path_to_home_template(self) -> str:
        path = self._config.path_to_template(self._group_by, self._language)
        if not os.path.isfile(path):
            raise ValueError(
                f'Missing Home template: `{path}`. '
                'Ship one there or configure template_dir.')
        return path

    def _home_passage(self) -> list[str]:
        if not hasattr(self, '_cached_home_passage'):
            with open(self._path_to_home_template(), encoding='utf-8') as f:
                self._cached_home_passage = f.readlines() + ['\n']
        return self._cached_home_passage

    def _write_home_passage(self) -> None:
        if os.path.exists(self._path_to_wikis_by_owner_dir()):
            shutil.rmtree(self._path_to_wikis_by_owner_dir())
        passage = self._home_passage()
        for namespace, wikis in self._owned_wiki_maps().items():
            self._append_block(passage, namespace, wikis, owned=True)
        for namespace, wikis in self._plain_wiki_maps().items():
            self._append_block(passage, namespace, wikis, owned=False)
        with open(self._path_to_home, 'w', encoding='utf-8') as f:
            f.write(''.join(passage).rstrip('\n') + '\n')

    def _write_concise_home_passage(self) -> None:
        os.makedirs(self._path_to_wikis_by_owner_dir(), exist_ok=True)
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
        with open(self._path_to_home, 'w', encoding='utf-8') as f:
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
            self._path_to_wikis_by_owner_dir(), f'{namespace}.md')
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(''.join(scratch).rstrip('\n') + '\n')

    def _heading_for(self, namespace: str, owned: bool) -> str:
        owner_base_url = self._config.owner_base_url
        if owned and owner_base_url:
            url = owner_base_url + namespace.replace('@', '')
            return f'## [{namespace}]({url})'
        return f'## {namespace}'
