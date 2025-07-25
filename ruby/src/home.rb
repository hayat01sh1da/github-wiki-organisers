require_relative './application'

class Home < Application
  HOME_URL = "https://github.com/#{ENV.fetch('USERNAME', 'hayat01sh1da')}/github-wiki-organisers/wiki".freeze

  def initialize(base_path:, genre:, language:)
    super(base_path:, genre:, language:)
    @base_owner_url = "https://github.com/orgs/#{ENV.fetch('USERNAME', 'hayat01sh1da')}/teams/"
  end

  def run
    update_home_passage
    File.write(path_to_home, home_passage.join.chomp)
    HOME_URL
  end

  private

  attr_reader :base_owner_url

  # @return [String]
  def template_genre
    case genre
    when '-o', '--owner'
      'owner'
    when '-c', '--category'
      'category'
    end
  end

  # @return [String]
  def path_to_home_template
    File.join('..', 'home_template', template_genre, "#{language.gsub(/^\-/, '')}.md")
  end

  # @return [Array<String>]
  def home_passage
    @home_passage ||= File.readlines(path_to_home_template).append("\n")
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
