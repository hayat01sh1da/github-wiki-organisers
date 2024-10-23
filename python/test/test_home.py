import sys
import os
import unittest
sys.path.append('./src')
sys.path.append('./test')
from home import Home
from test_application import TestApplication

class TestHome(TestApplication):
    def setUp(self):
        super().setUp()
        Home(self.base_path).run()
        path_to_home = os.path.join(self.base_path, 'Home.md')
        with open(path_to_home) as f:
            self.home = f.read()

    def test_run(self):
        self.assertEqual(self.home, self.__home_passage__())

    # private

    def __home_passage__(self):
        passage  = 'このページは Owner チームごとに Wiki をグルーピングして一覧化しています。\n\n'
        passage += '## Wiki ページの運用ルール\n\n'
        passage += 'Ownership をどのチームが持つのかが不明だと、責任の所在が不明瞭になり、保守性の悪化に伴うノイズの増加と検索性の悪化が発生します。  \n'
        passage += '治安維持のため、各ページの冒頭に `Owner: {オーナーチーム名}` を明記して頂きますようよろしくお願いします。  \n'
        passage += 'なお、Home・Sidebar は専用のスクリプトで自動更新しますので編集は不要です。\n\n'
        passage += '## [@test-owner](https://github.com/orgs/quipper/teams/test-owner)\n\n'
        passage += '- [[Owner記名ありページ]]\n\n'
        passage += '## Ownerチームが不明だが必要なページ群\n\n'
        passage += '- [[Ownerチームが不明だが必要なページ]]\n\n'
        passage += '## Ownerチーム・要or不要が不明なページ群\n\n'
        passage += '- [[Ownerチーム・要or不要が不明なページ]]\n\n'
        passage += '## Owner記名なし\n\n'
        passage += '- [[Owner記名なしページ1]]\n'
        passage += '- [[Owner記名なしページ2]]\n'
        return passage

if __name__ == '__main__':
    unittest.main()
