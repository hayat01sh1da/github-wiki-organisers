import sys
import unittest
import os
import glob
import shutil
sys.path.append('./src')
from application import Application

class TestApplication(unittest.TestCase):
    def setUp(self):
        self.base_path = os.path.join('.', 'test', 'wiki')
        self.pycaches  = glob.glob(os.path.join('.', '**', '__pycache__'), recursive = True)
        if not os.path.exists(self.base_path):
            os.makedirs(self.base_path)
        test_file_maps = {
            'Owner記名ありページ.md': 'Owner: @test-owner',
            'Ownerチームが不明だが必要なページ.md': 'Owner: Ownerチームが不明だが必要なページ群',
            'Ownerチーム・要or不要が不明なページ.md': 'Owner: Ownerチーム・要or不要が不明なページ群',
            'Owner記名なしページ1.md': '',
            'Owner記名なしページ2.md': 'This is a sample Wiki'
        }
        for wiki, namespace in test_file_maps.items():
            with open(os.path.join(self.base_path, wiki), 'w') as f:
                f.write(namespace)
        self.application = Application(self.base_path)

    def tearDown(self):
        if os.path.exists(self.base_path):
            shutil.rmtree(self.base_path)
        for pycache in self.pycaches:
            if os.path.exists(pycache):
                shutil.rmtree(pycache)

    def test_run(self):
        with self.assertRaises(NotImplementedError, msg = 'This method must be implemented in each subclass.'):
            self.application.run()

if __name__ == '__main__':
    unittest.main()
