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
        self.application.run()

    def tearDown(self):
        if os.path.exists(self.base_path):
            shutil.rmtree(self.base_path)
        for pycache in self.pycaches:
            if os.path.exists(pycache):
                shutil.rmtree(pycache)

    def test_run(self):
        self.assertEqual(self.application.base_path, self.base_path)
        self.assertEqual(self.application.path_to_home, os.path.join(self.base_path, 'Home.md'))
        self.assertEqual(self.application.path_to_sidebar, os.path.join(self.base_path, '_Sidebar.md'))
        self.assertEqual(self.application.target_paths, [
            './test/wiki/Ownerチームが不明だが必要なページ.md',
            './test/wiki/Ownerチーム・要or不要が不明なページ.md',
            './test/wiki/Owner記名ありページ.md',
            './test/wiki/Owner記名なしページ1.md',
            './test/wiki/Owner記名なしページ2.md',
        ])
        self.assertEqual(self.application.owner_and_wiki_maps, {
            'Ownerチームが不明だが必要なページ群': ['Ownerチームが不明だが必要なページ.md'],
            'Ownerチーム・要or不要が不明なページ群': ['Ownerチーム・要or不要が不明なページ.md'],
            '@test-owner': ['Owner記名ありページ.md'],
            'Owner記名なし': ['Owner記名なしページ1.md', 'Owner記名なしページ2.md']
        })

if __name__ == '__main__':
    unittest.main()
