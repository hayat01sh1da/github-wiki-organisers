import sys
import os
import unittest
sys.path.append('./src')
sys.path.append('./test')
from directory import Directory
from test_application import TestApplication

class TestDirectory(TestApplication):
    def setUp(self):
        super().setUp()
        self.dir_to_delete = os.path.join(self.base_path, 'foo')
        os.makedirs(self.dir_to_delete)
        Directory(self.base_path).run()

    def test_run(self):
        self.assertEqual(os.path.isfile(os.path.join(self.base_path, 'test-owner', 'Owner記名ありページ.md')), True)
        self.assertEqual(os.path.isfile(os.path.join(self.base_path, 'Ownerチームが不明だが必要なページ群', 'Ownerチームが不明だが必要なページ.md')), True)
        self.assertEqual(os.path.isfile(os.path.join(self.base_path, 'Ownerチーム・要or不要が不明なページ群', 'Ownerチーム・要or不要が不明なページ.md')), True)
        self.assertEqual(os.path.isfile(os.path.join(self.base_path, 'Owner記名なし', 'Owner記名なしページ1.md')), True)
        self.assertEqual(os.path.isfile(os.path.join(self.base_path, 'Owner記名なし', 'Owner記名なしページ2.md')), True)
        self.assertEqual(os.path.isfile(self.dir_to_delete), False)

if __name__ == '__main__':
    unittest.main()
