"""
Evennia settings file.

"""
from evennia.settings_default import *
import re

######################################################################
# Evennia base server config
######################################################################

# This is the name of your game. Make it catchy!
SERVERNAME = "ConsecroMUD"

######################################################################
# Installed Apps
######################################################################

INSTALLED_APPS += ('web.chargen',)
INSTALLED_APPS += ('web.charinfo',)
INSTALLED_APPS += ('web.curses',)
INSTALLED_APPS += ('web.areas',)
INSTALLED_APPS += ('web.bugs',)
INSTALLED_APPS += ('web.account',)
INSTALLED_APPS += ('debug_toolbar',)

######################################################################
# Player settings
######################################################################

# Session mode
MULTISESSION_MODE = 2
# Max Characters per player
MAX_NR_CHARACTERS = 3
# Account name standards
ACCOUNT_NAME_STANDARDS = re.compile(r"^[a-z]{3,}$", re.I)
# Password min length
PASSWORD_LENGTH = 6
# Failed login password attempts
PASSWORD_ATTEMPTS = 3
# Forbidden Account Names
FORBIDDEN_NAMES = ['god', 'immortal', 'superman', 'watcher', 'gamemaster'
                   'thegamemaster', 'thewatcher', 'theimmortal', 'consecro',
                   'consecromud', 'theconsecro']


######################################################################
# Evennia commandsets
######################################################################

# command set used for login
CMDSET_UNLOGGEDIN = "cmdsets.prelogin.UnloggedinCmdSet"
CMDSET_PLAYER = "cmdsets.player.PlayerCmdSet"
CMDSET_CHARACTER = "cmdsets.character.CharacterCmdSet"


######################################################################
# Django web features
######################################################################

DEBUG = True

STATIC_ROOT = os.path.join(GAME_DIR, "web", "static")

LOGIN_REDIRECT_URL = '/account'
# Where to redirect users when using the @login_required decorator.
LOGIN_URL = '/account/login'
# Where to redirect users who wish to logout.
LOGOUT_URL = '/account/login'

# Location of static data to overload the defaults from
# evennia/web/webclient and evennia/web/website's static/ dirs.
STATICFILES_DIRS = (
    os.path.join(GAME_DIR, "web", "static_overrides"),)
# Patterns of files in the static directories. Used here to make sure that
# its readme file is preserved but unused.
STATICFILES_IGNORE_PATTERNS = ('README.md',)
# The name of the currently selected web template. This corresponds to the
# directory names shown in the templates directory.
WEBSITE_TEMPLATE = 'website'
WEBCLIENT_TEMPLATE = 'webclient'
# We setup the location of the website template as well as the admin site.
TEMPLATES = [{
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(GAME_DIR, "web", WEBSITE_TEMPLATE),
            os.path.join(GAME_DIR, "web", WEBCLIENT_TEMPLATE),
            os.path.join(GAME_DIR, "web"),
            os.path.join(EVENNIA_DIR, "web", "website", "templates", WEBSITE_TEMPLATE),
            os.path.join(EVENNIA_DIR, "web", "website", "templates"),
            os.path.join(EVENNIA_DIR, "web", "webclient", "templates", WEBCLIENT_TEMPLATE),
            os.path.join(EVENNIA_DIR, "web", "webclient", "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            "context_processors": [
                'django.template.context_processors.i18n',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.media',
                'django.template.context_processors.debug',
                'evennia.web.utils.general_context.general_context']
            }
        }]


# The secret key is randomly seeded upon creation. It is used to sign
# Django's cookies. Do not share this with anyone. Changing it will
# log out all active web browsing sessions. Game web client sessions
# may survive.
SECRET_KEY = 'g`WY~U^uFxkZSsB*"Rw-.8)5AHPf2I!toV/TJ"jC'
