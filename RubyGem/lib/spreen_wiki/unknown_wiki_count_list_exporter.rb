# frozen_string_literal: true
# rbs_inline: enabled

require_relative 'application'

module SpreenWiki
  # Writes a sorted text report of how many wikis exist under each of the
  # configured "unknown owner/category" namespaces.
  class UnknownWikiCountListExporter < Application
    DEFAULT_OUTPUT_FILENAME = 'unknown_wiki_count_list_by_namespace.txt'

    # @rbs base_path: String
    # @rbs group_by: String
    # @rbs language: String
    # @rbs home_overflow: (bool | String)
    # @rbs output: String?
    # @rbs **options: untyped
    # @rbs return: void
    def initialize(base_path: Dir.pwd, group_by: 'Owner', language: 'English', home_overflow: 'false',
                   output: nil, **)
      super(base_path:, group_by:, language:, home_overflow:, **)
      @path_to_export = resolve_output_path(output || DEFAULT_OUTPUT_FILENAME)
    end

    # @rbs return: [Array[String], String]
    def run
      File.open(path_to_export, 'wb') { |f| f.puts(count_list_by_namespace) }
      [count_list_by_namespace, path_to_export]
    end

    private

    attr_reader :path_to_export #: String

    # @rbs filename: String
    # @rbs return: String
    def resolve_output_path(filename)
      File.absolute_path?(filename) ? filename : File.join(base_path, filename)
    end

    # @rbs return: Array[String]
    def namespace_list
      config.unknown_namespaces(group_by, language)
    end

    # @rbs return: Array[String]
    def missing_count_list_by_namespace
      (namespace_list - plain_wiki_maps.keys).map { |namespace| "#{namespace}: 0" }
    end

    # @rbs return: Array[String]
    def count_list_by_namespace
      @count_list_by_namespace ||= begin
        counts = plain_wiki_maps.slice(*namespace_list).map { |namespace, wikis| "#{namespace}: #{wikis.length}" }
        (counts + missing_count_list_by_namespace).sort
      end
    end
  end
end
