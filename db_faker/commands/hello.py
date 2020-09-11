import logging

from cliff.command import Command


class Hello(Command):
    """Simple hello world command"""

    log = logging.getLogger(__name__)

    def take_action(self, parsed_args):
        self.log.info("Hello world!")
