require 'minitest/autorun'
require 'fileutils'
require_relative '../src/application'

class ApplicationTest < Minitest::Test
  def setup(base_path: File.join('.', 'test', 'wiki'), group_by: '-o', language: '-en')
    @base_path = base_path
    @group_by  = group_by
    @language  = language
    FileUtils.mkdir_p(base_path) unless Dir.exist?(base_path)
    test_file_maps.each { |wiki, namespace|
      File.write(File.join(base_path, wiki), namespace)
    }
  end

  def teardown
    FileUtils.rm_rf(base_path) if Dir.exist?(base_path)
  end

  def test_validate_group_by!
    error = assert_raises ArgumentError do
      Application.new(base_path:, group_by: '-x', language:).validate!
    end
    assert_equal('Unknown group_by: `-x`', error.message)
  end

  def test_validate_language!
    error = assert_raises ArgumentError do
      Application.new(base_path:, group_by: '-o', language: '-spa').validate!
    end
    assert_equal('Unknown language: `-spa`', error.message)
  end

  def test_self_run
    error = assert_raises Application::NotImplementedError do
      Application.run(base_path:, group_by:)
    end
    assert_equal('This method must be implemented in each subclass.', error.message)
  end

  private

  attr_reader :base_path, :group_by, :language

  def test_file_maps
    case group_by
    when '-o', '--owner'
      case language
      when '-en'
        {
          'Owned Wiki.md' => 'Owner: @test-owner',
          'Unowned but Necessary Wiki.md' => 'Owner: Unowned but Necessary',
          'Unknown Owner nor Necessity Wiki.md' => 'Owner: Unknown Owner nor Necessity',
          'Unowned Wiki 1.md' => '',
          'Unowned Wiki 2.md' => 'This is a sample Wiki'
        }
      when '-ja'
        {
          'Owner記名ありページ.md' => 'Owner: @test-owner',
          'Ownerチームが不明だが必要なページ.md' => 'Owner: Ownerチームが不明だが必要なページ群',
          'Ownerチーム・要or不要が不明なページ.md' => 'Owner: Ownerチーム・要or不要が不明なページ群',
          'Owner記名なしページ1.md' => '',
          'Owner記名なしページ2.md' => 'サンプル Wiki'
        }
      end
    when '-c', '--category'
      case language
      when '-en'
        {
          'Categorised Wiki.md' => 'Category: test-category',
          'Uncategorised Wiki 1.md' => '',
          'Uncategorised Wiki 2.md' => 'This is a sample Wiki'
        }
      when '-ja'
        {
          'Category記載ありページ.md' => 'Category: test-category',
          'Category記載なしページ1.md' => '',
          'Category記載なしページ2.md' => 'サンプル Wiki'
        }
      end
    end
  end
end
