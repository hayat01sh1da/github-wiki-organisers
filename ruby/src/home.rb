require_relative './application'

class Home < Application
  HOME_URL = "https://github.com/#{ENV.fetch('USERNAME', 'hayat01sh1da')}/github-wiki-organisers/wiki".freeze

  def initialize(base_path:, genre:)
    super(base_path:, genre:)
    @base_owner_url = "https://github.com/orgs/#{ENV.fetch('USERNAME', 'hayat01sh1da')}/teams/"
    @home_passage   = []
  end

  def run
    write_home_template
    update_home_passage
    File.write(path_to_home, home_passage.join.chomp)
    HOME_URL
  end

  private

  attr_reader :base_owner_url, :home_passage

  # @return [String]
  def write_home_template
    case genre
    when '-o', '--owner'
      home_passage << "## Wiki ページの運用ルール\n"
      home_passage << "\n"
      home_passage << "このページは Owner チームごとに Wiki をグルーピングして一覧化しています。\n"
      home_passage << "\n"
      home_passage << "Ownership をどのチームが持つのかが不明だと、責任の所在が不明瞭になり、保守性の悪化に伴うノイズの増加と検索性の悪化が発生します。  \n"
      home_passage << "治安維持のため、各ページの冒頭に `Owner: {オーナーチーム名}` を明記して頂きますようよろしくお願いします。\n"
    when '-c', '--category'
      home_passage << "## Wiki ページの運用ルール\n"
      home_passage << "\n"
      home_passage << "このページは Category ごとに Wiki をグルーピングして一覧化しています。\n"
      home_passage << "\n"
      home_passage << "Category が不明だと、保守性と検索性の悪化が発生します。  \n"
      home_passage << "治安維持のため、各ページの冒頭に `Category: {カテゴリー名}` を明記して頂きますようよろしくお願いします。\n"
    end

    home_passage << "\n"
    home_passage << "なお、Home・Sidebar は専用の定期実行ジョブで自動更新しますので編集は不要です。\n"
    home_passage << "\n"
  end

  # @return nil
  def update_home_passage
    owned_wiki_maps.each { |namespace, wikis|
      home_passage << "## [#{namespace}](#{base_owner_url + namespace.gsub(/\@/, '')})\n"
      home_passage << "\n"
      wikis.each { |wiki|
        home_passage << "- [[#{wiki.gsub(/\.md/, '')}]]\n"
      }
      home_passage << "\n"
    }

    plain_wiki_maps.each { |namespace, wikis|
      home_passage << "## #{namespace}\n"
      home_passage << "\n"
      wikis.each { |wiki|
        home_passage << "- [[#{wiki.gsub(/\.md/, '')}]]\n"
      }
      home_passage << "\n"
    }
  end
end
