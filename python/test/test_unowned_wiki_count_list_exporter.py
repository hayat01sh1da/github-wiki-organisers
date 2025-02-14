import sys
import os
import unittest
sys.path.append('./src')
sys.path.append('./test')
from unowned_wiki_count_list_exporter import UnknownWikiCountListExporter
from test_application import TestApplication

class TestUnknownWikiCountListExporter(TestApplication):
    def setUp(self):
        super().setUp()
        UnknownWikiCountListExporter(self.base_path).run()
        path_to_unowned_wiki_count_list = os.path.join(self.base_path, 'unowned_wiki_count_list_by_namespace.txt')
        with open(path_to_unowned_wiki_count_list) as f:
            self.unowned_wiki_count_list = f.read()

class RegularCase1(TestUnknownWikiCountListExporter):
    def test_run(self):
        self.assertEqual(self.unowned_wiki_count_list, self.__unowned_wiki_count_list_by_namespace__())

    # private

    def __unowned_wiki_count_list_by_namespace__(self):
        lists  = 'Ownerチームが不明だが必要なページ群: 1件\n'
        lists += 'Ownerチーム・要or不要が不明なページ群: 1件\n'
        lists += 'Owner記名なし: 2件\n'
        return lists

class RegularCase2(TestUnknownWikiCountListExporter):
    def test_run(self):
        self.assertEqual(self.unowned_wiki_count_list, self.__unowned_wiki_count_list_by_namespace__())

    # private

    def __unowned_wiki_count_list_by_namespace__(self):
        lists  = 'Ownerチームが不明だが必要なページ群: 1件\n'
        lists += 'Ownerチーム・要or不要が不明なページ群: 1件\n'
        lists += 'Owner記名なし: 2件\n'
        return lists

    def __test_file_maps__(self):
        return {
            'Ownerチームが不明だが必要なページ.md': 'Owner: Ownerチームが不明だが必要なページ群',
            'Ownerチーム・要or不要が不明なページ.md': 'Owner: Ownerチーム・要or不要が不明なページ群',
            'Owner記名なしページ1.md': '',
            'Owner記名なしページ2.md': 'This is a sample Wiki'
        }

class IrregularCase1(TestUnknownWikiCountListExporter):
    def test_run(self):
        self.assertEqual(self.unowned_wiki_count_list, self.__unowned_wiki_count_list_by_namespace__())

    # private

    def __unowned_wiki_count_list_by_namespace__(self):
        lists  = 'Ownerチームが不明だが必要なページ群: 0件\n'
        lists += 'Ownerチーム・要or不要が不明なページ群: 1件\n'
        lists += 'Owner記名なし: 2件\n'
        return lists

    def __test_file_maps__(self):
        return {
            'Owner記名ありページ.md': 'Owner: @test-owner',
            'Ownerチーム・要or不要が不明なページ.md': 'Owner: Ownerチーム・要or不要が不明なページ群',
            'Owner記名なしページ1.md': '',
            'Owner記名なしページ2.md': 'This is a sample Wiki'
        }

class IrregularCase2(TestUnknownWikiCountListExporter):
    def test_run(self):
        self.assertEqual(self.unowned_wiki_count_list, self.__unowned_wiki_count_list_by_namespace__())

    # private

    def __unowned_wiki_count_list_by_namespace__(self):
        lists  = 'Ownerチームが不明だが必要なページ群: 1件\n'
        lists += 'Ownerチーム・要or不要が不明なページ群: 0件\n'
        lists += 'Owner記名なし: 2件\n'
        return lists

    def __test_file_maps__(self):
        return {
            'Owner記名ありページ.md': 'Owner: @test-owner',
            'Ownerチームが不明だが必要なページ.md': 'Owner: Ownerチームが不明だが必要なページ群',
            'Owner記名なしページ1.md': '',
            'Owner記名なしページ2.md': 'This is a sample Wiki'
        }

class IrregularCase3(TestUnknownWikiCountListExporter):
    def test_run(self):
        self.assertEqual(self.unowned_wiki_count_list, self.__unowned_wiki_count_list_by_namespace__())

    # private

    def __unowned_wiki_count_list_by_namespace__(self):
        lists  = 'Ownerチームが不明だが必要なページ群: 1件\n'
        lists += 'Ownerチーム・要or不要が不明なページ群: 1件\n'
        lists += 'Owner記名なし: 0件\n'
        return lists

    def __test_file_maps__(self):
        return {
            'Owner記名ありページ.md': 'Owner: @test-owner',
            'Ownerチームが不明だが必要なページ.md': 'Owner: Ownerチームが不明だが必要なページ群',
            'Ownerチーム・要or不要が不明なページ.md': 'Owner: Ownerチーム・要or不要が不明なページ群',
        }

if __name__ == '__main__':
    unittest.main()
