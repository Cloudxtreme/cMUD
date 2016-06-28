from evennia import Command
from evennia.utils import evtable
from language.english.core.ooclook import *


class CmdOOCLook(Command):
    """
    An OOC version of the look command. This is called by the server
    when the player first connects to their account.
    """
    key = "look"
    locks = "cmd:all()"
    arg_regex = r"^$"

    def func(self):
        table = evtable.EvTable(OOCLOOK_HEADING, self.player,
                                table=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], border="cells")

        table.add_column("This is long data", "This is even longer data")
        table.add_row("This is a single row")
        self.msg(table)
