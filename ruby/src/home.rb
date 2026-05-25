# frozen_string_literal: true
# rbs_inline: enabled

require_relative 'application'

# Generates the wiki Home page, optionally splitting per-owner content out into
# `wikis-by-owner/<owner>.md` when home_overflow is enabled.
class Home < Application
  HOME_URL = "https://github.com/#{ENV.fetch('ORGANISATION_NAME', 'hayat01sh1da')}/github-wiki-organisers/wiki".freeze

  # @rbs base_path: String
  # @rbs group_by: String
  # @rbs language: String
  # @rbs home_overflow: String
  # @rbs return: void
  def initialize(base_path: '', group_by: '', language: '', home_overflow: 'false')
    super
    @base_owner_url         = "https://github.com/orgs/#{ENV.fetch('ORGANISATION_NAME', 'hayat01sh1da')}/teams/"
    @path_to_wikis_by_owner = File.join(base_path, 'wikis-by-owner')
  end

  # @rbs return: String
  def run
    home_overflow ? write_concise_home_passage : write_home_passage
    HOME_URL
  end

  private

  attr_reader :base_owner_url, :path_to_wikis_by_owner

  # @rbs return: String
  def path_to_home_template
    File.join('..', 'home_template', group_by.downcase, "#{language.downcase}.md")
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

  # @rbs array: Array[untyped]
  # @rbs return: void
  def write_concise_home_passage(array = [])
    FileUtils.mkdir_p(path_to_wikis_by_owner)
    write_per_namespace_files(array)
    write_home_table_of_contents
  end

  # @rbs array: Array[untyped]
  # @rbs return: void
  def write_per_namespace_files(array)
    owned_wiki_maps.each { |namespace, wikis| write_overflow_block(namespace, wikis, array, owned: true) }
    plain_wiki_maps.each { |namespace, wikis| write_overflow_block(namespace, wikis, array.dup, owned: false) }
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
  # @rbs scratch: Array[String]
  # @rbs owned: bool
  # @rbs return: void
  def write_overflow_block(namespace, wikis, scratch, owned:)
    append_block(scratch, namespace, wikis, owned:)
    File.write(File.join(path_to_wikis_by_owner, "#{namespace}.md"), scratch.join.chomp)
  end

  # @rbs namespace: String
  # @rbs owned: bool
  # @rbs return: String
  def heading_for(namespace, owned:)
    owned ? "## [#{namespace}](#{base_owner_url + namespace.delete('@')})" : "## #{namespace}"
  end
end
