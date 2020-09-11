#!/usr/bin/env python

"""
Unit tests for ValidateSchema command
"""

import pytest

from db_faker.commands.validate_schema import ValidateSchema


def test_check_json_schema_loads():
    """Checks that the JSON schema is loading"""
    cmd = ValidateSchema()
    schema = cmd.json_schema
    print(schema)
    assert schema is not None
