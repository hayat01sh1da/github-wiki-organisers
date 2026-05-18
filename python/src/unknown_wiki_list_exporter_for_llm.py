from application import Application
import sys
import os
sys.path.append('./src')


class UnknownWikiListExporterForLLM(Application):
    def __init__(
            self,
            base_path: str = os.path.join(
                '..',
                '..'),
            group_by: str = 'Owner',
            language: str = 'English',
            home_overflow: str | bool = False) -> None:
        super().__init__(base_path, group_by, language, home_overflow)
        self.path_to_export: str = os.path.join(
            self.base_path, 'unknown_wiki_list_for_llm.txt')
        self.unknown_wiki_list_for_llm: str = ''.join(
            sorted(self.__unknown_wiki_list_for_llm__()))

    def run(self) -> str:
        with open(self.path_to_export, 'w') as f:
            f.write(self.unknown_wiki_list_for_llm.rstrip() + '\n')

        return self.path_to_export

    # private

    # @return [str]
    def __target_namespace__(self) -> str:
        match self.group_by:
            case 'Owner':
                match self.language:
                    case 'English':
                        return 'Unknown Owner nor Necessity'
                    case 'Japanese':
                        return 'Ownerチーム・要or不要が不明なページ群'
                    case _:
                        raise ValueError(
                            f'Invalid language: `{self.language}`')
            case 'Category':
                match self.language:
                    case 'English':
                        return 'Uncategorised'
                    case 'Japanese':
                        return 'Category記載なし'
                    case _:
                        raise ValueError(
                            f'Invalid language: `{self.language}`')
            case _:
                raise ValueError(f'Invalid group_by: `{self.group_by}`')

    # @return [list<str>]
    def __unknown_wiki_list_for_llm__(self) -> list[str]:
        unknown_wiki_list_for_llm: list[str] = []

        for namespace, wikis in self.plain_wiki_maps.items():
            if namespace == self.__target_namespace__():
                for wiki in wikis:
                    unknown_wiki_list_for_llm.append(f'{wiki}\n')

        return unknown_wiki_list_for_llm
