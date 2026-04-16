# rbs_inline: enabled

require_relative './application'

class Sidebar < Application
  # @rbs base_path: String
  # @rbs group_by: String
  # @rbs language: String
  # @rbs home_overflow: String
  # @rbs return: void
  def initialize(base_path: '', group_by: '', language: '', home_overflow: 'false')
    super(base_path:, group_by:, language:, home_overflow:)
    @base_owner_url = "https://github.com/orgs/#{ENV.fetch('ORGANISATION_NAME', 'hayat01sh1da')}/teams/"
    @wiki_list      = Array.new
  end

  # @rbs return: void
  def run
    update_wiki_list
    File.write(path_to_sidebar, wiki_list.join)
  end

  private

  attr_reader :base_owner_url, :wiki_list

  # @rbs return: void
  def update_wiki_list
    owned_wiki_maps.each { |namespace, wikis|
      wiki_list << "- [#{namespace}](#{base_owner_url + namespace.gsub(/\@/, '')})\n"
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
