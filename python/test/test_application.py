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
        with self.assertRaises(ValueError) as e:
            Application(base_path = self.base_path, genre = '-x')
        self.assertEqual(str(e.exception), 'Unknown genre: `-x`')

    def test_run(self):
        with self.assertRaises(NotImplementedError, msg = 'This method must be implemented in each subclass.'):
            Application(base_path = self.base_path, genre = self.genre).run()

    # private

    def __test_file_maps__(self):
        match self.genre:
            case '-o' | '--owner':
                return {
                    'Owned Wiki.md': 'Owner: @test-owner',
                    'Unowned but Necessary Wiki.md': 'Owner: Unowned but Necessary',
                    'Unknown Owner nor Necessity Wiki.md': 'Owner: Unknown Owner nor Necessity',
                    'Unowned Wiki 1.md': '',
                    'Unowned Wiki 2.md': 'This is a sample Wiki'
                }
            case '-c' | '--category':
                return {
                    'Categorised Wiki.md': 'Category: test-category',
                    'Uncategorised Wiki1.md': '',
                    'Uncategorised Wiki2.md': 'This is a sample Wiki',
                }

if __name__ == '__main__':
    unittest.main()
