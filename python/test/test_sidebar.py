import sys
import os
import unittest
sys.path.append('./src')
sys.path.append('./test')
from sidebar import Sidebar
from test_application import TestApplication

class TestSidebar(TestApplication):
    def setUp(self, genre = '-o'):
        super().setUp(genre = genre)
        Sidebar(self.base_path, genre = genre).run()
        path_to_sidebar = os.path.join(self.base_path, '_Sidebar.md')
        with open(path_to_sidebar) as f:
            self.sidebar = f.read()

class OwnedHomeTest(TestSidebar):
    def test_run(self):
        self.assertEqual(self.sidebar, self.__wiki_list__())

    # private

    def __wiki_list__(self):
        lst  = '- [@test-owner](https://github.com/orgs/hayat01sh1da/teams/test-owner)\n'
        lst += '  - [[Owner記名ありページ]]\n'
        lst += '- Ownerチームが不明だが必要なページ群\n'
        lst += '  - [[Ownerチームが不明だが必要なページ]]\n'
        lst += '- Ownerチーム・要or不要が不明なページ群\n'
        lst += '  - [[Ownerチーム・要or不要が不明なページ]]\n'
        lst += '- Owner記名なし\n'
        lst += '  - [[Owner記名なしページ1]]\n'
        lst += '  - [[Owner記名なしページ2]]\n'

        return lst
class PlainHomeTest(TestSidebar):
    def setUp(self):
        super().setUp(genre = '-c')

    def test_run(self):
        self.assertEqual(self.sidebar, self.__sidebar_passage__())

    # private

    def __sidebar_passage__(self):
        lst  = '- test-category\n'
        lst += '  - [[Category記載ありページ]]\n'
        lst += '- Category記載なし\n'
        lst += '  - [[Category記載なしページ1]]\n'
        lst += '  - [[Category記載なしページ2]]\n'

        return lst

if __name__ == '__main__':
    unittest.main()
