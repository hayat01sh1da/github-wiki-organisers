require_relative './application'

class Sidebar < Application
  def initialize(base_path)
    super(base_path)
    @base_owner_url = "https://github.com/orgs/#{ENV.fetch('USERNAME', 'hayat01sh1da')}/teams/"
    @wiki_list      = []
  end

  def run
    update_wiki_list
    File.write(path_to_sidebar, wiki_list.join)
  end

  private

  attr_reader :base_owner_url, :wiki_list

  # @return nil
  def update_wiki_list
    owned_wiki_maps.each { |owner, wikis|
      wiki_list << "- [#{owner}](#{base_owner_url + owner.gsub(/\@/, '')})\n"
      wikis.each { |wiki|
        wiki_list << "  - [[#{wiki.gsub(/\.md/, '')}]]\n"
      }
    }

    plain_wiki_maps.each { |namespace, wikis|
      wiki_list << "- #{namespace}\n"
      wikis.each { |wiki|
        wiki_list << "  - [[#{wiki.gsub(/\.md/, '')}]]\n"
      }
    }
  end
end
