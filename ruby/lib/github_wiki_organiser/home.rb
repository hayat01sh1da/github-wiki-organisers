# frozen_string_literal: true
# rbs_inline: enabled

require 'fileutils'
require_relative 'application'

module GithubWikiOrganiser
  # Generates the wiki Home page, optionally splitting per-owner content out
  # into `wikis-by-owner/<owner>.md` when home_overflow is enabled. Returns
  # the configured wiki URL (if any) so callers can point at the result.
  class Home < Application
    # @rbs return: String?
    def run
      home_overflow ? write_concise_home_passage : write_home_passage
      config.wiki_url
    end

    private

    # @rbs return: String
    def path_to_wikis_by_owner
      @path_to_wikis_by_owner ||= File.join(base_path, 'wikis-by-owner')
    end

    # @rbs return: String
    def path_to_home_template
      path = config.path_to_template(group_by, language)
      unless File.exist?(path)
        raise ArgumentError, "Missing Home template: `#{path}`. Ship one there or configure template_dir."
      end

      path
    end

    # @rbs return: Array[String]
    def home_passage
      @home_passage ||= File.readlines(path_to_home_template).append("\n")
    end

    # @rbs return: void
    def write_home_passage
      FileUtils.rm_rf(path_to_wikis_by_owner)
      owned_wiki_maps.each { |namespace, wikis| append_block(home_passage, namespace, wikis, owned: true) }
      plain_wiki_maps.each { |namespace, wikis| append_block(home_passage, namespace, wikis, owned: false) }
      File.write(path_to_home, home_passage.join.chomp)
    end

    # @rbs return: void
    def write_concise_home_passage
      FileUtils.mkdir_p(path_to_wikis_by_owner)
      write_per_namespace_files
      write_home_table_of_contents
    end

    # @rbs return: void
    def write_per_namespace_files
      owned_wiki_maps.each { |namespace, wikis| write_overflow_block(namespace, wikis, owned: true) }
      plain_wiki_maps.each { |namespace, wikis| write_overflow_block(namespace, wikis, owned: false) }
    end

    # @rbs return: void
    def write_home_table_of_contents
      (owned_wiki_maps.keys + plain_wiki_maps.keys).each { |namespace| home_passage << "- [[#{namespace}]]\n" }
      home_passage << "\n"
      File.write(path_to_home, home_passage.join.chomp)
    end

    # @rbs passage: Array[String]
    # @rbs namespace: String
    # @rbs wikis: Array[String]
    # @rbs owned: bool
    # @rbs return: void
    def append_block(passage, namespace, wikis, owned:)
      passage << "#{heading_for(namespace, owned:)}\n"
      passage << "\n"
      wikis.each { |wiki| passage << "- [[#{wiki.gsub('.md', '')}]]\n" }
      passage << "\n"
    end

    # @rbs namespace: String
    # @rbs wikis: Array[String]
    # @rbs owned: bool
    # @rbs return: void
    def write_overflow_block(namespace, wikis, owned:)
      scratch = [] #: Array[String]
      append_block(scratch, namespace, wikis, owned:)
      File.write(File.join(path_to_wikis_by_owner, "#{namespace}.md"), scratch.join.chomp)
    end

    # @rbs namespace: String
    # @rbs owned: bool
    # @rbs return: String
    def heading_for(namespace, owned:)
      owner_base_url = config.owner_base_url
      return "## #{namespace}" unless owned && owner_base_url

      "## [#{namespace}](#{owner_base_url + namespace.delete('@')})"
    end
  end
end
