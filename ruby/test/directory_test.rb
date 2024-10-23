require_relative './application_test'
require_relative '../src/directory'

class DirectoryTest < ApplicationTest
  def setup
    super
    @dir_to_delete = File.join(base_path, 'foo')
    FileUtils.mkdir_p(dir_to_delete)
    Directory.run(base_path:)
  end

  def test_self_run
    assert_equal(File.exist?(File.join(base_path, 'test-owner', 'Owner記名ありページ.md')), true)
    assert_equal(File.exist?(File.join(base_path, 'Ownerチームが不明だが必要なページ群', 'Ownerチームが不明だが必要なページ.md')), true)
    assert_equal(File.exist?(File.join(base_path, 'Ownerチーム・要or不要が不明なページ群', 'Ownerチーム・要or不要が不明なページ.md')), true)
    assert_equal(File.exist?(File.join(base_path, 'Owner記名なし', 'Owner記名なしページ1.md')), true)
    assert_equal(File.exist?(File.join(base_path, 'Owner記名なし', 'Owner記名なしページ2.md')), true)
    assert_equal(File.exist?(dir_to_delete), false)
  end

  private

  attr_reader :dir_to_delete
end
