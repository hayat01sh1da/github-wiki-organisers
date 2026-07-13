# frozen_string_literal: true
# rbs_inline: enabled

require_relative 'application'

module Spreen
  module Wiki
    # Writes a flat list of the wikis under the configured "unknown
    # owner/category" namespace in a form suitable for feeding to an LLM.
    class UnknownWikiListExporterForLLM < Application
      DEFAULT_OUTPUT_FILENAME = 'unknown_wiki_list_for_llm.txt'

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

      # @rbs return: String
      def run
        File.open(path_to_export, 'wb') { |f| f.puts(unknown_wiki_list_for_llm) }
        path_to_export
      end

      private

      attr_reader :path_to_export #: String

      # @rbs filename: String
      # @rbs return: String
      def resolve_output_path(filename)
        File.absolute_path?(filename) ? filename : File.join(base_path, filename)
      end

      # @rbs return: String
      def target_namespace
        config.llm_target_namespace(group_by, language)
      end

      # @rbs return: Array[String]
      def unknown_wiki_list_for_llm
        @unknown_wiki_list_for_llm ||= plain_wiki_maps.slice(target_namespace).values.flatten
      end
    end
  end
end
