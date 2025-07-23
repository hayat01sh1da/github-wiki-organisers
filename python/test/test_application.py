import sys
import unittest
import os
import glob
import shutil
sys.path.append('./src')

from application import Application

class TestApplication(unittest.TestCase):
    def setUp(self, base_path = os.path.join('.', 'test', 'wiki'), genre = '-o'):
        self.base_path = base_path
        self.genre     = genre
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

    def test_validate(self):
        with self.assertRaises(ValueError, msg = 'Unknown genre: `-x`'):
            Application(base_path = self.base_path, genre = '-x').validate()

    def test_run(self):
        with self.assertRaises(NotImplementedError, msg = 'This method must be implemented in each subclass.'):
            Application(base_path = self.base_path, genre = self.genre).run()

    # private

    def __test_file_maps__(self):
        match self.genre:
            case '-o' | '--owner':
                return {
                    'Owner記名ありページ.md': 'Owner: @test-owner',
                    'Ownerチームが不明だが必要なページ.md': 'Owner: Ownerチームが不明だが必要なページ群',
                    'Ownerチーム・要or不要が不明なページ.md': 'Owner: Ownerチーム・要or不要が不明なページ群',
                    'Owner記名なしページ1.md': '',
                    'Owner記名なしページ2.md': 'This is a sample Wiki'
                }
            case '-c' | '--category':
                return {
                    'Category記載ありページ.md': 'Category: test-category',
                    'Category記載なしページ1.md': '',
                    'Category記載なしページ2.md': 'This is a sample Wiki',
                }

if __name__ == '__main__':
    unittest.main()
