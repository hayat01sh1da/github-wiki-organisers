import glob
import os
from collections.abc import Callable

from home import Home

_FIXTURES_DIR = os.path.join('.', 'test', 'fixtures', 'home')


def _run_home(wiki_workspace: Callable[..., str], group_by: str = 'Owner',
              language: str = 'English',
              home_overflow: bool = False) -> tuple[str, str, list[str]]:
    base_path = wiki_workspace(group_by=group_by, language=language)
    Home.run(
        base_path=base_path,
        group_by=group_by,
        language=language,
        home_overflow=home_overflow,
    )
    with open(os.path.join(base_path, 'Home.md'), encoding='utf-8') as f:
        home = f.read()
    path_to_wikis_by_owner = os.path.join(base_path, 'wikis-by-owner')
    overflow_files = sorted(
        glob.glob(
            os.path.join(
                path_to_wikis_by_owner,
                '*.md')))
    return home, path_to_wikis_by_owner, overflow_files


def _expected_wikis_by_owner(path_to_wikis_by_owner: str,
                             namespaces: list[str]) -> list[str]:
    return sorted(
        os.path.join(
            path_to_wikis_by_owner,
            f'{namespace}.md') for namespace in namespaces)


def _expected_home(basename: str) -> str:
    """Expected Home pages live under test/fixtures/home/."""
    with open(os.path.join(_FIXTURES_DIR, basename), encoding='utf-8') as f:
        return f.read()


def test_english_owned_home_without_overflow(
        wiki_workspace: Callable[..., str]) -> None:
    home, path_to_wikis_by_owner, _ = _run_home(wiki_workspace)
    assert not os.path.exists(path_to_wikis_by_owner)
    assert home == _expected_home('english_owned_non_overflow.md')


def test_english_owned_home_with_overflow(
        wiki_workspace: Callable[..., str]) -> None:
    home, path_to_wikis_by_owner, overflow_files = _run_home(
        wiki_workspace, home_overflow=True)
    assert os.path.exists(path_to_wikis_by_owner)
    assert home == _expected_home('english_owned_overflow.md')
    assert overflow_files == _expected_wikis_by_owner(
        path_to_wikis_by_owner,
        ['@test-owner', 'Unknown Owner nor Necessity', 'Unowned but Necessary', 'Unowned'],
    )


def test_english_categorised_home(
        wiki_workspace: Callable[..., str]) -> None:
    home, _, _ = _run_home(wiki_workspace, group_by='Category')
    assert home == _expected_home('english_categorised.md')


def test_japanese_owned_home_without_overflow(
        wiki_workspace: Callable[..., str]) -> None:
    home, path_to_wikis_by_owner, _ = _run_home(
        wiki_workspace, language='Japanese')
    assert not os.path.exists(path_to_wikis_by_owner)
    assert home == _expected_home('japanese_owned_non_overflow.md')


def test_japanese_owned_home_with_overflow(
        wiki_workspace: Callable[..., str]) -> None:
    home, path_to_wikis_by_owner, overflow_files = _run_home(
        wiki_workspace, language='Japanese', home_overflow=True,
    )
    assert os.path.exists(path_to_wikis_by_owner)
    assert home == _expected_home('japanese_owned_overflow.md')
    assert overflow_files == _expected_wikis_by_owner(
        path_to_wikis_by_owner,
        ['@test-owner', 'Ownerチームが不明だが必要なページ群', 'Ownerチーム・要or不要が不明なページ群', 'Owner記名なし'],
    )


def test_japanese_categorised_home(
        wiki_workspace: Callable[..., str]) -> None:
    home, _, _ = _run_home(
        wiki_workspace, group_by='Category', language='Japanese')
    assert home == _expected_home('japanese_categorised.md')
