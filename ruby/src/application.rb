class Application
  class NotImplementedError < StandardError; end

  def self.run(base_path: File.join('..', '..'), group_by: 'Owner', language: 'English', home_overflow: false)
    instance = new(base_path:, group_by:, language:, home_overflow:)
    instance.validate!
    instance.run
  end

  def initialize(base_path:, group_by:, language:, home_overflow:)
    @base_path       = base_path
    @group_by        = group_by
    @language        = language
    @home_overflow   = home_overflow
    @path_to_home    = File.join(base_path, 'Home.md')
    @path_to_sidebar = File.join(base_path, '_Sidebar.md')
    @paths_to_wikis  = Dir[File.join(base_path, '**', '*.md')].sort
  end

  def validate!
    raise ArgumentError, "Invalid group_by: `#{group_by}`" unless ['Owner', 'Category'].include?(group_by)
    raise ArgumentError, "Invalid language: `#{language}`" unless ['English', 'Japanese'].include?(language)
    raise ArgumentError, "Invalid home_overflow: `#{home_overflow}` must be boolean" unless [true, false].include?(home_overflow)
  end

  def run
    raise NotImplementedError, 'This method must be implemented in each subclass.'
  end

  private

  attr_reader :base_path, :group_by, :language, :home_overflow, :path_to_home, :path_to_sidebar, :paths_to_wikis

  # @return [String]
  def target_paths
    @target_paths ||= paths_to_wikis.delete_if {
      it == path_to_home ||
      it == path_to_sidebar ||
      it =~ /github\-wiki\-organisers/ ||
      it =~ /wikis\-by\-owner/
    }
  end

  # @return [Regexp]
  def target_regexp
    @target_regexp ||= case group_by
    when 'Owner'
      /[Oo]wner:\s?/
    when 'Category'
      /[Cc]ategory:\s?/
    end
  end

  # @return [String]
  def no_declaration
    @no_declaration ||= case group_by
    when 'Owner'
      case language
      when 'English'
        'Unowned'
      when 'Japanese'
        'Owner記名なし'
      end
    when 'Category'
      case language
      when 'English'
        'Uncategorised'
      when 'Japanese'
        'Category記載なし'
      end
    end
  end

  # @return [Hash<String => Array<String>>]
  def wiki_maps_with_namespace
    hash                   = Hash.new { |hash, namespace| hash[namespace] = [] }
    uncategrised_wiki_maps = Hash.new { |hash, namespace| hash[namespace] = [] }

    @wiki_maps_with_namespace ||= target_paths.each.with_object(hash) { |target_path, hash|
      File.open(target_path) { |file|
        wiki = File.basename(file)

        namespace_declaration = file.readlines.first
        namespace             = if namespace_declaration&.start_with?(target_regexp)
          namespace_declaration.chomp.gsub(target_regexp, '')
        else
          no_declaration
        end

        hash[namespace] << wiki unless namespace == no_declaration
        uncategrised_wiki_maps[namespace] << wiki if namespace == no_declaration
      }
    }.sort.to_h.merge(uncategrised_wiki_maps)
  end

  # @return [Hash<String => Array<String>>]
  def owned_wiki_maps
    @owned_wiki_maps ||= wiki_maps_with_namespace.select { |namespace, _| namespace.include?('@') }
  end

  # @return [Hash<String => Array<String>>]
  def plain_wiki_maps
    @plain_wiki_maps ||= wiki_maps_with_namespace.reject { |namespace, _| namespace.include?('@') }
  end
end
