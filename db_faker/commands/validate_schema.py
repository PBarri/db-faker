import logging
import json
import db_faker.utils as utils

from pathlib import Path
from cliff.command import Command
from jsonschema import validate, ValidationError


class ValidateSchema(Command):
    """
    Command that will validate the given JSON file to the JSON schema
    """
    def __init__(self, app, app_args):
        super(ValidateSchema, self).__init__(app, app_args, cmd_name="validate-schema")
        self.log = logging.getLogger(__name__)
        schema_path = utils.get_root_path()/'schemas'/'dbSchema.json'
        with open(schema_path) as path:
            self.json_schema = json.load(path)

    def get_parser(self, prog_name):
        parser = super(ValidateSchema, self).get_parser(prog_name)
        parser.add_argument('-s', '--schema', default='./schema.json', metavar='',
                            help='The schema to be used for generating the fake data', type=str)
        return parser

    def take_action(self, parsed_args):
        self.log.debug("Selected schema: %s", parsed_args.schema)
        schema = parsed_args.schema

        if utils.file_exists(schema):
            with open(utils.get_file_abs_path(schema)) as schema_file:
                schema_to_validate_json = json.load(schema_file)
                try:
                    # Validate the desired JSON file against the JSON schema for the database definition
                    validate(schema_to_validate_json, self.json_schema)
                    self.log.info("The schema is valid")
                except ValidationError as e:
                    self.log.error("The schema passed is not valid")
                    self.log.error(e.message)
        else:
            self.log.error("The file could not be found")
            raise FileNotFoundError()
