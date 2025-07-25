require_relative './application'

class UnknownWikiCountListExporter < Application
  def initialize(base_path:, genre:, language:)
    super(base_path:, genre:, language:)
    @path_to_export = File.join(base_path, 'unknown_wiki_count_list_by_namespace.txt')
  end

  def run
    File.open(path_to_export, 'wb') { |f| f.puts(count_list_by_namespace) }
    [count_list_by_namespace, path_to_export]
  end

  private

  attr_reader :path_to_export

  # @return [Array<String>]
  def namespace_list
    case language
    when 'en'
      case genre
      when '-o', '--owner'
        [
          'Unknown Owner nor Necessity',
          'Unowned but Necessary',
          'Unowned'
        ]
      when '-c', '--category'
        [
          'Uncategorised'
        ]
      end
    when 'ja'
      case genre
      when '-o', '--owner'
        [
          'Ownerチームが不明だが必要なページ群',
          'Ownerチーム・要or不要が不明なページ群',
          'Owner記名なし'
        ]
      when '-c', '--category'
        [
          'Category記載なし'
        ]
      end
    end
  end

  # @return [Array<String>]
  def missing_count_list_by_namespace
    (namespace_list - plain_wiki_maps.keys).map { |namespace| "#{namespace}: 0" }
  end

  # @return [Array<String>]
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
