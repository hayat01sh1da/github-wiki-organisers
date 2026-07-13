# frozen_string_literal: true
# rbs_inline: enabled

require 'yaml'

module Spreen
  module Wiki
    # Resolves the runtime configuration for a wiki checkout. Every value is
    # looked up with the same precedence: explicit keyword argument, then the
    # `.spreen.yml` file under base_path (or config_path), then the
    # ORGANISATION_NAME environment variable (organisation only), then the
    # built-in defaults.
    class Configuration
      CONFIG_FILENAME = '.spreen.yml'
      EMPTY_HASH = {}.freeze #: Hash[String, untyped]
      DEFAULT_TEMPLATE_DIR = File.expand_path(File.join(__dir__.to_s, 'templates'))
      DEFAULT_EXCLUDED_DIRS = %w[spreen-wiki wikis-by-owner].freeze

      # Built-in labels: how the first line of a wiki page is parsed (regexp),
      # which namespace collects pages without a declaration (no_declaration),
      # which namespaces the count report covers (unknown_namespaces) and which
      # namespace the LLM export targets (llm_target_namespace). A config file
      # can override any of these, add languages or add group_by criteria.
      DEFAULT_LABELS = {
        'Owner' => {
          'regexp' => '[Oo]wner:\s?',
          'languages' => {
            'English' => {
              'no_declaration' => 'Unowned',
              'unknown_namespaces' => ['Unknown Owner nor Necessity', 'Unowned but Necessary', 'Unowned'],
              'llm_target_namespace' => 'Unknown Owner nor Necessity'
            },
            'Japanese' => {
              'no_declaration' => 'Owner記名なし',
              'unknown_namespaces' => [
                'Ownerチームが不明だが必要なページ群',
                'Ownerチーム・要or不要が不明なページ群',
                'Owner記名なし'
              ],
              'llm_target_namespace' => 'Ownerチーム・要or不要が不明なページ群'
            }
          }
        },
        'Category' => {
          'regexp' => '[Cc]ategory:\s?',
          'languages' => {
            'English' => {
              'no_declaration' => 'Uncategorised',
              'unknown_namespaces' => ['Uncategorised'],
              'llm_target_namespace' => 'Uncategorised'
            },
            'Japanese' => {
              'no_declaration' => 'Category記載なし',
              'unknown_namespaces' => ['Category記載なし'],
              'llm_target_namespace' => 'Category記載なし'
            }
          }
        }
      }.freeze

      attr_reader :organisation, :repository, :wiki_url, :owner_base_url, :excluded_dirs, :template_dir

      # @rbs!
      #   @organisation: String?
      #   @repository: String?
      #   @wiki_url: String?
      #   @owner_base_url: String?
      #   @excluded_dirs: Array[String]
      #   @template_dir: String
      #   @file: Hash[String, untyped]
      #   @labels: Hash[String, untyped]

      # @rbs base_path: String
      # @rbs config_path: String?
      # @rbs organisation: String?
      # @rbs repository: String?
      # @rbs wiki_url: String?
      # @rbs owner_base_url: String?
      # @rbs excluded_dirs: Array[String]?
      # @rbs template_dir: String?
      # @rbs return: void
      def initialize(base_path:, config_path: nil, organisation: nil, repository: nil, wiki_url: nil,
                     owner_base_url: nil, excluded_dirs: nil, template_dir: nil)
        @file           = load_file(config_path || File.join(base_path, CONFIG_FILENAME))
        @organisation   = resolve_organisation(organisation)
        @repository     = resolve(repository, 'repository')
        @wiki_url       = resolve_wiki_url(wiki_url)
        @owner_base_url = resolve_owner_base_url(owner_base_url)
        @excluded_dirs  = excluded_dirs || file.fetch('exclude', DEFAULT_EXCLUDED_DIRS)
        @template_dir   = template_dir || file.fetch('template_dir', DEFAULT_TEMPLATE_DIR)
        @labels         = deep_merge(DEFAULT_LABELS, file.fetch('labels', EMPTY_HASH))
      end

      # @rbs return: Array[String]
      def group_bys
        labels.keys
      end

      # @rbs group_by: String
      # @rbs return: Array[String]
      def languages(group_by)
        label_for(group_by).fetch('languages', EMPTY_HASH).keys
      end

      # @rbs group_by: String
      # @rbs return: Regexp
      def target_regexp(group_by)
        Regexp.new(label_for(group_by).fetch('regexp', ''))
      end

      # @rbs group_by: String
      # @rbs language: String
      # @rbs return: String
      def no_declaration(group_by, language)
        language_labels(group_by, language).fetch('no_declaration', '')
      end

      # @rbs group_by: String
      # @rbs language: String
      # @rbs return: Array[String]
      def unknown_namespaces(group_by, language)
        language_labels(group_by, language).fetch('unknown_namespaces', [])
      end

      # @rbs group_by: String
      # @rbs language: String
      # @rbs return: String
      def llm_target_namespace(group_by, language)
        language_labels(group_by, language).fetch('llm_target_namespace', '')
      end

      # @rbs group_by: String
      # @rbs language: String
      # @rbs return: String
      def path_to_template(group_by, language)
        File.join(template_dir, group_by.downcase, "#{language.downcase}.md")
      end

      private

      attr_reader :file, :labels

      # Treats empty strings the same as nil so that callers can pass values
      # straight from optional environment variables or CLI flags.
      # @rbs value: String?
      # @rbs return: String?
      def presence(value)
        value unless value.nil? || value.empty?
      end

      # @rbs explicit: String?
      # @rbs key: String
      # @rbs return: String?
      def resolve(explicit, key)
        presence(explicit) || presence(file[key])
      end

      # @rbs explicit: String?
      # @rbs return: String?
      def resolve_organisation(explicit)
        resolve(explicit, 'organisation') || presence(ENV.fetch('ORGANISATION_NAME', nil))
      end

      # @rbs explicit: String?
      # @rbs return: String?
      def resolve_wiki_url(explicit)
        resolve(explicit, 'wiki_url') || default_wiki_url
      end

      # @rbs explicit: String?
      # @rbs return: String?
      def resolve_owner_base_url(explicit)
        resolve(explicit, 'owner_base_url') || default_owner_base_url
      end

      # @rbs path: String
      # @rbs return: Hash[String, untyped]
      def load_file(path)
        return {} unless File.exist?(path)

        YAML.safe_load_file(path) || {}
      end

      # @rbs group_by: String
      # @rbs return: Hash[String, untyped]
      def label_for(group_by)
        labels.fetch(group_by, EMPTY_HASH)
      end

      # @rbs group_by: String
      # @rbs language: String
      # @rbs return: Hash[String, untyped]
      def language_labels(group_by, language)
        label_for(group_by).fetch('languages', EMPTY_HASH).fetch(language, EMPTY_HASH)
      end

      # @rbs return: String?
      def default_wiki_url
        "https://github.com/#{organisation}/#{repository}/wiki" if organisation && repository
      end

      # @rbs return: String?
      def default_owner_base_url
        "https://github.com/orgs/#{organisation}/teams/" if organisation
      end

      # @rbs base: Hash[String, untyped]
      # @rbs override: Hash[String, untyped]
      # @rbs return: Hash[String, untyped]
      def deep_merge(base, override)
        base.merge(override) do |_key, old_value, new_value|
          old_value.is_a?(Hash) && new_value.is_a?(Hash) ? deep_merge(old_value, new_value) : new_value
        end
      end
    end
  end
end
