class Application
  class NotImplementedError < StandardError; end

  def self.run(base_path: File.join('..', '..'))
    new(base_path).run
  end

  def initialize(base_path)
    @base_path       = base_path
    @path_to_home    = File.join(base_path, 'Home.md')
    @path_to_sidebar = File.join(base_path, '_Sidebar.md')
    @paths_to_wikis  = Dir[File.join(base_path, '**', '*.md')].sort
  end

  def run
    raise NotImplementedError, 'This method must be implemented in each subclass.'
  end

  private

  attr_reader :base_path, :path_to_home, :path_to_sidebar, :paths_to_wikis

  # @return [String]
  def target_paths
    @target_paths ||= paths_to_wikis.delete_if { it == path_to_home || it == path_to_sidebar || it =~ /github\-wiki\-organisers/ }
  end

  # @return [Hash<String => Array<String>>]
  def owner_and_wiki_maps
    @owner_and_wiki_maps ||= target_paths.each.with_object(Hash.new { |hash, owner| hash[owner] = [] }) { |target_path, hash|
      File.open(target_path) { |file|
        wiki = File.basename(file)

        ownership_declaration = file.readlines.first
        owner = if ownership_declaration&.start_with?(/[Oo]wner/)
          ownership_declaration.chomp.gsub(/Owner:\s?/, '')
        else
          'Owner記名なし'
        end

        hash[owner] << wiki
      }
    }.sort.to_h
  end
end
