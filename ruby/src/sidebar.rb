# frozen_string_literal: true
# rbs_inline: enabled

require_relative 'application'

# Generates the wiki _Sidebar.md as a nested list of owners/categories and
# their wiki pages.
class Sidebar < Application
  # @rbs base_path: String
  # @rbs group_by: String
  # @rbs language: String
  # @rbs home_overflow: String
  # @rbs array: Array[untyped]
  # @rbs return: void
  def initialize(base_path: '', group_by: '', language: '', home_overflow: 'false', array: [])
    super(base_path:, group_by:, language:, home_overflow:)
    @base_owner_url = "https://github.com/orgs/#{ENV.fetch('ORGANISATION_NAME', 'hayat01sh1da')}/teams/"
    @wiki_list      = array
  end

  # @rbs return: void
  def run
    update_wiki_list
    File.write(path_to_sidebar, wiki_list.join)
  end

  private

  attr_reader :base_owner_url, :wiki_list

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
    owned ? "- [#{namespace}](#{base_owner_url + namespace.delete('@')})" : "- #{namespace}"
  end
end
