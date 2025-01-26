require 'minitest/autorun'
require 'fileutils'
require_relative '../src/application'

class ApplicationTest < Minitest::Test
  def setup
    @base_path = File.join('.', 'test', 'wiki')
    FileUtils.mkdir_p(base_path) unless Dir.exist?(base_path)
    test_file_maps.each { |wiki, namespace|
      IO.write(File.join(base_path, wiki), namespace)
    }
  end

  def teardown
    FileUtils.rm_rf(base_path) if Dir.exist?(base_path)
  end

  def test_self_run
    error = assert_raises Application::NotImplementedError do
      Application.run
    end
    assert_equal(error.message, 'This method must be implemented in each subclass.')
  end

  private

  attr_reader :base_path

  def test_file_maps
    {
      'Owner記名ありページ.md' => 'Owner: @test-owner',
      'Ownerチームが不明だが必要なページ.md' => 'Owner: Ownerチームが不明だが必要なページ群',
      'Ownerチーム・要or不要が不明なページ.md' => 'Owner: Ownerチーム・要or不要が不明なページ群',
      'Owner記名なしページ1.md' => '',
      'Owner記名なしページ2.md' => 'This is a sample Wiki'
    }
  end
end
