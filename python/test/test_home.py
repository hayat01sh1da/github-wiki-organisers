import glob
import os

from home import Home


def _run_home(wiki_workspace, group_by='Owner', language='English', home_overflow=False):
    base_path = wiki_workspace(group_by=group_by, language=language)
    Home(base_path=base_path, group_by=group_by, language=language, home_overflow=home_overflow).run()
    with open(os.path.join(base_path, 'Home.md')) as f:
        home = f.read()
    path_to_wikis_by_owner = os.path.join(base_path, 'wikis-by-owner')
    overflow_files = sorted(glob.glob(os.path.join(path_to_wikis_by_owner, '*.md')))
    return home, path_to_wikis_by_owner, overflow_files


def _expected_wikis_by_owner(path_to_wikis_by_owner, namespaces):
    return sorted(os.path.join(path_to_wikis_by_owner, f'{namespace}.md') for namespace in namespaces)


_ENGLISH_OWNED_HOME = (
    '## How to Manage Wiki Pages\n'
    '\n'
    'This Home page manage wikis by owner group.\n'
    '\n'
    'Absence of ownership declaration worsens maintainability and searchability because it makes ambiguous which team the responsibility belongs to.  \n'
    'Kindly make sure to articulate `Owner: @OWNER_TEAM` of the top of each of your wiki page to avoid it.\n'
    '\n'
    'Also, please keep in mind that you do not have to edit Home and Sidebar by yourself, which are automatically updated by a GitHub Actions cron job.\n'
    '\n'
)
_ENGLISH_OWNED_HOME_WITHOUT_OVERFLOW = _ENGLISH_OWNED_HOME + (
    '## [@test-owner](https://github.com/orgs/hayat01sh1da/teams/test-owner)\n'
    '\n'
    '- [[Owned Wiki]]\n'
    '\n'
    '## Unknown Owner nor Necessity\n'
    '\n'
    '- [[Unknown Owner nor Necessity Wiki]]\n'
    '\n'
    '## Unowned but Necessary\n'
    '\n'
    '- [[Unowned but Necessary Wiki]]\n'
    '\n'
    '## Unowned\n'
    '\n'
    '- [[Unowned Wiki 1]]\n'
    '- [[Unowned Wiki 2]]\n'
)
_ENGLISH_OWNED_HOME_WITH_OVERFLOW = _ENGLISH_OWNED_HOME + (
    '- [[@test-owner]]\n'
    '- [[Unknown Owner nor Necessity]]\n'
    '- [[Unowned but Necessary]]\n'
    '- [[Unowned]]\n'
)
_ENGLISH_CATEGORISED_HOME = (
    '## How to Manage Wiki Pages\n'
    '\n'
    'This Home page manage wikis by category group.\n'
    '\n'
    'Absence of category declaration worsens maintainability and searchability.  \n'
    'Kindly make sure to articulate `Category: CATEGORY_NAME` of the top of each of your wiki page to avoid it.\n'
    '\n'
    'Also, please keep in mind that you do not have to edit Home and Sidebar by yourself, which are automatically updated by a GitHub Actions cron job.\n'
    '\n'
    '## test-category\n'
    '\n'
    '- [[Categorised Wiki]]\n'
    '\n'
    '## Uncategorised\n'
    '\n'
    '- [[Uncategorised Wiki 1]]\n'
    '- [[Uncategorised Wiki 2]]\n'
)
_JAPANESE_OWNED_HOME = (
    '## Wiki ページの運用ルール\n'
    '\n'
    'このページは Owner チームごとに Wiki をグルーピングして一覧化しています。\n'
    '\n'
    'Ownership をどのチームが持つのかが不明だと、責任の所在が不明瞭になり、保守性の悪化に伴うノイズの増加と検索性の悪化が発生します。  \n'
    '治安維持のため、各ページの冒頭に `Owner: @オーナーチーム` を明記して頂きますようよろしくお願いします。\n'
    '\n'
    'なお、Home・Sidebar は専用の定期実行ジョブで自動更新しますので編集は不要です。\n'
    '\n'
)
_JAPANESE_OWNED_HOME_WITHOUT_OVERFLOW = _JAPANESE_OWNED_HOME + (
    '## [@test-owner](https://github.com/orgs/hayat01sh1da/teams/test-owner)\n'
    '\n'
    '- [[Owner記名ありページ]]\n'
    '\n'
    '## Ownerチームが不明だが必要なページ群\n'
    '\n'
    '- [[Ownerチームが不明だが必要なページ]]\n'
    '\n'
    '## Ownerチーム・要or不要が不明なページ群\n'
    '\n'
    '- [[Ownerチーム・要or不要が不明なページ]]\n'
    '\n'
    '## Owner記名なし\n'
    '\n'
    '- [[Owner記名なしページ1]]\n'
    '- [[Owner記名なしページ2]]\n'
)
_JAPANESE_OWNED_HOME_WITH_OVERFLOW = _JAPANESE_OWNED_HOME + (
    '- [[@test-owner]]\n'
    '- [[Ownerチームが不明だが必要なページ群]]\n'
    '- [[Ownerチーム・要or不要が不明なページ群]]\n'
    '- [[Owner記名なし]]\n'
)
_JAPANESE_CATEGORISED_HOME = (
    '## Wiki ページの運用ルール\n'
    '\n'
    'このページは Category ごとに Wiki をグルーピングして一覧化しています。\n'
    '\n'
    'Category が不明だと、保守性と検索性の悪化が発生します。  \n'
    '治安維持のため、各ページの冒頭に `Category: カテゴリー名` を明記して頂きますようよろしくお願いします。\n'
    '\n'
    'なお、Home・Sidebar は専用の定期実行ジョブで自動更新しますので編集は不要です。\n'
    '\n'
    '## test-category\n'
    '\n'
    '- [[Category記載ありページ]]\n'
    '\n'
    '## Category記載なし\n'
    '\n'
    '- [[Category記載なしページ1]]\n'
    '- [[Category記載なしページ2]]\n'
)


def test_english_owned_home_without_overflow(wiki_workspace):
    home, path_to_wikis_by_owner, _ = _run_home(wiki_workspace)
    assert not os.path.exists(path_to_wikis_by_owner)
    assert home == _ENGLISH_OWNED_HOME_WITHOUT_OVERFLOW


def test_english_owned_home_with_overflow(wiki_workspace):
    home, path_to_wikis_by_owner, overflow_files = _run_home(wiki_workspace, home_overflow=True)
    assert os.path.exists(path_to_wikis_by_owner)
    assert home == _ENGLISH_OWNED_HOME_WITH_OVERFLOW
    assert overflow_files == _expected_wikis_by_owner(
        path_to_wikis_by_owner,
        ['@test-owner', 'Unknown Owner nor Necessity', 'Unowned but Necessary', 'Unowned'],
    )


def test_english_categorised_home(wiki_workspace):
    home, _, _ = _run_home(wiki_workspace, group_by='Category')
    assert home == _ENGLISH_CATEGORISED_HOME


def test_japanese_owned_home_without_overflow(wiki_workspace):
    home, path_to_wikis_by_owner, _ = _run_home(wiki_workspace, language='Japanese')
    assert not os.path.exists(path_to_wikis_by_owner)
    assert home == _JAPANESE_OWNED_HOME_WITHOUT_OVERFLOW


def test_japanese_owned_home_with_overflow(wiki_workspace):
    home, path_to_wikis_by_owner, overflow_files = _run_home(
        wiki_workspace, language='Japanese', home_overflow=True,
    )
    assert os.path.exists(path_to_wikis_by_owner)
    assert home == _JAPANESE_OWNED_HOME_WITH_OVERFLOW
    assert overflow_files == _expected_wikis_by_owner(
        path_to_wikis_by_owner,
        ['@test-owner', 'Ownerチームが不明だが必要なページ群', 'Ownerチーム・要or不要が不明なページ群', 'Owner記名なし'],
    )


def test_japanese_categorised_home(wiki_workspace):
    home, _, _ = _run_home(wiki_workspace, group_by='Category', language='Japanese')
    assert home == _JAPANESE_CATEGORISED_HOME
