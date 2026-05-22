import os
import sys

from invoke import Context, task

_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_ROOT, 'src'))

from home import Home  # noqa: E402
from sidebar import Sidebar  # noqa: E402
from unknown_wiki_count_list_exporter import (  # noqa: E402
    UnknownWikiCountListExporter,
)
from unknown_wiki_list_exporter_for_llm import (  # noqa: E402
    UnknownWikiListExporterForLLM,
)


@task
def update_wiki_list_on_home_and_sidebar(c: Context) -> None:
    """Update Wiki List on Home and Sidebar"""
    print('Provide the group_by(Owner or Category)')
    group_by = input().strip()

    print('Provide the language(English or Japanese)')
    language = input().strip()

    print('Provide the home_overflow(true or false)')
    home_overflow = input().strip()

    params: dict[str, str] = {}
    for key, value in {
        'group_by': group_by,
        'language': language,
        'home_overflow': home_overflow,
    }.items():
        if value:
            params[key] = value

    print('-------------------- Categorising the Entire '
          'github-wiki-organisers Wiki Pages... --------------------')
    print()
    print('-------------------- Organising Home... --------------------')
    home_url = Home(**params).run()
    print(f"Check out an Up-to-date Wiki List on Home at '{home_url}' !!")
    print('-------------------- Done Organising Home 🎉 '
          '--------------------')
    print()
    print('-------------------- Organising Sidebar... '
          '--------------------')
    Sidebar(**params).run()
    print(f"Check out an Up-to-date Wiki List on Sidebar at "
          f"'{home_url}' !!")
    print('-------------------- Done Organising Sidebar 🎉 '
          '--------------------')
    print()
    print('-------------------- Done Categorising the Entire '
          'github-wiki-organisers Wiki Pages 🎉 --------------------')


@task
def export_unknown_wiki_count_list_by_namespace(c: Context) -> None:
    """Export Unknown Wiki Count List by Namespace"""
    print('Provide the group_by(Owner or Category)')
    group_by = input().strip()

    print('Provide the language(English or Japanese)')
    language = input().strip()

    params: dict[str, str] = {}
    for key, value in {'group_by': group_by, 'language': language}.items():
        if value:
            params[key] = value

    print('-------------------- Exporting Unknown Wiki Count List... '
          '--------------------')
    count_list_by_namespace, path_to_export = \
        UnknownWikiCountListExporter(**params).run()
    print()
    print('Here is the result:')
    print()
    print('---------------------------------------')
    print(count_list_by_namespace.rstrip())
    print('---------------------------------------')
    print()
    print(f"Check it out result on '{path_to_export}' !!")
    print()
    print('-------------------- Done Exporting Unknown Wiki Count List '
          '🎉 --------------------')


@task
def export_unknown_wiki_list_for_llm(c: Context) -> None:
    """Export Unknown Wiki List for LLM"""
    print('Provide the group_by(Owner or Category)')
    group_by = input().strip()

    print('Provide the language(English or Japanese)')
    language = input().strip()

    params: dict[str, str] = {}
    for key, value in {'group_by': group_by, 'language': language}.items():
        if value:
            params[key] = value

    print('-------------------- Exporting Unknown Wiki List... '
          '--------------------')
    path_to_export = UnknownWikiListExporterForLLM(**params).run()
    print()
    print(f"Check it out result on '{path_to_export}' !!")
    print()
    print('-------------------- Done Exporting Unknown Wiki List 🎉 '
          '--------------------')


@task(default=True)
def test(c: Context) -> None:
    """Run all tests"""
    c.run('pytest .')
