#!/usr/bin/env python

"""Tests for `db_faker` package."""

import pytest

from db_faker import db_faker
from db_faker import cli


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_command_line_interface(capsys):
    """Test the CLI."""
    result = cli.main()
    captured = capsys.readouterr()
    assert result == 0
    assert 'Hello world!' in captured.out
