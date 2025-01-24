require_relative './application'

class Sidebar < Application
  def initialize(base_path)
    super(base_path)
    @base_owner_url = 'https://github.com/orgs/quipper/teams/'
    @wiki_list      = []
  end

  def run
    update_wiki_list
    IO.write(path_to_sidebar, wiki_list.join)
  end

  private

  attr_reader :base_owner_url, :wiki_list

  # @return [Hash<String => Array<String>>]
  def owner_and_wiki_maps_with_ownership
    @owner_and_wiki_maps_with_ownership ||= owner_and_wiki_maps.select { |owner, _| owner.include?('@') }
  end

  # @return [Hash<String => Array<String>>]
  def owner_and_wiki_maps_without_ownership
    @owner_and_wiki_maps_without_ownership ||= owner_and_wiki_maps.reject { |owner, _| owner.include?('@') }
  end

  # @return nil
  def update_wiki_list
    owner_and_wiki_maps_with_ownership.each { |owner, wikis|
      wiki_list << "- [#{owner}](#{base_owner_url + owner.gsub(/\@/, '')})\n"
      wikis.each { |wiki|
        wiki_list << "  - [[#{wiki.gsub(/\.md/, '')}]]\n"
      }
    }

    owner_and_wiki_maps_without_ownership.each { |namespace, wikis|
      wiki_list << "- #{namespace}\n"
      wikis.each { |wiki|
        wiki_list << "  - [[#{wiki.gsub(/\.md/, '')}]]\n"
      }
    }
  end
end
