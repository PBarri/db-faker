#!/usr/bin/env python

"""Tests for the utils module."""

import pytest
import logging
import db_faker.utils as Utils

from pathlib import Path

# Get the absolute path of the current directory
current_absolute_path = Utils.get_root_path() / 'tests'


@pytest.mark.parametrize("path, expected", [
    (str(current_absolute_path / 'sample-schema.json'), True),
    ("./sample-schema.json", True),
    (str(current_absolute_path / 'invalid-file.txt'), False),
    ("./invalid-file.txt", False)])
def test_is_file(path: str, expected):
    """
    Tests files exists in unix platforms
    """
    # str_path = str(path)
    file_exists = Utils.file_exists(path)

    assert file_exists == expected
