import os
from collections.abc import Callable

from unknown_wiki_list_exporter_for_llm import UnknownWikiListExporterForLLM


def _run(wiki_workspace: Callable[..., str], group_by: str = 'Owner',
         language: str = 'English') -> str:
    base_path = wiki_workspace(group_by=group_by, language=language)
    UnknownWikiListExporterForLLM(
        base_path=base_path,
        group_by=group_by,
        language=language).run()
    with open(os.path.join(base_path, 'unknown_wiki_list_for_llm.txt')) as f:
        return f.read()


def test_english_ownership(wiki_workspace: Callable[..., str]) -> None:
    assert _run(wiki_workspace) == 'Unknown Owner nor Necessity Wiki.md\n'


def test_english_category(wiki_workspace: Callable[..., str]) -> None:
    assert _run(wiki_workspace, group_by='Category') == \
        'Uncategorised Wiki 1.md\nUncategorised Wiki 2.md\n'


def test_japanese_ownership(wiki_workspace: Callable[..., str]) -> None:
    assert _run(
        wiki_workspace,
        language='Japanese') == 'Ownerチーム・要or不要が不明なページ.md\n'


def test_japanese_category(wiki_workspace: Callable[..., str]) -> None:
    assert _run(wiki_workspace, group_by='Category', language='Japanese') == \
        'Category記載なしページ1.md\nCategory記載なしページ2.md\n'
