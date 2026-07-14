# frozen_string_literal: true
# rbs_inline: enabled

require_relative 'application'

module SpreenWiki
  # Generates the wiki _Sidebar.md as a nested list of owners/categories and
  # their wiki pages.
  class Sidebar < Application
    # @rbs return: void
    def run
      update_wiki_list
      File.write(path_to_sidebar, wiki_list.join)
    end

    private

    # @rbs return: Array[String]
    def wiki_list
      @wiki_list ||= []
    end

    # @rbs return: void
    def update_wiki_list
      owned_wiki_maps.each { |namespace, wikis| append_section(namespace, wikis, owned: true) }
      plain_wiki_maps.each { |namespace, wikis| append_section(namespace, wikis, owned: false) }
    end

    # @rbs namespace: String
    # @rbs wikis: Array[String]
    # @rbs owned: bool
    # @rbs return: void
    def append_section(namespace, wikis, owned:)
      wiki_list << "#{section_heading(namespace, owned:)}\n"
      wikis.each { |wiki| wiki_list << "  - [[#{wiki.gsub('.md', '')}]]\n" }
    end

    # @rbs namespace: String
    # @rbs owned: bool
    # @rbs return: String
    def section_heading(namespace, owned:)
      owner_base_url = config.owner_base_url
      return "- #{namespace}" unless owned && owner_base_url

      "- [#{namespace}](#{owner_base_url + namespace.delete('@')})"
    end
  end
end
