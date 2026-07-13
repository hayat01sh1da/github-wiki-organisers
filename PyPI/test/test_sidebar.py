import os
from collections.abc import Callable

from spreen_wiki.sidebar import Sidebar

_FIXTURES_DIR = os.path.join('.', 'test', 'fixtures', 'sidebar')


def _run_sidebar(wiki_workspace: Callable[..., str], group_by: str = 'Owner',
                 language: str = 'English') -> str:
    base_path = wiki_workspace(group_by=group_by, language=language)
    Sidebar.run(base_path=base_path, group_by=group_by, language=language,
                organisation='test-org')
    with open(os.path.join(base_path, '_Sidebar.md'), encoding='utf-8') as f:
        return f.read()


def _expected_sidebar(basename: str) -> str:
    """Expected Sidebar pages live under test/fixtures/sidebar/."""
    with open(os.path.join(_FIXTURES_DIR, basename), encoding='utf-8') as f:
        return f.read()


def test_english_owned_sidebar(wiki_workspace: Callable[..., str]) -> None:
    assert _run_sidebar(wiki_workspace) == _expected_sidebar(
        'english_owned.md')


def test_english_plain_sidebar(wiki_workspace: Callable[..., str]) -> None:
    assert _run_sidebar(wiki_workspace, group_by='Category') == \
        _expected_sidebar('english_categorised.md')


def test_japanese_owned_sidebar(wiki_workspace: Callable[..., str]) -> None:
    assert _run_sidebar(wiki_workspace, language='Japanese') == \
        _expected_sidebar('japanese_owned.md')


def test_japanese_plain_sidebar(wiki_workspace: Callable[..., str]) -> None:
    assert _run_sidebar(
        wiki_workspace,
        group_by='Category',
        language='Japanese') == _expected_sidebar('japanese_categorised.md')
