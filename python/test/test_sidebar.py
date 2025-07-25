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
        lst += '  - [[Owned Wiki]]\n'
        lst += '- Unknown Owner nor Necessity\n'
        lst += '  - [[Unknown Owner nor Necessity Wiki]]\n'
        lst += '- Unowned but Necessary\n'
        lst += '  - [[Unowned but Necessary Wiki]]\n'
        lst += '- Unowned\n'
        lst += '  - [[Unowned Wiki 1]]\n'
        lst += '  - [[Unowned Wiki 2]]\n'

        return lst
class PlainHomeTest(TestSidebar):
    def setUp(self):
        super().setUp(genre = '-c')

    def test_run(self):
        self.assertEqual(self.sidebar, self.__wiki_list__())

    # private

    def __wiki_list__(self):
        lst  = '- test-category\n'
        lst += '  - [[Categorised Wiki]]\n'
        lst += '- Uncategorised\n'
        lst += '  - [[Uncategorised Wiki1]]\n'
        lst += '  - [[Uncategorised Wiki2]]\n'

        return lst

if __name__ == '__main__':
    unittest.main()
