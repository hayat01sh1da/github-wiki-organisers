import glob
import os
import shutil
import sys

sys.path.append('./src')


import pytest


_DEFAULT_FILE_MAPS = {
    ('Owner', 'English'): {
        'Owned Wiki.md': 'Owner: @test-owner',
        'Unowned but Necessary Wiki.md': 'Owner: Unowned but Necessary',
        'Unknown Owner nor Necessity Wiki.md': 'Owner: Unknown Owner nor Necessity',
        'Unowned Wiki 1.md': '',
        'Unowned Wiki 2.md': 'This is a sample Wiki',
    },
    ('Owner', 'Japanese'): {
        'Owner記名ありページ.md': 'Owner: @test-owner',
        'Ownerチームが不明だが必要なページ.md': 'Owner: Ownerチームが不明だが必要なページ群',
        'Ownerチーム・要or不要が不明なページ.md': 'Owner: Ownerチーム・要or不要が不明なページ群',
        'Owner記名なしページ1.md': '',
        'Owner記名なしページ2.md': 'サンプル Wiki',
    },
    ('Category', 'English'): {
        'Categorised Wiki.md': 'Category: test-category',
        'Uncategorised Wiki 1.md': '',
        'Uncategorised Wiki 2.md': 'This is a sample Wiki',
    },
    ('Category', 'Japanese'): {
        'Category記載ありページ.md': 'Category: test-category',
        'Category記載なしページ1.md': '',
        'Category記載なしページ2.md': 'サンプル Wiki',
    },
}


@pytest.fixture(autouse=True)
def _cleanup_pycaches():
    before = set(glob.glob(os.path.join('.', '**', '__pycache__'), recursive=True))
    yield
    for pycache in before:
        if os.path.exists(pycache):
            shutil.rmtree(pycache)


@pytest.fixture
def wiki_workspace():
    base_path = os.path.join('.', 'test', 'wiki')

    def _build(group_by='Owner', language='English', file_maps=None):
        if file_maps is None:
            file_maps = _DEFAULT_FILE_MAPS[(group_by, language)]
        os.makedirs(base_path, exist_ok=True)
        for wiki, namespace in file_maps.items():
            with open(os.path.join(base_path, wiki), 'w') as f:
                f.write(namespace)
        return base_path

    yield _build
    if os.path.exists(base_path):
        shutil.rmtree(base_path)
