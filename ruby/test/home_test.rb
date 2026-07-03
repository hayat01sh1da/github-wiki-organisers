# frozen_string_literal: true
# rbs_inline: enabled

require_relative 'application_test'
require_relative '../src/home'

class HomeTest < ApplicationTest
  def setup(group_by: 'Owner', language: 'English', home_overflow: false)
    super
    Home.run(base_path:, group_by:, language:, home_overflow:)
    @path_to_home           = File.join(base_path, 'Home.md')
    @home                   = File.read(path_to_home)
    @path_to_wikis_by_owner = File.join(base_path, 'wikis-by-owner')
  end

  private

  attr_reader :path_to_home, :home, :path_to_wikis_by_owner

  # Expected Home pages live under test/fixtures/home/.
  # @rbs basename: String
  # @rbs return: String
  def expected_home(basename)
    File.read(File.join('.', 'test', 'fixtures', 'home', basename))
  end

  module English
    class OwnedHomeTest < HomeTest
      class NonOverflowTest < OwnedHomeTest
        def test_self_run
          refute(Dir.exist?(path_to_wikis_by_owner))
          assert_equal(expected_home('english_owned_non_overflow.md'), home)
        end
      end

      class OverflowTest < OwnedHomeTest
        def setup
          super(home_overflow: true)
        end

        def test_self_run
          assert(Dir.exist?(path_to_wikis_by_owner))
          assert_equal(expected_home('english_owned_overflow.md'), home)
        end
      end
    end

    class CategorisedHomeTest < HomeTest
      def setup
        super(group_by: 'Category')
      end

      def test_self_run
        assert_equal(expected_home('english_categorised.md'), home)
      end
    end
  end

  module Japanese
    class OwnedHomeTest < HomeTest
      class NonOverflowTest < OwnedHomeTest
        def setup
          super(language: 'Japanese')
        end

        def test_self_run
          refute(Dir.exist?(path_to_wikis_by_owner))
          assert_equal(expected_home('japanese_owned_non_overflow.md'), home)
        end
      end

      class OverflowTest < OwnedHomeTest
        def setup
          super(language: 'Japanese', home_overflow: true)
        end

        def test_self_run
          assert(Dir.exist?(path_to_wikis_by_owner))
          assert_equal(expected_home('japanese_owned_overflow.md'), home)
        end
      end
    end

    class CategorisedHomeTest < HomeTest
      def setup
        super(group_by: 'Category', language: 'Japanese')
      end

      def test_self_run
        assert_equal(expected_home('japanese_categorised.md'), home)
      end
    end
  end
end
