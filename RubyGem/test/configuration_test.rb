# frozen_string_literal: true
# rbs_inline: enabled

require_relative 'application_test'
require_relative '../lib/spreen/wiki/configuration'
require_relative '../lib/spreen/wiki/home'
require_relative '../lib/spreen/wiki/unknown_wiki_count_list_exporter'

class ConfigurationTest < ApplicationTest
  CUSTOM_CONFIG = <<~YAML
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
  YAML

  def test_default_group_bys_and_languages
    configuration = Spreen::Wiki::Configuration.new(base_path:)

    assert_equal(%w[Owner Category], configuration.group_bys)
    assert_equal(%w[English Japanese], configuration.languages('Owner'))
  end

  def test_default_labels
    configuration = Spreen::Wiki::Configuration.new(base_path:)

    assert_equal('Unowned', configuration.no_declaration('Owner', 'English'))
    assert_equal('Category記載なし', configuration.no_declaration('Category', 'Japanese'))
    assert_equal('Unknown Owner nor Necessity', configuration.llm_target_namespace('Owner', 'English'))
  end

  def test_default_unknown_namespaces
    configuration = Spreen::Wiki::Configuration.new(base_path:)

    assert_equal(['Unknown Owner nor Necessity', 'Unowned but Necessary', 'Unowned'],
                 configuration.unknown_namespaces('Owner', 'English'))
  end

  def test_default_excluded_dirs
    configuration = Spreen::Wiki::Configuration.new(base_path:)

    assert_equal(%w[github-wiki-organisers wikis-by-owner], configuration.excluded_dirs)
  end

  def test_urls_are_absent_without_an_organisation
    configuration = Spreen::Wiki::Configuration.new(base_path:)

    assert_nil(configuration.wiki_url)
    assert_nil(configuration.owner_base_url)
  end

  def test_urls_derived_from_organisation_and_repository
    configuration = Spreen::Wiki::Configuration.new(base_path:, organisation: 'test-org',
                                                    repository: 'test-repo')

    assert_equal('https://github.com/test-org/test-repo/wiki', configuration.wiki_url)
    assert_equal('https://github.com/orgs/test-org/teams/', configuration.owner_base_url)
  end

  def test_explicit_urls_win_over_derived_ones
    configuration = Spreen::Wiki::Configuration.new(base_path:, organisation: 'test-org',
                                                    repository: 'test-repo',
                                                    wiki_url: 'https://example.com/wiki',
                                                    owner_base_url: 'https://example.com/teams/')

    assert_equal('https://example.com/wiki', configuration.wiki_url)
    assert_equal('https://example.com/teams/', configuration.owner_base_url)
  end

  def test_empty_values_are_treated_as_absent
    configuration = Spreen::Wiki::Configuration.new(base_path:, organisation: '', repository: '')

    assert_nil(configuration.organisation)
    assert_nil(configuration.wiki_url)
  end

  def test_default_template_dir_ships_with_the_library
    configuration = Spreen::Wiki::Configuration.new(base_path:)

    assert_path_exists(configuration.path_to_template('Owner', 'English'))
    assert_path_exists(configuration.path_to_template('Category', 'Japanese'))
  end

  def test_config_file_overrides_values
    write_config_file
    configuration = Spreen::Wiki::Configuration.new(base_path:)

    assert_equal('config-org', configuration.organisation)
    assert_equal('https://github.com/config-org/config-repo/wiki', configuration.wiki_url)
    assert_equal(%w[archived], configuration.excluded_dirs)
  end

  def test_config_file_extends_languages
    write_config_file
    configuration = Spreen::Wiki::Configuration.new(base_path:)

    assert_equal(%w[English Japanese French], configuration.languages('Owner'))
    assert_equal('Sans propriétaire', configuration.no_declaration('Owner', 'French'))
    assert_equal(%w[English Japanese], configuration.languages('Category'))
  end

  def test_explicit_options_win_over_the_config_file
    write_config_file
    configuration = Spreen::Wiki::Configuration.new(base_path:, organisation: 'cli-org')

    assert_equal('cli-org', configuration.organisation)
  end

  def test_config_file_language_passes_validation
    write_config_file
    File.write(File.join(base_path, 'Page sans propriétaire.md'), '')
    application = Spreen::Wiki::Application.new(base_path:, group_by: 'Owner', language: 'French',
                                                home_overflow: 'false')

    assert_nil(application.validate!)
  end

  def test_exporter_honours_custom_output_filename
    _, path_to_export = Spreen::Wiki::UnknownWikiCountListExporter.run(base_path:, group_by:, language:,
                                                                       output: 'custom_report.txt')

    assert_equal(File.join(base_path, 'custom_report.txt'), path_to_export)
    assert_path_exists(path_to_export)
  end

  private

  # @rbs return: void
  def write_config_file
    File.write(File.join(base_path, Spreen::Wiki::Configuration::CONFIG_FILENAME), CUSTOM_CONFIG)
  end
end
