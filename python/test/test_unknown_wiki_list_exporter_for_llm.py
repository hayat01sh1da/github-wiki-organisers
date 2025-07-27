import sys
import os
import unittest
sys.path.append('./src')
sys.path.append('./test')
from unknown_wiki_list_exporter_for_llm import UnknownWikiListExporterForLLM
from test_application import TestApplication

class TestUnknownWikiListExporterForLLM(TestApplication):
    def setUp(self, genre = '-o', language = '-en'):
        super().setUp(genre = genre, language = language)
        UnknownWikiListExporterForLLM(base_path = self.base_path, genre = genre, language = language).run()
        path_to_unknown_wiki_list_for_llm = os.path.join(self.base_path, 'unknown_wiki_list_for_llm.txt')
        with open(path_to_unknown_wiki_list_for_llm) as f:
            self.unknown_wiki_list_for_llm = f.read()

class EnglishOwnershipTest(TestUnknownWikiListExporterForLLM):
    def test_run(self):
        self.assertEqual(self.unknown_wiki_list_for_llm, self.__unknown_wiki_list_for_llm__())

    # private

    def __unknown_wiki_list_for_llm__(self):
        return 'Unknown Owner nor Necessity Wiki.md\n'

class EnglishCategoryTest(TestUnknownWikiListExporterForLLM):
    def setUp(self):
        super().setUp(genre = '-c')

    def test_run(self):
        self.assertEqual(self.unknown_wiki_list_for_llm, ''.join(self.__unknown_wiki_list_for_llm__()))

    # private

    def __unknown_wiki_list_for_llm__(self):
        lst = [
            'Uncategorised Wiki 1.md\n',
            'Uncategorised Wiki 2.md\n'
        ]

        return lst

class JapaneseOwnershipTest(TestUnknownWikiListExporterForLLM):
    def setUp(self):
        super().setUp(genre = '-o', language = '-ja')

    def test_run(self):
        self.assertEqual(self.unknown_wiki_list_for_llm, self.__unknown_wiki_list_for_llm__())

    # private

    def __unknown_wiki_list_for_llm__(self):
        return 'Ownerチーム・要or不要が不明なページ.md\n'

class JapaneseCategoryTest(TestUnknownWikiListExporterForLLM):
    def setUp(self):
        super().setUp(genre = '-c', language = '-ja')

    def test_run(self):
        self.assertEqual(self.unknown_wiki_list_for_llm, ''.join(self.__unknown_wiki_list_for_llm__()))

    # private

    def __unknown_wiki_list_for_llm__(self):
        lst = [
            'Category記載なしページ1.md\n',
            'Category記載なしページ2.md\n'
        ]

        return lst

if __name__ == '__main__':
    unittest.main()
