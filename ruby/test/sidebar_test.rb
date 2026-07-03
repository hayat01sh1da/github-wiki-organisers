# frozen_string_literal: true
# rbs_inline: enabled

require_relative 'application_test'
require_relative '../src/sidebar'

class SidebarTest < ApplicationTest
  def setup(group_by: 'Owner', language: 'English')
    super
    Sidebar.run(base_path:, group_by:, language:)
    @path_to_sidebar = File.join(base_path, '_Sidebar.md')
    @sidebar         = File.read(path_to_sidebar)
  end

  private

  attr_reader :path_to_sidebar, :sidebar

  # Expected Sidebar pages live under test/fixtures/sidebar/.
  def expected_sidebar(basename)
    File.read(File.join('.', 'test', 'fixtures', 'sidebar', basename))
  end

  module English
    class OwnedSidebarTest < SidebarTest
      def test_self_run
        assert_equal(expected_sidebar('english_owned.md'), sidebar)
      end
    end

    class PlainSidebarTest < SidebarTest
      def setup
        super(group_by: 'Category')
      end

      def test_self_run
        assert_equal(expected_sidebar('english_categorised.md'), sidebar)
      end
    end
  end

  module Japanese
    class OwnedSidebarTest < SidebarTest
      def setup
        super(language: 'Japanese')
      end

      def test_self_run
        assert_equal(expected_sidebar('japanese_owned.md'), sidebar)
      end
    end

    class PlainSidebarTest < SidebarTest
      def setup
        super(group_by: 'Category', language: 'Japanese')
      end

      def test_self_run
        assert_equal(expected_sidebar('japanese_categorised.md'), sidebar)
      end
    end
  end
end
