import logging
import json
import db_faker.utils as Utils

from cliff.command import Command
from jsonschema import validate


class ValidateSchema(Command):
    """
    Function that will validate the given JSON file to the JSON schema
    """

    def __init__(self):
        self.log = logging.getLogger(__name__)
        schema_path = Utils.get_root_path()/'schemas'/'dbSchema.json'
        with open(schema_path) as path:
            self.json_schema = json.load(path)

    def take_action(self, parsed_args):
        self.log.debug(self.json_schema)
        self.log.error("Not implemented yet!")
        exit(-1)
