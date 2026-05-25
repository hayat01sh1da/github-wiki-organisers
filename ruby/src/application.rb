# frozen_string_literal: true
# rbs_inline: enabled

# Base class for the wiki-organising commands. Loads the wiki tree under
# base_path, groups it by Owner or Category in either English or Japanese, and
# exposes the resulting maps to its subclasses.
class Application
  class NotImplementedError < StandardError; end

  NO_DECLARATION = {
    %w[Owner English]     => 'Unowned',
    %w[Owner Japanese]    => 'Owner記名なし',
    %w[Category English]  => 'Uncategorised',
    %w[Category Japanese] => 'Category記載なし'
  }.freeze

  TARGET_REGEXP = {
    'Owner'    => /[Oo]wner:\s?/,
    'Category' => /[Cc]ategory:\s?/
  }.freeze

  # @rbs base_path: String
  # @rbs group_by: String
  # @rbs language: String
  # @rbs home_overflow: String
  # @rbs return: void
  def self.run(base_path: File.join('..', '..'), group_by: 'Owner', language: 'English', home_overflow: 'false')
    instance = new(base_path:, group_by:, language:, home_overflow:)
    instance.validate!
    instance.run
  end

  # @rbs base_path: String
  # @rbs group_by: String
  # @rbs language: String
  # @rbs home_overflow: String
  # @rbs return: void
  def initialize(base_path:, group_by:, language:, home_overflow:)
    @base_path     = base_path
    @group_by      = group_by
    @language      = language
    @home_overflow = parse_home_overflow(home_overflow)
    @path_to_home                   = File.join(base_path, 'Home.md')
    @path_to_sidebar                = File.join(base_path, '_Sidebar.md')
    @path_to_github_wiki_organisers = Dir[File.join(base_path, 'github-wiki-organisers', '**', '*.md')]
    @path_to_wikis_by_owner         = Dir[File.join(base_path, 'wikis-by-owner', '*.md')]
    @paths_to_wikis                 = Dir[File.join(base_path, '**', '*.md')]
  end

  # @rbs return: void
  def validate!
    raise ArgumentError, "Invalid group_by: `#{group_by}`" unless %w[Owner Category].include?(group_by)
    raise ArgumentError, "Invalid language: `#{language}`" unless %w[English Japanese].include?(language)

    return if [true, false].include?(home_overflow)

    raise ArgumentError, "Invalid home_overflow: `#{home_overflow}` must be boolean"
  end

  # @rbs return: void
  def run
    raise NotImplementedError, 'This method must be implemented in each subclass.'
  end

  private

  attr_reader :base_path,
              :group_by,
              :language,
              :home_overflow,
              :path_to_home,
              :path_to_sidebar,
              :path_to_github_wiki_organisers,
              :path_to_wikis_by_owner,
              :paths_to_wikis

  # @rbs raw: String
  # @rbs return: (bool | String)
  def parse_home_overflow(raw)
    case raw
    when 'true'  then true
    when 'false' then false
    else raw
    end
  end

  # @rbs return: Array[String]
  def target_paths
    @target_paths ||= paths_to_wikis.delete_if do |path_to_wiki|
      path_to_wiki == path_to_home ||
        path_to_wiki == path_to_sidebar ||
        path_to_github_wiki_organisers.include?(path_to_wiki) ||
        path_to_wikis_by_owner.include?(path_to_wiki)
    end
  end

  # @rbs return: Regexp
  def target_regexp
    @target_regexp ||= TARGET_REGEXP.fetch(group_by, //)
  end

  # @rbs return: String
  def no_declaration
    @no_declaration ||= NO_DECLARATION.fetch([group_by, language], '')
  end

  # @rbs array: Array[untyped]
  # @rbs hash: Hash[String, Array[untyped]]
  # @rbs return: Hash[String, Array[String]]
  def wiki_maps_with_namespace(array = [], hash = Hash.new { |h, namespace| h[namespace] = array.dup })
    uncategorised = hash

    @wiki_maps_with_namespace ||= target_paths.each.with_object(hash.dup) do |target_path, acc|
      populate_namespace(target_path, acc, uncategorised)
    end.sort.to_h.merge(uncategorised)
  end

  # @rbs target_path: String
  # @rbs hash: Hash[String, Array[String]]
  # @rbs uncategorised: Hash[String, Array[String]]
  # @rbs return: void
  def populate_namespace(target_path, hash, uncategorised)
    return unless File.exist?(target_path)

    File.open(target_path) do |file|
      wiki      = File.basename(file)
      namespace = namespace_for(file)

      target = namespace == no_declaration ? uncategorised : hash
      target[namespace] << wiki
    end
  end

  # @rbs file: File
  # @rbs return: String
  def namespace_for(file)
    declaration = file.readlines.first
    return no_declaration unless declaration&.start_with?(target_regexp)

    declaration.chomp.gsub(target_regexp, '')
  end

  # @rbs return: Hash[String, Array[String]]
  def owned_wiki_maps
    @owned_wiki_maps ||= wiki_maps_with_namespace.select { |namespace, _| namespace.include?('@') }
  end

  # @rbs return: Hash[String, Array[String]]
  def plain_wiki_maps
    @plain_wiki_maps ||= wiki_maps_with_namespace.reject { |namespace, _| namespace.include?('@') }
  end
end
