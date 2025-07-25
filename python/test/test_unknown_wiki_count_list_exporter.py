import sys
import os
import unittest
sys.path.append('./src')
sys.path.append('./test')

from unknown_wiki_count_list_exporter import UnknownWikiCountListExporter
from test_application import TestApplication

class TestUnknownWikiCountListExporter(TestApplication):
    def setUp(self, genre = '-o', language = 'en'):
        super().setUp(genre = genre, language = language)
        UnknownWikiCountListExporter(self.base_path, genre = genre, language = language).run()
        path_to_unknown_wiki_count_list = os.path.join(self.base_path, 'unknown_wiki_count_list_by_namespace.txt')
        with open(path_to_unknown_wiki_count_list) as f:
            self.unknown_wiki_count_list = f.read()

class English(TestUnknownWikiCountListExporter):
    class OwnershipTest(TestUnknownWikiCountListExporter):
        class RegularCase1(TestUnknownWikiCountListExporter):
            def test_run(self):
                self.assertEqual(self.unknown_wiki_count_list, self.__unknown_wiki_count_list_by_namespace__())

            # private

            def __unknown_wiki_count_list_by_namespace__(self):
                lst  = 'Unknown Owner nor Necessity: 1\n'
                lst += 'Unowned but Necessary: 1\n'
                lst += 'Unowned: 2\n'

                return lst

        class RegularCase2(TestUnknownWikiCountListExporter):
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

        class IrregularCase1(TestUnknownWikiCountListExporter):
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

        class IrregularCase2(TestUnknownWikiCountListExporter):
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

        class IrregularCase3(TestUnknownWikiCountListExporter):
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

    class CategoryTest(TestUnknownWikiCountListExporter):
        class RegularCase(TestUnknownWikiCountListExporter):
            def setUp(self):
                super().setUp(genre = '-c')

            def test_run(self):
                self.assertEqual(self.unknown_wiki_count_list, self.__unknown_wiki_count_list_by_namespace__())

            # private

            def __unknown_wiki_count_list_by_namespace__(self):
                return 'Uncategorised: 2\n'

        class IrregularCase(TestUnknownWikiCountListExporter):
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

class Japanese(TestUnknownWikiCountListExporter):
    class OwnershipTest(TestUnknownWikiCountListExporter):
        class RegularCase1(TestUnknownWikiCountListExporter):
            def setUp(self):
                super().setUp(language = 'ja')

            def test_run(self):
                self.assertEqual(self.unknown_wiki_count_list, self.__unknown_wiki_count_list_by_namespace__())

            # private

            def __unknown_wiki_count_list_by_namespace__(self):
                lst  = 'Unknown Owner nor Necessity: 1\n'
                lst += 'Unowned but Necessary: 1\n'
                lst += 'Unowned: 2\n'

                return lst

        class RegularCase2(TestUnknownWikiCountListExporter):
            def setUp(self):
                super().setUp(language = 'ja')

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

        class IrregularCase1(TestUnknownWikiCountListExporter):
            def setUp(self):
                super().setUp(language = 'ja')

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

        class IrregularCase2(TestUnknownWikiCountListExporter):
            def setUp(self):
                super().setUp(language = 'ja')

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

        class IrregularCase3(TestUnknownWikiCountListExporter):
            def setUp(self):
                super().setUp(language = 'ja')

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

    class CategoryTest(TestUnknownWikiCountListExporter):
        class RegularCase(TestUnknownWikiCountListExporter):
            def setUp(self):
                super().setUp(genre = 'c', language = 'ja')

            def test_run(self):
                self.assertEqual(self.unknown_wiki_count_list, self.__unknown_wiki_count_list_by_namespace__())

            # private

            def __unknown_wiki_count_list_by_namespace__(self):
                return 'Uncategorised: 2\n'

        class IrregularCase(TestUnknownWikiCountListExporter):
            def setUp(self):
                super().setUp(genre = 'c', language = 'ja')

            def test_run(self):
                self.assertEqual(self.unknown_wiki_count_list, self.__unknown_wiki_count_list_by_namespace__())

            # private

            def __unknown_wiki_count_list_by_namespace__(self):
                lst = 'Uncategorised: 4\n'

                return lst

            def __test_file_maps__(self):
                return {
                    'Unowned but Necessary Wiki.md': 'Owner: Unowned but Necessary',
                    'Unknown Owner nor Necessity Wiki.md': 'Owner: Unknown Owner nor Necessity',
                    'Unowned Wiki 1.md': '',
                    'Unowned Wiki 2.md': 'This is a sample Wiki'
                }

if __name__ == '__main__':
    unittest.main()
