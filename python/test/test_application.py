import sys
import unittest
import os
import glob
import shutil
sys.path.append('./src')

from application import Application

class TestApplication(unittest.TestCase):
    def setUp(self, base_path = os.path.join('.', 'test', 'wiki'), group_by = 'Owner', language = 'English'):
        self.base_path = base_path
        self.group_by  = group_by
        self.language  = language
        self.pycaches  = glob.glob(os.path.join('.', '**', '__pycache__'), recursive = True)
        if not os.path.exists(self.base_path):
            os.makedirs(self.base_path)
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
        with self.assertRaises(ValueError) as e:
            Application(base_path = self.base_path, group_by = '-x', language = self.language)
        self.assertEqual(str(e.exception), 'Unknown group_by: `-x`')

    def test_validate_language(self):
        with self.assertRaises(ValueError) as e:
            Application(base_path = self.base_path, group_by = self.group_by, language = '-spa')
        self.assertEqual(str(e.exception), 'Unknown language: `-spa`')

    def test_run(self):
        with self.assertRaises(NotImplementedError, msg = 'This method must be implemented in each subclass.'):
            Application(base_path = self.base_path, group_by = self.group_by, language = self.language).run()

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
