#!/usr/bin/env python

"""Tests for `db_faker` package."""

import pytest
import logging

from db_faker import cli
from db_faker.commands.hello import Hello


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


def test_command_line_interface(caplog):
    """Test the CLI."""
    result = cli.main(argv=["hello"])
    logs = caplog.record_tuples
    assert result == 0
    assert (Hello.log.name, logging.INFO, "Hello world!") in logs
