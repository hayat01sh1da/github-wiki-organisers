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

  # @return [Hash<String => Array<String>>]
  def owned_wiki_maps
    @owned_wiki_maps ||= wiki_maps_with_namespace.select { |namespace, _| namespace.include?('@') }
  end

  # @return [Hash<String => Array<String>>]
  def plain_wiki_maps
    @plain_wiki_maps ||= wiki_maps_with_namespace.reject { |namespace, _| namespace.include?('@') }
  end

  # @return [String]
  def target_paths
    @target_paths ||= paths_to_wikis.delete_if { it == path_to_home || it == path_to_sidebar || it =~ /github\-wiki\-organisers/ }
  end

  # @return [Hash<String => Array<String>>]
  def wiki_maps_with_namespace
    hash                        = Hash.new { |hash, namespace| hash[namespace] = [] }
    @wiki_maps_with_namespace ||= target_paths.each.with_object(hash) { |target_path, hash|
      File.open(target_path) { |file|
        wiki = File.basename(file)

        namespace_declaration = file.readlines.first
        namespace             = if namespace_declaration&.start_with?(/[Oo]wner/)
          namespace_declaration.chomp.gsub(/[Oo]wner:\s?/, '')
        else
          'Owner記名なし'
        end

        hash[namespace] << wiki
      }
    }.sort.to_h
  end
end
