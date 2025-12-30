import sys
import unittest
import os
import glob
import shutil
sys.path.append('./src')

from application import Application

class TestApplication(unittest.TestCase):
    def setUp(self, base_path = os.path.join('.', 'test', 'wiki'), group_by = 'Owner', language = 'English', home_overflow = False):
        self.base_path      = base_path
        self.group_by       = group_by
        self.language       = language
        self.home_overflow  = home_overflow
        self.pycaches  = glob.glob(os.path.join('.', '**', '__pycache__'), recursive = True)
        os.makedirs(self.base_path, exist_ok = True)
        for wiki, namespace in self.__test_file_maps__().items():
            with open(os.path.join(self.base_path, wiki), 'w') as f:
                f.write(namespace)

    def tearDown(self):
        if os.path.exists(self.base_path):
            shutil.rmtree(self.base_path)
        for pycache in self.pycaches:
            if os.path.exists(pycache):
                shutil.rmtree(pycache)

    def test_validate_group_by(self):
        with self.assertRaises(ValueError) as cm:
            Application(base_path = self.base_path, group_by = 'Group', language = self.language, home_overflow = self.home_overflow)
        self.assertEqual(str(cm.exception), 'Invalid group_by: `Group`')

    def test_validate_language(self):
        with self.assertRaises(ValueError) as cm:
            Application(base_path = self.base_path, group_by = self.group_by, language = 'Spanish', home_overflow = self.home_overflow)
        self.assertEqual(str(cm.exception), 'Invalid language: `Spanish`')

    def test_validate_home_overflow(self):
        with self.assertRaises(ValueError) as cm:
            Application(base_path = self.base_path, group_by = self.group_by, language = self.language, home_overflow = 'foo')
        self.assertEqual(str(cm.exception), 'Invalid home_overflow: `foo` must be boolean')

    def test_run(self):
        with self.assertRaises(NotImplementedError) as cm:
            Application(
                base_path     = self.base_path,
                group_by      = self.group_by,
                language      = self.language,
                home_overflow = self.home_overflow,
            ).run()
        self.assertEqual('This method must be implemented in each subclass.', str(cm.exception))

    # private

    def __test_file_maps__(self):
        match self.group_by:
            case 'Owner':
                match self.language:
                    case 'English':
                        return {
                            'Owned Wiki.md': 'Owner: @test-owner',
                            'Unowned but Necessary Wiki.md': 'Owner: Unowned but Necessary',
                            'Unknown Owner nor Necessity Wiki.md': 'Owner: Unknown Owner nor Necessity',
                            'Unowned Wiki 1.md': '',
                            'Unowned Wiki 2.md': 'This is a sample Wiki'
                        }
                    case 'Japanese':
                        return {
                            'Owner記名ありページ.md': 'Owner: @test-owner',
                            'Ownerチームが不明だが必要なページ.md': 'Owner: Ownerチームが不明だが必要なページ群',
                            'Ownerチーム・要or不要が不明なページ.md': 'Owner: Ownerチーム・要or不要が不明なページ群',
                            'Owner記名なしページ1.md': '',
                            'Owner記名なしページ2.md': 'サンプル Wiki'
                        }
            case 'Category':
                match self.language:
                    case 'English':
                        return {
                            'Categorised Wiki.md': 'Category: test-category',
                            'Uncategorised Wiki 1.md': '',
                            'Uncategorised Wiki 2.md': 'This is a sample Wiki',
                        }
                    case 'Japanese':
                        return {
                            'Category記載ありページ.md': 'Category: test-category',
                            'Category記載なしページ1.md': '',
                            'Category記載なしページ2.md': 'サンプル Wiki'
                        }

if __name__ == '__main__':
    unittest.main()
