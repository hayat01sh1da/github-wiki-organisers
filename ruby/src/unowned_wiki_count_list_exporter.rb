require_relative './application'

class UnknownWikiCountListExporter < Application
  NAMESPACE_LIST = [
    'Ownerチームが不明だが必要なページ群',
    'Ownerチーム・要or不要が不明なページ群',
    'Owner記名なし'
  ].freeze

  def initialize(base_path)
    super(base_path)
    @path_to_export = File.join(base_path, 'unowned_wiki_count_list_by_namespace.txt')
  end

  def run
    File.open(path_to_export, 'wb') { |f| f.puts(count_list_by_namespace) }
    [count_list_by_namespace, path_to_export]
  end

  private

  attr_reader :path_to_export

  # @return [Array<String>]
  def missing_count_list_by_namespace
    (NAMESPACE_LIST - unowned_wiki_maps.keys).map { |namespace| "#{namespace}: 0件" }
  end

  # @return [Array<String>]
  def count_list_by_namespace
    @count_list_by_namespace ||= unowned_wiki_maps.map { |namespace, wikis|
      "#{namespace}: #{wikis.length}件"
    }.then {
      it + missing_count_list_by_namespace
    }.sort
  end
end
