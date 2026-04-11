# rbs_inline: enabled

require_relative './application'

class UnknownWikiCountListExporter < Application
  # @rbs base_path: String
  # @rbs group_by: String
  # @rbs language: String
  # @rbs home_overflow: bool
  # @rbs return: void
  def initialize(base_path:, group_by:, language:, home_overflow: false)
    super(base_path:, group_by:, language:, home_overflow:)
    @path_to_export = File.join(base_path, 'unknown_wiki_count_list_by_namespace.txt')
  end

  # @rbs return: Array[untyped]
  def run
    File.open(path_to_export, 'wb') { |f| f.puts(count_list_by_namespace) }
    [count_list_by_namespace, path_to_export]
  end

  private

  attr_reader :path_to_export

  # @rbs return: Array[String]
  def namespace_list
    case group_by
    when 'Owner'
      case language
      when 'English'
        [
          'Unknown Owner nor Necessity',
          'Unowned but Necessary',
          'Unowned'
        ]
      when 'Japanese'
        [
          'Ownerチームが不明だが必要なページ群',
          'Ownerチーム・要or不要が不明なページ群',
          'Owner記名なし'
        ]
      end
    when 'Category'
      case language
      when 'English'
        [
          'Uncategorised'
        ]
      when 'Japanese'
        [
          'Category記載なし'
        ]
      end
    end
  end

  # @rbs return: Array[String]
  def missing_count_list_by_namespace
    (namespace_list - plain_wiki_maps.keys).map { |namespace| "#{namespace}: 0" }
  end

  # @rbs return: Array[String]
  def count_list_by_namespace
    @count_list_by_namespace ||= plain_wiki_maps.select { |namespace, _|
      namespace_list.include?(namespace)
    }.map { |namespace, wikis|
      "#{namespace}: #{wikis.length}"
    }.then {
      it + missing_count_list_by_namespace
    }.sort
  end
end
