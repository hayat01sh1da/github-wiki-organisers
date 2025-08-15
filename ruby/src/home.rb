require_relative './application'

class Home < Application
  HOME_URL = "https://github.com/#{ENV.fetch('ORGANISATION_NAME', 'hayat01sh1da')}/github-wiki-organisers/wiki".freeze

  def initialize(base_path:, group_by:, language:, home_overflow:)
    super(base_path:, group_by:, language:, home_overflow:)
    @base_owner_url = "https://github.com/orgs/#{ENV.fetch('ORGANISATION_NAME', 'hayat01sh1da')}/teams/"
  end

  def run
    write_home_passage
    HOME_URL
  end

  private

  attr_reader :base_owner_url

  # @return [String]
  def path_to_home_template
    File.join('..', 'home_template', group_by.downcase, "#{language.downcase}.md")
  end

  # @return [Array<String>]
  def home_passage
    @home_passage ||= File.readlines(path_to_home_template).append("\n")
  end

  # @return nil
  def write_home_passage
    if group_by == 'Owner' && home_overflow
      path_to_wikis_by_owners = File.join(base_path, 'wikis_by_owners')
      FileUtils.mkdir_p(path_to_wikis_by_owners) unless Dir.exist?(path_to_wikis_by_owners)

      owned_wiki_maps.each { |namespace, wikis|
        home_passage  = []
        home_passage << "## [#{namespace}](#{base_owner_url + namespace.gsub(/\@/, '')})\n"
        home_passage << "\n"
        wikis.each { |wiki|
          home_passage << "- [[#{wiki.gsub(/\.md/, '')}]]\n"
        }
        home_passage << "\n"

        File.write(File.join(path_to_wikis_by_owners,"#{namespace}.md"), home_passage.join.chomp)
      }

      plain_wiki_maps.each { |namespace, wikis|
        home_passage  = []
        home_passage << "## #{namespace}\n"
        home_passage << "\n"
        wikis.each { |wiki|
          home_passage << "- [[#{wiki.gsub(/\.md/, '')}]]\n"
        }
        home_passage << "\n"

        File.write(File.join(path_to_wikis_by_owners,"#{namespace}.md"), home_passage.join.chomp)
      }

      (owned_wiki_maps.keys + plain_wiki_maps.keys).each { |namespace| home_passage << "- [[#{namespace}]]\n" }
      home_passage << "\n"
      File.write(path_to_home, home_passage.join.chomp)
    else
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

      File.write(path_to_home, home_passage.join.chomp)
    end
  end
end
