"""
EvMenu-driven login system
dsimmons 2016
"""

from django.conf import settings

from evennia import logger
from evennia import managers
from evennia.server.models import ServerConfig
from language.english.core.login import *
from server.conf.settings import *


# login menu
def login(caller):
    initial_login = caller.ndb.initial_login or 0
    if initial_login == 0:
        caller.ndb.initial_login = 1
        caller.ndb.password_attempts = 1
        text = LOGIN_SCREEN
        text += LOGIN_ACCOUNT
        options = (
            {
                "key": ("quit","Quit"),
                "goto": "quit_menu",
            },
            {
                "key": "new",
                "goto": "create_account",
            },
            {
                "key": "_default",
                "exec": _account_check,
                "goto": "login",
            },
        )
    elif caller.ndb.quit_menu_check is True:
        text = ""
        options = ()
    elif caller.ndb.passed_account_check is False:
        text = LOGIN_ACCOUNT
        options = (
            {
                "key": ("quit", "Quit"),
                "goto": "quit_menu",
            },
            {
                "key": "new",
                "goto": "create_account",
            },
            {
                "key": "_default",
                "exec": _account_check,
                "goto": "login",
            },
        )
    elif caller.ndb.passed_account_check is True:
        text = LOGIN_PASSWORD
        options = (
            {
                "key": ("quit", "Quit"),
                "goto": "quit_menu",
            },
            {
                "key": "_default",
                "exec": _password_check,
                "goto": "login",
            },
        )
    else:
        text = LOGIN_ERROR
        options = (
            {
                "key": ("quit", "Quit"),
                "goto": "quit_menu",
            },
            {
                "key": "_default",
                "goto": "login",
            },
        )
    return text, options


# account creation menu
def create_account(caller):
    if caller.ndb.passed_account_creation is True:
        text = ""
        options = ()
    elif caller.ndb.confirm_needed is True:
        text = LOGIN_PASSWORD_CONFIRM
        options = (
            {
                "key": ("quit", "Quit"),
                "goto": "quit_menu",
            },
            {
                "key": "_default",
                "exec": _confirm_password,
                "goto": "create_account"
            }
        )
    elif caller.ndb.passed_new_account_name is True:
        text = LOGIN_NEW_PASSWORD
        options = (
            {
                "key": ("quit", "Quit"),
                "goto": "quit_menu",
            },
            {
                "key": "_default",
                "exec": _create_password,
                "goto": "create_account",
            },
        )
    else:
        text = LOGIN_NEW_ACCOUNT
        options = (
            {
                "key": ("quit", "Quit"),
                "goto": "quit_menu",
            },
            {
                "key": "_default",
                "exec": _create_account,
                "goto": "create_account",
            },
        )
    return text, options


# disconnect user
def quit_menu(caller):
    caller.sessionhandler.disconnect(caller, LOGIN_DISCONNECT)
    return "", None


# check account
def _account_check(caller, user_input):
    user_input = user_input.strip()
    player = managers.players.get_player_from_name(user_input)
    if not player:
        caller.ndb.passed_account_check = False
        caller.msg(LOGIN_NO_ACCOUNT)
    else:
        caller.ndb.passed_account_check = True
        caller.ndb._menutree.player = player


# check password
def _password_check(caller, user_input):
    user_input = user_input.strip()
    menutree = caller.ndb._menutree
    player = menutree.player
    if not player.check_password(user_input):
        nattempts = caller.ndb.password_attempts
        if nattempts >= PASSWORD_ATTEMPTS:
            caller.msg(LOGIN_PASSWORD_ATTEMPTS)
            caller.ndb.quit_menu_check = True
            caller.sessionhandler.disconnect(caller, LOGIN_DISCONNECT)
        else:
            caller.ndb.passed_password_check = False
            caller.ndb.password_attempts += 1
            caller.msg(LOGIN_BAD_PASSWORD)
    else:
        bans = ServerConfig.objects.conf("server_bans")
        banned = bans and (any(tup[0] == player.name.lower() for tup in bans) or
                           any(tup[2].match(caller.address) for tup in bans if tup[2]))
        if banned:
            # banned IP or name
            caller.msg(LOGIN_BANNED)
            caller.ndb.quit_menu_check = True
            caller.sessionhandler.disconnect(caller, LOGIN_DISCONNECT)
        else:
            # log us in.
            caller.ndb.quit_menu_check = True
            caller.sessionhandler.login(caller, player)


# check new account
def _create_account(caller, user_input):
    menutree = caller.ndb._menutree
    user_input = user_input.strip()
    player = managers.players.get_player_from_name(user_input)
    if player:
        caller.msg(LOGIN_ACCOUNT_EXISTS.format(user_input))
    elif not ACCOUNT_NAME_STANDARDS.search(user_input):
        caller.msg(LOGIN_ACCOUNT_STANDARDS)
    elif user_input.lower() in FORBIDDEN_NAMES:
        caller.msg(LOGIN_FORBIDDEN_NAME.format(user_input))
    elif not player:
        menutree.playername = user_input
        caller.ndb.passed_new_account_name = True
    else:
        caller.msg(LOGIN_ERROR)


# check new password
def _create_password(caller, user_input):
    menutree = caller.ndb._menutree
    password = user_input.strip()
    if not hasattr(menutree, 'playername'):
        caller.msg(LOGIN_ERROR)
    else:
        if len(password) < PASSWORD_LENGTH:
            # The password is too short
            caller.msg(LOGIN_PASSWORD_STANDARDS)
        else:
            caller.ndb.new_password = password
            caller.ndb.confirm_needed = True


# confirm password
def _confirm_password(caller, user_input):
    password = caller.ndb.new_password
    menutree = caller.ndb._menutree
    if user_input == password:
        # Create the new player account
        playername = menutree.playername
        from evennia.commands.default import unloggedin
        # We make use of the helper functions from the default set here.
        # noinspection PyBroadException
        try:
            permissions = settings.PERMISSION_PLAYER_DEFAULT
            new_player = unloggedin._create_player(caller, playername,
                                                   password, permissions)
        except Exception:
            # We are in the middle between logged in and -not, so we have
            # to handle tracebacks ourselves at this point. If we don't, we
            # won't see any errors at all.
            caller.msg(LOGIN_ERROR)
            logger.log_trace()
        else:
            caller.ndb.passed_account_creation = True
            caller.msg(LOGIN_ACCOUNT_CREATED.format(playername))
            caller.sessionhandler.login(caller, new_player)
    else:
        caller.msg(LOGIN_PASSWORD_MISMATCH)
        caller.ndb.confirm_needed = False
