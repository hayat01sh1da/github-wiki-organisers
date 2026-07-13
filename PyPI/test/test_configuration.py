import os
from collections.abc import Callable

from spreen_wiki.application import Application
from spreen_wiki.configuration import (
    CONFIG_FILENAME,
    Configuration,
)
from spreen_wiki.unknown_wiki_count_list_exporter import (
    UnknownWikiCountListExporter,
)

_CUSTOM_CONFIG = """\
organisation: config-org
repository: config-repo
exclude:
  - archived
labels:
  Owner:
    languages:
      French:
        no_declaration: Sans propriétaire
        unknown_namespaces:
          - Sans propriétaire
        llm_target_namespace: Sans propriétaire
"""


def _write_config_file(base_path: str) -> None:
    path = os.path.join(base_path, CONFIG_FILENAME)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(_CUSTOM_CONFIG)


def test_default_group_bys_and_languages(
        wiki_workspace: Callable[..., str]) -> None:
    configuration = Configuration(base_path=wiki_workspace())
    assert configuration.group_bys() == ['Owner', 'Category']
    assert configuration.languages('Owner') == ['English', 'Japanese']


def test_default_labels(wiki_workspace: Callable[..., str]) -> None:
    configuration = Configuration(base_path=wiki_workspace())
    assert configuration.no_declaration('Owner', 'English') == 'Unowned'
    assert configuration.no_declaration(
        'Category', 'Japanese') == 'Category記載なし'
    assert configuration.llm_target_namespace(
        'Owner', 'English') == 'Unknown Owner nor Necessity'


def test_default_unknown_namespaces(
        wiki_workspace: Callable[..., str]) -> None:
    configuration = Configuration(base_path=wiki_workspace())
    assert configuration.unknown_namespaces('Owner', 'English') == [
        'Unknown Owner nor Necessity',
        'Unowned but Necessary',
        'Unowned',
    ]


def test_default_excluded_dirs(wiki_workspace: Callable[..., str]) -> None:
    configuration = Configuration(base_path=wiki_workspace())
    assert configuration.excluded_dirs == [
        'spreen-wiki', 'wikis-by-owner']


def test_urls_are_absent_without_an_organisation(
        wiki_workspace: Callable[..., str]) -> None:
    configuration = Configuration(base_path=wiki_workspace())
    assert configuration.wiki_url is None
    assert configuration.owner_base_url is None


def test_urls_derived_from_organisation_and_repository(
        wiki_workspace: Callable[..., str]) -> None:
    configuration = Configuration(
        base_path=wiki_workspace(), organisation='test-org',
        repository='test-repo')
    assert configuration.wiki_url == \
        'https://github.com/test-org/test-repo/wiki'
    assert configuration.owner_base_url == \
        'https://github.com/orgs/test-org/teams/'


def test_explicit_urls_win_over_derived_ones(
        wiki_workspace: Callable[..., str]) -> None:
    configuration = Configuration(
        base_path=wiki_workspace(), organisation='test-org',
        repository='test-repo', wiki_url='https://example.com/wiki',
        owner_base_url='https://example.com/teams/')
    assert configuration.wiki_url == 'https://example.com/wiki'
    assert configuration.owner_base_url == 'https://example.com/teams/'


def test_empty_values_are_treated_as_absent(
        wiki_workspace: Callable[..., str]) -> None:
    configuration = Configuration(
        base_path=wiki_workspace(), organisation='', repository='')
    assert configuration.organisation is None
    assert configuration.wiki_url is None


def test_default_template_dir_ships_with_the_package(
        wiki_workspace: Callable[..., str]) -> None:
    configuration = Configuration(base_path=wiki_workspace())
    assert os.path.isfile(
        configuration.path_to_template('Owner', 'English'))
    assert os.path.isfile(
        configuration.path_to_template('Category', 'Japanese'))


def test_config_file_overrides_values(
        wiki_workspace: Callable[..., str]) -> None:
    base_path = wiki_workspace()
    _write_config_file(base_path)
    configuration = Configuration(base_path=base_path)
    assert configuration.organisation == 'config-org'
    assert configuration.wiki_url == \
        'https://github.com/config-org/config-repo/wiki'
    assert configuration.excluded_dirs == ['archived']


def test_config_file_extends_languages(
        wiki_workspace: Callable[..., str]) -> None:
    base_path = wiki_workspace()
    _write_config_file(base_path)
    configuration = Configuration(base_path=base_path)
    assert configuration.languages('Owner') == [
        'English', 'Japanese', 'French']
    assert configuration.no_declaration(
        'Owner', 'French') == 'Sans propriétaire'
    assert configuration.languages('Category') == ['English', 'Japanese']


def test_explicit_options_win_over_the_config_file(
        wiki_workspace: Callable[..., str]) -> None:
    base_path = wiki_workspace()
    _write_config_file(base_path)
    configuration = Configuration(
        base_path=base_path, organisation='cli-org')
    assert configuration.organisation == 'cli-org'


def test_config_file_language_passes_validation(
        wiki_workspace: Callable[..., str]) -> None:
    base_path = wiki_workspace()
    _write_config_file(base_path)
    application = Application(
        base_path=base_path, group_by='Owner', language='French',
        home_overflow='false')
    application.validate()


def test_exporter_honours_custom_output_filename(
        wiki_workspace: Callable[..., str]) -> None:
    base_path = wiki_workspace()
    _, path_to_export = UnknownWikiCountListExporter.run(
        base_path=base_path, output='custom_report.txt')
    assert path_to_export == os.path.join(base_path, 'custom_report.txt')
    assert os.path.isfile(path_to_export)
