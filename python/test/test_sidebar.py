import sys
import os
import unittest
sys.path.append('./src')
sys.path.append('./test')
from sidebar import Sidebar
from test_application import TestApplication

class TestSidebar(TestApplication):
    def setUp(self):
        super().setUp()
        Sidebar(self.base_path).run()
        path_to_sidebar = os.path.join(self.base_path, '_Sidebar.md')
        with open(path_to_sidebar) as f:
            self.sidebar = f.read()

    def test_run(self):
        self.assertEqual(self.sidebar, self.__wiki_list__())

    # private

    def __wiki_list__(self):
        list  = '- [@test-owner](https://github.com/orgs/quipper/teams/test-owner)\n'
        list += '  - [[Owner記名ありページ]]\n'
        list += '- Ownerチームが不明だが必要なページ群\n'
        list += '  - [[Ownerチームが不明だが必要なページ]]\n'
        list += '- Ownerチーム・要or不要が不明なページ群\n'
        list += '  - [[Ownerチーム・要or不要が不明なページ]]\n'
        list += '- Owner記名なし\n'
        list += '  - [[Owner記名なしページ1]]\n'
        list += '  - [[Owner記名なしページ2]]\n'
        return list

if __name__ == '__main__':
    unittest.main()
