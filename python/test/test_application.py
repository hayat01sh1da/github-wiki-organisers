import pytest

from application import Application


def test_validate_group_by(wiki_workspace):
    base_path = wiki_workspace()
    with pytest.raises(ValueError, match=r'^Invalid group_by: `Group`$'):
        Application(base_path=base_path, group_by='Group', language='English', home_overflow=False)


def test_validate_language(wiki_workspace):
    base_path = wiki_workspace()
    with pytest.raises(ValueError, match=r'^Invalid language: `Spanish`$'):
        Application(base_path=base_path, group_by='Owner', language='Spanish', home_overflow=False)


def test_validate_home_overflow(wiki_workspace):
    base_path = wiki_workspace()
    with pytest.raises(ValueError, match=r'^Invalid home_overflow: `foo` must be boolean$'):
        Application(base_path=base_path, group_by='Owner', language='English', home_overflow='foo')


def test_run_raises_not_implemented(wiki_workspace):
    base_path = wiki_workspace()
    with pytest.raises(NotImplementedError, match=r'^This method must be implemented in each subclass\.$'):
        Application(base_path=base_path, group_by='Owner', language='English', home_overflow=False).run()
