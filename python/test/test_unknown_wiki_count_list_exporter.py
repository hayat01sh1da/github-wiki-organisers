import sys
import os
import unittest
sys.path.append('./src')
sys.path.append('./test')

from unknown_wiki_count_list_exporter import UnknownWikiCountListExporter
from test_application import TestApplication

class TestUnknownWikiCountListExporter(TestApplication):
    def setUp(self, genre = '-o', language = '-en'):
        super().setUp(genre = genre, language = language)
        UnknownWikiCountListExporter(self.base_path, genre = genre, language = language).run()
        path_to_unknown_wiki_count_list = os.path.join(self.base_path, 'unknown_wiki_count_list_by_namespace.txt')
        with open(path_to_unknown_wiki_count_list) as f:
            self.unknown_wiki_count_list = f.read()

class EnglishOwnerTestRegularCase1(TestUnknownWikiCountListExporter):
    def test_run(self):
        self.assertEqual(self.unknown_wiki_count_list, self.__unknown_wiki_count_list_by_namespace__())

    # private

    def __unknown_wiki_count_list_by_namespace__(self):
        lst  = 'Unknown Owner nor Necessity: 1\n'
        lst += 'Unowned but Necessary: 1\n'
        lst += 'Unowned: 2\n'

        return lst

class EnglishOwnerTestRegularCase2(TestUnknownWikiCountListExporter):
    def test_run(self):
        self.assertEqual(self.unknown_wiki_count_list, self.__unknown_wiki_count_list_by_namespace__())

    # private

    def __unknown_wiki_count_list_by_namespace__(self):
        lst  = 'Unknown Owner nor Necessity: 1\n'
        lst += 'Unowned but Necessary: 1\n'
        lst += 'Unowned: 2\n'

        return lst

    def __test_file_maps__(self):
        return {
            'Unowned but Necessary Wiki.md': 'Owner: Unowned but Necessary',
            'Unknown Owner nor Necessity Wiki.md': 'Owner: Unknown Owner nor Necessity',
            'Unowned Wiki 1.md': '',
            'Unowned Wiki 2.md': 'This is a sample Wiki'
        }

class EnglishOwnerTestIrregularCase1(TestUnknownWikiCountListExporter):
    def test_run(self):
        self.assertEqual(self.unknown_wiki_count_list, self.__unknown_wiki_count_list_by_namespace__())

    # private

    def __unknown_wiki_count_list_by_namespace__(self):
        lst  = 'Unknown Owner nor Necessity: 0\n'
        lst += 'Unowned but Necessary: 1\n'
        lst += 'Unowned: 2\n'

        return lst

    def __test_file_maps__(self):
        return {
            'Owned Wiki.md': 'Owner: @test-owner',
            'Unowned but Necessary Wiki.md': 'Owner: Unowned but Necessary',
            'Unowned Wiki 1.md': '',
            'Unowned Wiki 2.md': 'This is a sample Wiki'
        }

class EnglishOwnerTestIrregularCase2(TestUnknownWikiCountListExporter):
    def test_run(self):
        self.assertEqual(self.unknown_wiki_count_list, self.__unknown_wiki_count_list_by_namespace__())

    # private

    def __unknown_wiki_count_list_by_namespace__(self):
        lst  = 'Unknown Owner nor Necessity: 1\n'
        lst += 'Unowned but Necessary: 0\n'
        lst += 'Unowned: 2\n'

        return lst

    def __test_file_maps__(self):
        return {
            'Owned Wiki.md': 'Owner: @test-owner',
            'Unknown Owner nor Necessity Wiki.md': 'Owner: Unknown Owner nor Necessity',
            'Unowned Wiki 1.md': '',
            'Unowned Wiki 2.md': 'This is a sample Wiki'
        }

class EnglishOwnerTestIrregularCase3(TestUnknownWikiCountListExporter):
    def test_run(self):
        self.assertEqual(self.unknown_wiki_count_list, self.__unknown_wiki_count_list_by_namespace__())

    # private

    def __unknown_wiki_count_list_by_namespace__(self):
        lst  = 'Unknown Owner nor Necessity: 1\n'
        lst += 'Unowned but Necessary: 1\n'
        lst += 'Unowned: 0\n'

        return lst

    def __test_file_maps__(self):
        return {
            'Owned Wiki.md': 'Owner: @test-owner',
            'Unowned but Necessary Wiki.md': 'Owner: Unowned but Necessary',
            'Unknown Owner nor Necessity Wiki.md': 'Owner: Unknown Owner nor Necessity',
        }

class EnglishCategoryTestRegularCase(TestUnknownWikiCountListExporter):
    def setUp(self):
        super().setUp(genre = '-c')

    def test_run(self):
        self.assertEqual(self.unknown_wiki_count_list, self.__unknown_wiki_count_list_by_namespace__())

    # private

    def __unknown_wiki_count_list_by_namespace__(self):
        return 'Uncategorised: 2\n'

class EnglishCategoryTestIrregularCase(TestUnknownWikiCountListExporter):
    def setUp(self):
        super().setUp(genre = '-c')

    def test_run(self):
        self.assertEqual(self.unknown_wiki_count_list, self.__unknown_wiki_count_list_by_namespace__())

    # private

    def __unknown_wiki_count_list_by_namespace__(self):
        lst = 'Uncategorised: 5\n'

        return lst

    def __test_file_maps__(self):
        return {
            'Owned Wiki.md': 'Owner: @test-owner',
            'Unowned but Necessary Wiki.md': 'Owner: Unowned but Necessary',
            'Unknown Owner nor Necessity Wiki.md': 'Owner: Unknown Owner nor Necessity',
            'Unowned Wiki 1.md': '',
            'Unowned Wiki 2.md': 'This is a sample Wiki'
        }

class JapaneseOwnerTestRegularCase1(TestUnknownWikiCountListExporter):
    def setUp(self):
        super().setUp(language = '-ja')

    def test_run(self):
        self.assertEqual(self.unknown_wiki_count_list, self.__unknown_wiki_count_list_by_namespace__())

    # private

    def __unknown_wiki_count_list_by_namespace__(self):
        lst  = 'Ownerチームが不明だが必要なページ群: 1\n'
        lst += 'Ownerチーム・要or不要が不明なページ群: 1\n'
        lst += 'Owner記名なし: 2\n'

        return lst

class JapaneseOwnerTestRegularCase2(TestUnknownWikiCountListExporter):
    def setUp(self):
        super().setUp(language = '-ja')

    def test_run(self):
        self.assertEqual(self.unknown_wiki_count_list, self.__unknown_wiki_count_list_by_namespace__())

    # private

    def __unknown_wiki_count_list_by_namespace__(self):
        lst  = 'Ownerチームが不明だが必要なページ群: 1\n'
        lst += 'Ownerチーム・要or不要が不明なページ群: 1\n'
        lst += 'Owner記名なし: 2\n'

        return lst

    def __test_file_maps__(self):
        return {
            'Ownerチームが不明だが必要なページ.md': 'Owner: Ownerチームが不明だが必要なページ群',
            'Ownerチーム・要or不要が不明なページ.md': 'Owner: Ownerチーム・要or不要が不明なページ群',
            'Owner記名なしページ1.md': '',
            'Owner記名なしページ2.md': 'サンプル Wiki'
        }

class JapaneseOwnerTestIrregularCase1(TestUnknownWikiCountListExporter):
    def setUp(self):
        super().setUp(language = '-ja')

    def test_run(self):
        self.assertEqual(self.unknown_wiki_count_list, self.__unknown_wiki_count_list_by_namespace__())

    # private

    def __unknown_wiki_count_list_by_namespace__(self):
        lst  = 'Ownerチームが不明だが必要なページ群: 1\n'
        lst += 'Ownerチーム・要or不要が不明なページ群: 0\n'
        lst += 'Owner記名なし: 2\n'

        return lst

    def __test_file_maps__(self):
        return {
            'Owner記名ありページ.md': 'Owner: @test-owner',
            'Ownerチームが不明だが必要なページ.md': 'Owner: Ownerチームが不明だが必要なページ群',
            'Owner記名なしページ1.md': '',
            'Owner記名なしページ2.md': 'サンプル Wiki'
        }

class JapaneseOwnerTestIrregularCase2(TestUnknownWikiCountListExporter):
    def setUp(self):
        super().setUp(language = '-ja')

    def test_run(self):
        self.assertEqual(self.unknown_wiki_count_list, self.__unknown_wiki_count_list_by_namespace__())

    # private

    def __unknown_wiki_count_list_by_namespace__(self):
        lst  = 'Ownerチームが不明だが必要なページ群: 0\n'
        lst += 'Ownerチーム・要or不要が不明なページ群: 1\n'
        lst += 'Owner記名なし: 2\n'

        return lst

    def __test_file_maps__(self):
        return {
            'Owner記名ありページ.md': 'Owner: @test-owner',
            'Ownerチーム・要or不要が不明なページ.md': 'Owner: Ownerチーム・要or不要が不明なページ群',
            'Owner記名なしページ1.md': '',
            'Owner記名なしページ2.md': 'サンプル Wiki'
        }

class JapaneseOwnerTestIrregularCase3(TestUnknownWikiCountListExporter):
    def setUp(self):
        super().setUp(language = '-ja')

    def test_run(self):
        self.assertEqual(self.unknown_wiki_count_list, self.__unknown_wiki_count_list_by_namespace__())

    # private

    def __unknown_wiki_count_list_by_namespace__(self):
        lst  = 'Ownerチームが不明だが必要なページ群: 1\n'
        lst += 'Ownerチーム・要or不要が不明なページ群: 1\n'
        lst += 'Owner記名なし: 0\n'

        return lst

    def __test_file_maps__(self):
        return {
            'Owner記名ありページ.md': 'Owner: @test-owner',
            'Ownerチームが不明だが必要なページ.md': 'Owner: Ownerチームが不明だが必要なページ群',
            'Ownerチーム・要or不要が不明なページ.md': 'Owner: Ownerチーム・要or不要が不明なページ群',
        }

class JapaneseCategoryTestRegularCase(TestUnknownWikiCountListExporter):
    def setUp(self):
        super().setUp(genre = '-c', language = '-ja')

    def test_run(self):
        self.assertEqual(self.unknown_wiki_count_list, self.__unknown_wiki_count_list_by_namespace__())

    # private

    def __unknown_wiki_count_list_by_namespace__(self):
        return 'Category記載なし: 2\n'

class JapaneseCategoryTestIrregularCase(TestUnknownWikiCountListExporter):
    def setUp(self):
        super().setUp(genre = '-c', language = '-ja')

    def test_run(self):
        self.assertEqual(self.unknown_wiki_count_list, self.__unknown_wiki_count_list_by_namespace__())

    # private

    def __unknown_wiki_count_list_by_namespace__(self):
        lst = 'Category記載なし: 5\n'

        return lst

    def __test_file_maps__(self):
        return {
            'Owner記名ありページ.md': 'Owner: @test-owner',
            'Ownerチームが不明だが必要なページ.md': 'Owner: Ownerチームが不明だが必要なページ群',
            'Ownerチーム・要or不要が不明なページ.md': 'Owner: Ownerチーム・要or不要が不明なページ群',
            'Owner記名なしページ1.md': '',
            'Owner記名なしページ2.md': 'サンプル Wiki'
        }

if __name__ == '__main__':
    unittest.main()
