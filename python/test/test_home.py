import sys
import os
import unittest
sys.path.append('./src')
sys.path.append('./test')

from home import Home
from test_application import TestApplication

class TestHome(TestApplication):
    def setUp(self, genre = '-o', language = '-en'):
        super().setUp(genre = genre, language = language)
        Home(base_path = self.base_path, genre = genre, language = language).run()
        path_to_home = os.path.join(self.base_path, 'Home.md')
        with open(path_to_home) as f:
            self.home = f.read()

class EnglishOwnedHomeTest(TestHome):
    def test_run(self):
        self.assertEqual(self.home, self.__home_passage__())

    # private

    def __home_passage__(self):
        passage  = '## How to Manage Wiki Pages\n'
        passage += '\n'
        passage += 'This Home page manage wikis by owner group.\n'
        passage += '\n'
        passage += 'Absence of ownership declaration worsens maintainability and searchability because it makes ambiguous which team the responsibility belongs to.  \n'
        passage += 'Kindly make sure to articulate `Owner: @OWNER_TEAM` of the top of each of your wiki page to avoid it.\n'
        passage += '\n'
        passage += 'Also, please keep in mind that you do not have to edit Home and Sidebar by yourself, which are automatically updated by a GitHub Actions cron job.\n'
        passage += '\n'
        passage += '## [@test-owner](https://github.com/orgs/hayat01sh1da/teams/test-owner)\n'
        passage += '\n'
        passage += '- [[Owned Wiki]]\n'
        passage += '\n'
        passage += '## Unknown Owner nor Necessity\n'
        passage += '\n'
        passage += '- [[Unknown Owner nor Necessity Wiki]]\n'
        passage += '\n'
        passage += '## Unowned but Necessary\n'
        passage += '\n'
        passage += '- [[Unowned but Necessary Wiki]]\n'
        passage += '\n'
        passage += '## Unowned\n'
        passage += '\n'
        passage += '- [[Unowned Wiki 1]]\n'
        passage += '- [[Unowned Wiki 2]]\n'

        return passage

class EnglishPlainHomeTest(TestHome):
    def setUp(self):
        super().setUp(genre = '-c')

    def test_run(self):
        self.assertEqual(self.home, self.__home_passage__())

    # private

    def __home_passage__(self):
        passage  = '## How to Manage Wiki Pages\n'
        passage += '\n'
        passage += 'This Home page manage wikis by category group.\n'
        passage += '\n'
        passage += 'Absence of category declaration worsens maintainability and searchability.  \n'
        passage += 'Kindly make sure to articulate `Category: CATEGORY_NAME` of the top of each of your wiki page to avoid it.\n'
        passage += '\n'
        passage += 'Also, please keep in mind that you do not have to edit Home and Sidebar by yourself, which are automatically updated by a GitHub Actions cron job.\n'
        passage += '\n'
        passage += '## test-category\n'
        passage += '\n'
        passage += '- [[Categorised Wiki]]\n'
        passage += '\n'
        passage += '## Uncategorised\n'
        passage += '\n'
        passage += '- [[Uncategorised Wiki 1]]\n'
        passage += '- [[Uncategorised Wiki 2]]\n'

        return passage

class JapaneseOwnedHomeTest(TestHome):
    def setUp(self):
        super().setUp(language = '-ja')

    def test_run(self):
        self.assertEqual(self.home, self.__home_passage__())

    # private

    def __home_passage__(self):
        passage  = '## Wiki ページの運用ルール\n'
        passage += '\n'
        passage += 'このページは Owner チームごとに Wiki をグルーピングして一覧化しています。\n'
        passage += '\n'
        passage += 'Ownership をどのチームが持つのかが不明だと、責任の所在が不明瞭になり、保守性の悪化に伴うノイズの増加と検索性の悪化が発生します。  \n'
        passage += '治安維持のため、各ページの冒頭に `Owner: @オーナーチーム` を明記して頂きますようよろしくお願いします。\n'
        passage += '\n'
        passage += 'なお、Home・Sidebar は専用の定期実行ジョブで自動更新しますので編集は不要です。\n'
        passage += '\n'
        passage += '## [@test-owner](https://github.com/orgs/hayat01sh1da/teams/test-owner)\n'
        passage += '\n'
        passage += '- [[Owner記名ありページ]]\n'
        passage += '\n'
        passage += '## Ownerチームが不明だが必要なページ群\n'
        passage += '\n'
        passage += '- [[Ownerチームが不明だが必要なページ]]\n'
        passage += '\n'
        passage += '## Ownerチーム・要or不要が不明なページ群\n'
        passage += '\n'
        passage += '- [[Ownerチーム・要or不要が不明なページ]]\n'
        passage += '\n'
        passage += '## Owner記名なし\n'
        passage += '\n'
        passage += '- [[Owner記名なしページ1]]\n'
        passage += '- [[Owner記名なしページ2]]\n'

        return passage

class JapanesePlainHomeTest(TestHome):
    def setUp(self):
        super().setUp(genre = '-c', language = '-ja')

    def test_run(self):
        self.assertEqual(self.home, self.__home_passage__())

    # private

    def __home_passage__(self):
        passage  = '## Wiki ページの運用ルール\n'
        passage += '\n'
        passage += 'このページは Category ごとに Wiki をグルーピングして一覧化しています。\n'
        passage += '\n'
        passage += 'Category が不明だと、保守性と検索性の悪化が発生します。  \n'
        passage += '治安維持のため、各ページの冒頭に `Category: カテゴリー名` を明記して頂きますようよろしくお願いします。\n'
        passage += '\n'
        passage += 'なお、Home・Sidebar は専用の定期実行ジョブで自動更新しますので編集は不要です。\n'
        passage += '\n'
        passage += '## test-category\n'
        passage += '\n'
        passage += '- [[Category記載ありページ]]\n'
        passage += '\n'
        passage += '## Category記載なし\n'
        passage += '\n'
        passage += '- [[Category記載なしページ1]]\n'
        passage += '- [[Category記載なしページ2]]\n'

        return passage

if __name__ == '__main__':
    unittest.main()
