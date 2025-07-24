require 'minitest/autorun'
require 'fileutils'
require_relative '../src/application'

class ApplicationTest < Minitest::Test
  def setup(base_path: File.join('.', 'test', 'wiki'), genre: '-o')
    @base_path = base_path
    @genre     = genre
    FileUtils.mkdir_p(base_path) unless Dir.exist?(base_path)
    test_file_maps.each { |wiki, namespace|
      IO.write(File.join(base_path, wiki), namespace)
    }
  end

  def teardown
    FileUtils.rm_rf(base_path) if Dir.exist?(base_path)
  end

  def test_validate!
    error = assert_raises ArgumentError do
      Application.new(base_path:, genre: '-x').validate!
    end
    assert_equal('Unknown genre: `-x`', error.message)
  end

  def test_self_run
    error = assert_raises Application::NotImplementedError do
      Application.run(base_path:, genre:)
    end
    assert_equal('This method must be implemented in each subclass.', error.message)
  end

  private

  attr_reader :base_path
  attr_accessor :genre

  def test_file_maps
    case genre
    when '-o', '--owner'
      {
        'Owner記名ありページ.md' => 'Owner: @test-owner',
        'Ownerチームが不明だが必要なページ.md' => 'Owner: Ownerチームが不明だが必要なページ群',
        'Ownerチーム・要or不要が不明なページ.md' => 'Owner: Ownerチーム・要or不要が不明なページ群',
        'Owner記名なしページ1.md' => '',
        'Owner記名なしページ2.md' => 'This is a sample Wiki'
      }
    when '-c', '--category'
      {
        'Category記載ありページ.md' => 'Category: test-category',
        'Category記載なしページ1.md' => '',
        'Category記載なしページ2.md' => 'This is a sample Wiki'
      }
    end
  end
end
