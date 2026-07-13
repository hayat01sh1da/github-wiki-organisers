# frozen_string_literal: true
# rbs_inline: enabled

require_relative 'configuration'

module Spreen
  module Wiki
    # Base class for the wiki-organising commands. Loads the wiki tree under
    # base_path, groups it by Owner or Category in either English or Japanese,
    # and exposes the resulting maps to its subclasses. Grouping criteria,
    # languages and labels are resolved through Configuration and can be
    # extended via a `.spreen.yml` file.
    class Application
      class NotImplementedError < StandardError; end

      # @rbs base_path: String
      # @rbs group_by: String
      # @rbs language: String
      # @rbs home_overflow: (bool | String)
      # @rbs **options: untyped
      # @rbs return: untyped
      def self.run(base_path: Dir.pwd, group_by: 'Owner', language: 'English', home_overflow: 'false', **)
        instance = new(base_path:, group_by:, language:, home_overflow:, **)
        instance.validate!
        instance.run
      end

      # @rbs base_path: String
      # @rbs group_by: String
      # @rbs language: String
      # @rbs home_overflow: (bool | String)
      # @rbs config: Configuration?
      # @rbs **options: untyped
      # @rbs return: void
      def initialize(base_path: Dir.pwd, group_by: 'Owner', language: 'English', home_overflow: 'false',
                     config: nil, **)
        @base_path       = base_path
        @group_by        = group_by
        @language        = language
        @home_overflow   = parse_home_overflow(home_overflow)
        @config          = config || Configuration.new(base_path:, **)
        @path_to_home    = File.join(base_path, 'Home.md')
        @path_to_sidebar = File.join(base_path, '_Sidebar.md')
        @paths_to_wikis  = Dir[File.join(base_path, '**', '*.md')]
        @excluded_paths  = @config.excluded_dirs.flat_map { |dir| Dir[File.join(base_path, dir, '**', '*.md')] }
      end

      # @rbs return: void
      def validate!
        raise ArgumentError, "Invalid group_by: `#{group_by}`" unless config.group_bys.include?(group_by)
        raise ArgumentError, "Invalid language: `#{language}`" unless config.languages(group_by).include?(language)

        validate_home_overflow!
      end

      # @rbs return: untyped
      def run
        raise NotImplementedError, 'This method must be implemented in each subclass.'
      end

      private

      attr_reader :base_path,
                  :group_by,
                  :language,
                  :home_overflow,
                  :config,
                  :path_to_home,
                  :path_to_sidebar,
                  :paths_to_wikis,
                  :excluded_paths

      # @rbs return: void
      def validate_home_overflow!
        return if [true, false].include?(home_overflow)

        raise ArgumentError, "Invalid home_overflow: `#{home_overflow}` must be boolean"
      end

      # @rbs raw: (bool | String)
      # @rbs return: (bool | String)
      def parse_home_overflow(raw)
        case raw
        when 'true'  then true
        when 'false' then false
        else raw
        end
      end

      # @rbs return: Array[String]
      def target_paths
        @target_paths ||= paths_to_wikis.reject do |path_to_wiki|
          path_to_wiki == path_to_home ||
            path_to_wiki == path_to_sidebar ||
            excluded_paths.include?(path_to_wiki)
        end
      end

      # @rbs return: Regexp
      def target_regexp
        @target_regexp ||= config.target_regexp(group_by)
      end

      # @rbs return: String
      def no_declaration
        @no_declaration ||= config.no_declaration(group_by, language)
      end

      # @rbs return: Hash[String, Array[String]]
      def wiki_maps_with_namespace
        @wiki_maps_with_namespace ||= begin
          named      = Hash.new { |hash, namespace| hash[namespace] = [] } #: Hash[String, Array[String]]
          undeclared = Hash.new { |hash, namespace| hash[namespace] = [] } #: Hash[String, Array[String]]
          target_paths.each { |target_path| populate_namespace(target_path, named, undeclared) }
          named.sort.to_h.merge(undeclared)
        end
      end

      # @rbs target_path: String
      # @rbs named: Hash[String, Array[String]]
      # @rbs undeclared: Hash[String, Array[String]]
      # @rbs return: void
      def populate_namespace(target_path, named, undeclared)
        return unless File.exist?(target_path)

        namespace = namespace_for(target_path)
        bucket    = namespace == no_declaration ? undeclared : named
        bucket[namespace] << File.basename(target_path)
      end

      # @rbs target_path: String
      # @rbs return: String
      def namespace_for(target_path)
        declaration = File.open(target_path, &:gets)
        return no_declaration unless declaration&.start_with?(target_regexp)

        declaration.chomp.gsub(target_regexp, '')
      end

      # @rbs return: Hash[String, Array[String]]
      def owned_wiki_maps
        @owned_wiki_maps ||= wiki_maps_with_namespace.select { |namespace, _| namespace.include?('@') }
      end

      # @rbs return: Hash[String, Array[String]]
      def plain_wiki_maps
        @plain_wiki_maps ||= wiki_maps_with_namespace.reject { |namespace, _| namespace.include?('@') }
      end
    end
  end
end
