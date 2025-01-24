require_relative './application'

class Home < Application
  HOME_URL = 'https://github.com/hayat01sh1da/github-wiki-organisers/wiki'.freeze

  def initialize(base_path)
    super(base_path)
    @base_owner_url = 'https://github.com/orgs/quipper/teams/'
    @home_passage   = []
  end

  def run
    write_home_template
    update_home_passage
    IO.write(path_to_home, home_passage.join.chomp)
    HOME_URL
  end

  private

  attr_reader :base_owner_url, :home_passage

  # @return [Hash<String => Array<String>>]
  def owner_and_wiki_maps_with_ownership
    @owner_and_wiki_maps_with_ownership ||= owner_and_wiki_maps.select { |owner, _| owner.include?('@') }
  end

  # @return [Hash<String => Array<String>>]
  def owner_and_wiki_maps_without_ownership
    @owner_and_wiki_maps_without_ownership ||= owner_and_wiki_maps.reject { |owner, _| owner.include?('@') }
  end

  # @return [String]
  def write_home_template
    home_passage << "このページは Owner チームごとに Wiki をグルーピングして一覧化しています。\n\n"
    home_passage << "## Wiki ページの運用ルール\n\n"
    home_passage << "Ownership をどのチームが持つのかが不明だと、責任の所在が不明瞭になり、保守性の悪化に伴うノイズの増加と検索性の悪化が発生します。  \n"
    home_passage << "治安維持のため、各ページの冒頭に `Owner: {オーナーチーム名}` を明記して頂きますようよろしくお願いします。  \n"
    home_passage << "なお、Home・Sidebar は専用のスクリプトで自動更新しますので編集は不要です。\n\n"
  end

  # @return nil
  def update_home_passage
    owner_and_wiki_maps_with_ownership.each { |owner, wikis|
      home_passage << "## [#{owner}](#{base_owner_url + owner.gsub(/\@/, '')})\n\n"
      wikis.each { |wiki|
        home_passage << "- [[#{wiki.gsub(/\.md/, '')}]]\n"
      }
      home_passage << "\n"
    }

    owner_and_wiki_maps_without_ownership.each { |namespace, wikis|
      home_passage << "## #{namespace}\n\n"
      wikis.each { |wiki|
        home_passage << "- [[#{wiki.gsub(/\.md/, '')}]]\n"
      }
      home_passage << "\n"
    }
  end
end
