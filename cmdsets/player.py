"""

This is the cmdset for Player (OOC) commands.  These are
stored on the Player object and should thus be able to handle getting
a Player object as caller rather than a Character.

"""

from evennia.commands.cmdset import CmdSet
from evennia.commands.default import help, comms, admin, system
from evennia.commands.default import building, player
from commands.ooclook import CmdOOCLook


class PlayerCmdSet(CmdSet):
    """
    Implements the player command set.
    """

    key = "DefaultPlayer"
    priority = -10

    def at_cmdset_creation(self):

        # Player OOC commands
        self.add(CmdOOCLook())
        self.add(player.CmdIC())
        self.add(player.CmdOOC())
        self.add(player.CmdCharCreate())

        # Player-specific commands
        self.add(player.CmdWho())
        self.add(player.CmdOption())
        self.add(player.CmdQuit())
        self.add(player.CmdPassword())
        self.add(player.CmdColorTest())
        self.add(player.CmdQuell())

        # testing
        self.add(building.CmdExamine())

        # Help command
        self.add(help.CmdHelp())

        # system commands
        self.add(system.CmdReload())
        self.add(system.CmdReset())
        self.add(system.CmdShutdown())
        self.add(system.CmdPy())

        # Admin commands
        self.add(admin.CmdDelPlayer())
        self.add(admin.CmdNewPassword())

        # Comm commands
        self.add(comms.CmdAddCom())
        self.add(comms.CmdDelCom())
        self.add(comms.CmdAllCom())
        self.add(comms.CmdChannels())
        self.add(comms.CmdCdestroy())
        self.add(comms.CmdChannelCreate())
        self.add(comms.CmdClock())
        self.add(comms.CmdCBoot())
        self.add(comms.CmdCemit())
        self.add(comms.CmdCWho())
        self.add(comms.CmdCdesc())
        self.add(comms.CmdPage())
        self.add(comms.CmdIRC2Chan())
        self.add(comms.CmdRSS2Chan())
