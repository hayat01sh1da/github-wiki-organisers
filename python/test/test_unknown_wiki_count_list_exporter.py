import os
from collections.abc import Callable

import pytest

from unknown_wiki_count_list_exporter import UnknownWikiCountListExporter


def _run(wiki_workspace: Callable[..., str], group_by: str = 'Owner',
         language: str = 'English',
         file_maps: dict[str, str] | None = None) -> str:
    base_path = wiki_workspace(
        group_by=group_by,
        language=language,
        file_maps=file_maps)
    UnknownWikiCountListExporter(
        base_path,
        group_by=group_by,
        language=language).run()
    with open(os.path.join(base_path, 'unknown_wiki_count_list_by_namespace.txt')) as f:
        return f.read()


@pytest.mark.parametrize(('file_maps',
                          'expected'),
                         [(None,
                           'Unknown Owner nor Necessity: 1\nUnowned but Necessary: 1\nUnowned: 2\n',
                           ),
                          ({'Unowned but Necessary Wiki.md': 'Owner: Unowned but Necessary',
                            'Unknown Owner nor Necessity Wiki.md': 'Owner: Unknown Owner nor Necessity',
                            'Unowned Wiki 1.md': '',
                            'Unowned Wiki 2.md': 'This is a sample Wiki',
                            },
                           'Unknown Owner nor Necessity: 1\nUnowned but Necessary: 1\nUnowned: 2\n',
                           ),
                          ({'Owned Wiki.md': 'Owner: @test-owner',
                            'Unowned but Necessary Wiki.md': 'Owner: Unowned but Necessary',
                            'Unowned Wiki 1.md': '',
                            'Unowned Wiki 2.md': 'This is a sample Wiki',
                            },
                             'Unknown Owner nor Necessity: 0\nUnowned but Necessary: 1\nUnowned: 2\n',
                           ),
                          ({'Owned Wiki.md': 'Owner: @test-owner',
                            'Unknown Owner nor Necessity Wiki.md': 'Owner: Unknown Owner nor Necessity',
                            'Unowned Wiki 1.md': '',
                            'Unowned Wiki 2.md': 'This is a sample Wiki',
                            },
                             'Unknown Owner nor Necessity: 1\nUnowned but Necessary: 0\nUnowned: 2\n',
                           ),
                          ({'Owned Wiki.md': 'Owner: @test-owner',
                            'Unowned but Necessary Wiki.md': 'Owner: Unowned but Necessary',
                            'Unknown Owner nor Necessity Wiki.md': 'Owner: Unknown Owner nor Necessity',
                            },
                             'Unknown Owner nor Necessity: 1\nUnowned but Necessary: 1\nUnowned: 0\n',
                           ),
                          ],
                         )
def test_english_owner(wiki_workspace: Callable[..., str],
                       file_maps: dict[str, str] | None,
                       expected: str) -> None:
    assert _run(wiki_workspace, file_maps=file_maps) == expected


@pytest.mark.parametrize(('file_maps',
                          'expected'),
                         [(None,
                           'Uncategorised: 2\n'),
                          ({'Owned Wiki.md': 'Owner: @test-owner',
                            'Unowned but Necessary Wiki.md': 'Owner: Unowned but Necessary',
                            'Unknown Owner nor Necessity Wiki.md': 'Owner: Unknown Owner nor Necessity',
                            'Unowned Wiki 1.md': '',
                            'Unowned Wiki 2.md': 'This is a sample Wiki',
                            },
                             'Uncategorised: 5\n',
                           ),
                          ],
                         )
def test_english_category(wiki_workspace: Callable[..., str],
                          file_maps: dict[str, str] | None,
                          expected: str) -> None:
    assert _run(
        wiki_workspace,
        group_by='Category',
        file_maps=file_maps) == expected


@pytest.mark.parametrize(('file_maps',
                          'expected'),
                         [(None,
                           'Ownerチームが不明だが必要なページ群: 1\nOwnerチーム・要or不要が不明なページ群: 1\nOwner記名なし: 2\n',
                           ),
                          ({'Ownerチームが不明だが必要なページ.md': 'Owner: Ownerチームが不明だが必要なページ群',
                            'Ownerチーム・要or不要が不明なページ.md': 'Owner: Ownerチーム・要or不要が不明なページ群',
                            'Owner記名なしページ1.md': '',
                            'Owner記名なしページ2.md': 'サンプル Wiki',
                            },
                           'Ownerチームが不明だが必要なページ群: 1\nOwnerチーム・要or不要が不明なページ群: 1\nOwner記名なし: 2\n',
                           ),
                          ({'Owner記名ありページ.md': 'Owner: @test-owner',
                            'Ownerチームが不明だが必要なページ.md': 'Owner: Ownerチームが不明だが必要なページ群',
                            'Owner記名なしページ1.md': '',
                            'Owner記名なしページ2.md': 'サンプル Wiki',
                            },
                             'Ownerチームが不明だが必要なページ群: 1\nOwnerチーム・要or不要が不明なページ群: 0\nOwner記名なし: 2\n',
                           ),
                          ({'Owner記名ありページ.md': 'Owner: @test-owner',
                            'Ownerチーム・要or不要が不明なページ.md': 'Owner: Ownerチーム・要or不要が不明なページ群',
                            'Owner記名なしページ1.md': '',
                            'Owner記名なしページ2.md': 'サンプル Wiki',
                            },
                             'Ownerチームが不明だが必要なページ群: 0\nOwnerチーム・要or不要が不明なページ群: 1\nOwner記名なし: 2\n',
                           ),
                          ({'Owner記名ありページ.md': 'Owner: @test-owner',
                            'Ownerチームが不明だが必要なページ.md': 'Owner: Ownerチームが不明だが必要なページ群',
                            'Ownerチーム・要or不要が不明なページ.md': 'Owner: Ownerチーム・要or不要が不明なページ群',
                            },
                             'Ownerチームが不明だが必要なページ群: 1\nOwnerチーム・要or不要が不明なページ群: 1\nOwner記名なし: 0\n',
                           ),
                          ],
                         )
def test_japanese_owner(wiki_workspace: Callable[..., str],
                        file_maps: dict[str, str] | None,
                        expected: str) -> None:
    assert _run(
        wiki_workspace,
        language='Japanese',
        file_maps=file_maps) == expected


@pytest.mark.parametrize(
    ('file_maps', 'expected'),
    [
        (None, 'Category記載なし: 2\n'),
        (
            {
                'Owner記名ありページ.md': 'Owner: @test-owner',
                'Ownerチームが不明だが必要なページ.md': 'Owner: Ownerチームが不明だが必要なページ群',
                'Ownerチーム・要or不要が不明なページ.md': 'Owner: Ownerチーム・要or不要が不明なページ群',
                'Owner記名なしページ1.md': '',
                'Owner記名なしページ2.md': 'サンプル Wiki',
            },
            'Category記載なし: 5\n',
        ),
    ],
)
def test_japanese_category(wiki_workspace: Callable[..., str],
                           file_maps: dict[str, str] | None,
                           expected: str) -> None:
    assert _run(
        wiki_workspace,
        group_by='Category',
        language='Japanese',
        file_maps=file_maps) == expected
