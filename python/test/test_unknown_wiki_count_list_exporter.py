import sys
import os
import unittest
sys.path.append('./src')
sys.path.append('./test')

from export_unknown_wiki_count_list_by_namespace import UnknownWikiCountListExporter
from test_application import TestApplication

class TestUnknownWikiCountListExporter(TestApplication):
    def setUp(self, genre = '-o'):
        super().setUp(genre = genre)
        UnknownWikiCountListExporter(self.base_path, genre = genre).run()
        path_to_unknown_wiki_count_list = os.path.join(self.base_path, 'unknown_wiki_count_list_by_namespace.txt')
        with open(path_to_unknown_wiki_count_list) as f:
            self.unknown_wiki_count_list = f.read()

class OwnershipTest(TestUnknownWikiCountListExporter):
    pass

class RegularCase1(OwnershipTest):
    def test_run(self):
        self.assertEqual(self.unknown_wiki_count_list, self.__unknown_wiki_count_list_by_namespace__())

    # private

    def __unknown_wiki_count_list_by_namespace__(self):
        lst  = 'Ownerチームが不明だが必要なページ群: 1件\n'
        lst += 'Ownerチーム・要or不要が不明なページ群: 1件\n'
        lst += 'Owner記名なし: 2件\n'

        return lst

class RegularCase2(OwnershipTest):
    def test_run(self):
        self.assertEqual(self.unknown_wiki_count_list, self.__unknown_wiki_count_list_by_namespace__())

    # private

    def __unknown_wiki_count_list_by_namespace__(self):
        lst  = 'Ownerチームが不明だが必要なページ群: 1件\n'
        lst += 'Ownerチーム・要or不要が不明なページ群: 1件\n'
        lst += 'Owner記名なし: 2件\n'

        return lst

    def __test_file_maps__(self):
        return {
            'Ownerチームが不明だが必要なページ.md': 'Owner: Ownerチームが不明だが必要なページ群',
            'Ownerチーム・要or不要が不明なページ.md': 'Owner: Ownerチーム・要or不要が不明なページ群',
            'Owner記名なしページ1.md': '',
            'Owner記名なしページ2.md': 'This is a sample Wiki'
        }

class IrregularCase1(TestUnknownWikiCountListExporter):
    def test_run(self):
        self.assertEqual(self.unknown_wiki_count_list, self.__unknown_wiki_count_list_by_namespace__())

    # private

    def __unknown_wiki_count_list_by_namespace__(self):
        lst  = 'Ownerチームが不明だが必要なページ群: 0件\n'
        lst += 'Ownerチーム・要or不要が不明なページ群: 1件\n'
        lst += 'Owner記名なし: 2件\n'

        return lst

    def __test_file_maps__(self):
        return {
            'Owner記名ありページ.md': 'Owner: @test-owner',
            'Ownerチーム・要or不要が不明なページ.md': 'Owner: Ownerチーム・要or不要が不明なページ群',
            'Owner記名なしページ1.md': '',
            'Owner記名なしページ2.md': 'This is a sample Wiki'
        }

class IrregularCase2(TestUnknownWikiCountListExporter):
    def test_run(self):
        self.assertEqual(self.unknown_wiki_count_list, self.__unknown_wiki_count_list_by_namespace__())

    # private

    def __unknown_wiki_count_list_by_namespace__(self):
        lst  = 'Ownerチームが不明だが必要なページ群: 1件\n'
        lst += 'Ownerチーム・要or不要が不明なページ群: 0件\n'
        lst += 'Owner記名なし: 2件\n'

        return lst

    def __test_file_maps__(self):
        return {
            'Owner記名ありページ.md': 'Owner: @test-owner',
            'Ownerチームが不明だが必要なページ.md': 'Owner: Ownerチームが不明だが必要なページ群',
            'Owner記名なしページ1.md': '',
            'Owner記名なしページ2.md': 'This is a sample Wiki'
        }

class IrregularCase3(TestUnknownWikiCountListExporter):
    def test_run(self):
        self.assertEqual(self.unknown_wiki_count_list, self.__unknown_wiki_count_list_by_namespace__())

    # private

    def __unknown_wiki_count_list_by_namespace__(self):
        lst  = 'Ownerチームが不明だが必要なページ群: 1件\n'
        lst += 'Ownerチーム・要or不要が不明なページ群: 1件\n'
        lst += 'Owner記名なし: 0件\n'

        return lst

    def __test_file_maps__(self):
        return {
            'Owner記名ありページ.md': 'Owner: @test-owner',
            'Ownerチームが不明だが必要なページ.md': 'Owner: Ownerチームが不明だが必要なページ群',
            'Ownerチーム・要or不要が不明なページ.md': 'Owner: Ownerチーム・要or不要が不明なページ群',
        }

class CategoryTest(TestUnknownWikiCountListExporter):
    def setUp(self):
        super().setUp(genre = '-c')

class RegularCase(CategoryTest):
    def test_run(self):
        self.assertEqual(self.unknown_wiki_count_list, self.__unknown_wiki_count_list_by_namespace__())

    # private

    def __unknown_wiki_count_list_by_namespace__(self):
        lst  = 'Category記載なし: 2件\n'
        lst += 'test-category: 1件\n'

        return lst

class IrregularCase(CategoryTest):
    def test_run(self):
        self.assertEqual(self.unknown_wiki_count_list, self.__unknown_wiki_count_list_by_namespace__())

    # private

    def __unknown_wiki_count_list_by_namespace__(self):
        lst = 'Category記載なし: 4件\n'

        return lst

    def __test_file_maps__(self):
        return {
            'Ownerチームが不明だが必要なページ.md': 'Owner: Ownerチームが不明だが必要なページ群',
            'Ownerチーム・要or不要が不明なページ.md': 'Owner: Ownerチーム・要or不要が不明なページ群',
            'Owner記名なしページ1.md': '',
            'Owner記名なしページ2.md': 'This is a sample Wiki'
        }

if __name__ == '__main__':
    unittest.main()
