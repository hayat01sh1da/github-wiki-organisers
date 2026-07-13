from collections.abc import Callable

import pytest

from spreen_wiki.application import Application


def test_validate_group_by(wiki_workspace: Callable[..., str]) -> None:
    base_path = wiki_workspace()
    with pytest.raises(ValueError, match=r'^Invalid group_by: `Group`$'):
        Application(
            base_path=base_path,
            group_by='Group',
            language='English',
            home_overflow=False,
        ).validate()


def test_validate_language(wiki_workspace: Callable[..., str]) -> None:
    base_path = wiki_workspace()
    with pytest.raises(ValueError, match=r'^Invalid language: `Spanish`$'):
        Application(
            base_path=base_path,
            group_by='Owner',
            language='Spanish',
            home_overflow=False,
        ).validate()


def test_validate_home_overflow(
        wiki_workspace: Callable[..., str]) -> None:
    base_path = wiki_workspace()
    with pytest.raises(
            ValueError,
            match=r'^Invalid home_overflow: `foo` must be boolean$'):
        Application(
            base_path=base_path,
            group_by='Owner',
            language='English',
            home_overflow='foo',
        ).validate()


def test_self_run(wiki_workspace: Callable[..., str]) -> None:
    base_path = wiki_workspace()
    with pytest.raises(
            Application.NotImplementedError,
            match=r'^This method must be implemented in each subclass\.$'):
        Application.run(base_path=base_path)
