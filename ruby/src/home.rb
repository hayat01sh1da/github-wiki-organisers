# rbs_inline: enabled

require_relative './application'
require 'fileutils'

class Home < Application
  HOME_URL = "https://github.com/#{ENV.fetch('ORGANISATION_NAME', 'hayat01sh1da')}/github-wiki-organisers/wiki".freeze

  # @rbs base_path: String
  # @rbs group_by: String
  # @rbs language: String
  # @rbs home_overflow: bool
  # @rbs return: void
  def initialize(base_path:, group_by:, language:, home_overflow:)
    super(base_path:, group_by:, language:, home_overflow:)
    @base_owner_url         = "https://github.com/orgs/#{ENV.fetch('ORGANISATION_NAME', 'hayat01sh1da')}/teams/"
    @path_to_wikis_by_owner = File.join(base_path, 'wikis-by-owner')
  end

  # @rbs return: String
  def run
    write_home_passage
    HOME_URL
  end

  private

  attr_reader :base_owner_url, :path_to_wikis_by_owner

  # @rbs return: String
  def path_to_home_template
    File.join('..', 'home_template', group_by.downcase, "#{language.downcase}.md")
  end

  # @rbs return: Array[String]
  def home_passage
    @home_passage ||= File.readlines(path_to_home_template).append("\n")
  end

  # @rbs return: void
  def write_home_passage
    if home_overflow
      FileUtils.mkdir_p(path_to_wikis_by_owner) unless Dir.exist?(path_to_wikis_by_owner)

      owned_wiki_maps.each { |namespace, wikis|
        home_passage  = Array.new
        home_passage << "## [#{namespace}](#{base_owner_url + namespace.gsub(/\@/, '')})\n"
        home_passage << "\n"
        wikis.each { |wiki|
          home_passage << "- [[#{wiki.gsub(/\.md/, '')}]]\n"
        }
        home_passage << "\n"

        File.write(File.join(path_to_wikis_by_owner,"#{namespace}.md"), home_passage.join.chomp)
      }

      plain_wiki_maps.each { |namespace, wikis|
        home_passage  = Array.new
        home_passage << "## #{namespace}\n"
        home_passage << "\n"
        wikis.each { |wiki|
          home_passage << "- [[#{wiki.gsub(/\.md/, '')}]]\n"
        }
        home_passage << "\n"

        File.write(File.join(path_to_wikis_by_owner,"#{namespace}.md"), home_passage.join.chomp)
      }

      (owned_wiki_maps.keys + plain_wiki_maps.keys).each { |namespace| home_passage << "- [[#{namespace}]]\n" }
      home_passage << "\n"
      File.write(path_to_home, home_passage.join.chomp)
    else
      FileUtils.rm_rf(path_to_wikis_by_owner) if Dir.exist?(path_to_wikis_by_owner)

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
