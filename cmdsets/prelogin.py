"""
Pre login cmdset

"""

from evennia import CmdSet
from commands.unloggedinlook import CmdUnloggedinLook


class UnloggedinCmdSet(CmdSet):
    # Cmdset for the unloggedin state
    key = "DefaultUnloggedin"
    priority = 0

    def at_cmdset_creation(self):
        # Called when cmdset is first created.
        self.add(CmdUnloggedinLook())
