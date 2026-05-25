# frozen_string_literal: true
# rbs_inline: enabled

require_relative 'application'

# Writes a flat list of the wikis under the "unknown owner/category" namespace
# in a form suitable for feeding to an LLM.
class UnknownWikiListExporterForLLM < Application
  TARGET_NAMESPACE = {
    %w[Owner English] => 'Unknown Owner nor Necessity',
    %w[Owner Japanese] => 'Ownerチーム・要or不要が不明なページ群',
    %w[Category English] => 'Uncategorised',
    %w[Category Japanese] => 'Category記載なし'
  }.freeze

  # @rbs base_path: String
  # @rbs group_by: String
  # @rbs language: String
  # @rbs home_overflow: String
  # @rbs return: void
  def initialize(base_path: '', group_by: '', language: '', home_overflow: 'false')
    super
    @path_to_export = File.join(base_path, 'unknown_wiki_list_for_llm.txt')
  end

  # @rbs return: String
  def run
    File.open(path_to_export, 'wb') { |f| f.puts(unknown_wiki_list_for_llm) }
    path_to_export
  end

  private

  attr_reader :path_to_export

  # @rbs return: String
  def target_namespace
    TARGET_NAMESPACE.fetch([group_by, language], '')
  end

  # @rbs return: Array[String]
  def unknown_wiki_list_for_llm
    @unknown_wiki_list_for_llm ||= plain_wiki_maps.slice(target_namespace).values.flatten
  end
end
