from evennia import Command
from evennia import syscmdkeys
from evennia.utils.evmenu import EvMenu


class CmdUnloggedinLook(Command):
    """
    An unloggedin version of the look command. This is called by the server
    when the player first connects. It sets up the menu before handing off
    to the menu's own look command.
    """
    key = syscmdkeys.CMD_LOGINSTART
    locks = "cmd:all()"
    arg_regex = r"^$"

    def func(self):
        # Execute the menu
        menu = EvMenu(self.caller, "core.login_menu",
                      startnode="login", auto_quit=False, auto_help=False,
                      auto_look=False, node_formatter=_formatter)


def _formatter(nodetext, optionstext, caller=None):
    # removes the menu options from view
    return nodetext
