require 'fileutils'
require_relative './application'

class Directory < Application
  def run
    mkdirs
    mv_wikis_to_dirs
    delete_empty_dirs
  end

  private

  # @return [Hash<String => String>]
  def source_path_maps
    @source_path_maps ||= target_paths.map.with_object({}) { |target_path, hash|
      dirname        = File.dirname(target_path)
      filename       = File.basename(target_path)
      hash[filename] = File.join(dirname, filename)
    }
  end

  # @return [Array<String>]
  def target_dirs
    @target_dirs ||= owner_and_wiki_maps.keys.map { |dir| dir.gsub(/\@/, '') }
  end

  # @return [Array<String>]
  def mkdirs
    return unless target_dirs
    target_dirs.each { |target_dir|
      path = File.join(base_path, target_dir)
      FileUtils.mkdir_p(path) unless Dir.exist?(path)
    }
  end

  # @return [Array<String>]
  def mv_wikis_to_dirs
    owner_and_wiki_maps.each { |owner, wikis|
      wikis.each { |wiki|
        dest_path = File.join(base_path, owner.gsub(/\@/, ''), wiki)
        FileUtils.move(source_path_maps[wiki], dest_path) unless source_path_maps[wiki] == dest_path
      }
    }
  end

  # @return [Array<String>]
  def delete_empty_dirs
    dirs = Dir[File.join(base_path, '**')].uniq
    dirs.each { |dir|
      # [NOTE] Navigation pages are needed.
      if dir == path_to_home || dir == path_to_sidebar
        next
      # [NOTE] Wiki-related files are needed.
      elsif Dir[File.join(dir, '**', '*.md')].any? || Dir[File.join(dir, '**', '*.png')].any?
        next
      # [NOTE] Ruby files for automation are needed.
      elsif Dir[File.join(dir, '**', '*.rb')].any?
        next
      else
        FileUtils.rm_rf(dir)
      end
    }
  end
end
