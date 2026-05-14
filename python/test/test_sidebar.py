import os

from sidebar import Sidebar


def _run_sidebar(wiki_workspace, group_by='Owner', language='English'):
    base_path = wiki_workspace(group_by=group_by, language=language)
    Sidebar(base_path, group_by=group_by, language=language).run()
    with open(os.path.join(base_path, '_Sidebar.md')) as f:
        return f.read()


_ENGLISH_OWNED = (
    '- [@test-owner](https://github.com/orgs/hayat01sh1da/teams/test-owner)\n'
    '  - [[Owned Wiki]]\n'
    '- Unknown Owner nor Necessity\n'
    '  - [[Unknown Owner nor Necessity Wiki]]\n'
    '- Unowned but Necessary\n'
    '  - [[Unowned but Necessary Wiki]]\n'
    '- Unowned\n'
    '  - [[Unowned Wiki 1]]\n'
    '  - [[Unowned Wiki 2]]\n'
)
_ENGLISH_PLAIN = (
    '- test-category\n'
    '  - [[Categorised Wiki]]\n'
    '- Uncategorised\n'
    '  - [[Uncategorised Wiki 1]]\n'
    '  - [[Uncategorised Wiki 2]]\n'
)
_JAPANESE_OWNED = (
    '- [@test-owner](https://github.com/orgs/hayat01sh1da/teams/test-owner)\n'
    '  - [[Owner記名ありページ]]\n'
    '- Ownerチームが不明だが必要なページ群\n'
    '  - [[Ownerチームが不明だが必要なページ]]\n'
    '- Ownerチーム・要or不要が不明なページ群\n'
    '  - [[Ownerチーム・要or不要が不明なページ]]\n'
    '- Owner記名なし\n'
    '  - [[Owner記名なしページ1]]\n'
    '  - [[Owner記名なしページ2]]\n'
)
_JAPANESE_PLAIN = (
    '- test-category\n'
    '  - [[Category記載ありページ]]\n'
    '- Category記載なし\n'
    '  - [[Category記載なしページ1]]\n'
    '  - [[Category記載なしページ2]]\n'
)


def test_english_owned_sidebar(wiki_workspace):
    assert _run_sidebar(wiki_workspace) == _ENGLISH_OWNED


def test_english_plain_sidebar(wiki_workspace):
    assert _run_sidebar(wiki_workspace, group_by='Category') == _ENGLISH_PLAIN


def test_japanese_owned_sidebar(wiki_workspace):
    assert _run_sidebar(wiki_workspace, language='Japanese') == _JAPANESE_OWNED


def test_japanese_plain_sidebar(wiki_workspace):
    assert _run_sidebar(wiki_workspace, group_by='Category', language='Japanese') == _JAPANESE_PLAIN
