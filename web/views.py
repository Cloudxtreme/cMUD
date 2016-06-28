
"""
This file contains the generic, assorted views that don't fall under one of
the other applications. Views are django's way of processing e.g. html
templates on the fly.

"""
from django.conf import settings
from django.shortcuts import render

from evennia.objects.models import ObjectDB
from evennia.players.models import PlayerDB
from evennia.utils import logger

from django.contrib.auth import login

_BASE_CHAR_TYPECLASS = settings.BASE_CHARACTER_TYPECLASS


def _shared_login(request):
    """
    Handle the shared login between website and webclient.

    """
    csession = request.session
    player = request.user
    sesslogin = csession.get("logged_in", None)

    if csession.session_key is None:
        # this is necessary to build the sessid key
        csession.save()
    elif player.is_authenticated():
        if not sesslogin:
            csession["logged_in"] = player.id
    elif sesslogin:
        # The webclient has previously registered a login to this csession
        player = PlayerDB.objects.get(id=sesslogin)
        try:
            login(request, player)
        except AttributeError:
            logger.log_trace()


def _gamestats():
    # TODO: Move this to either SQL or settings.py based configuration.
    fpage_player_limit = 4

    # A QuerySet of the most recently connected players.
    recent_users = PlayerDB.objects.get_recently_connected_players()[:fpage_player_limit]
    nplyrs_conn_recent = len(recent_users) or "0"
    nplyrs = PlayerDB.objects.num_total_players() or "0"
    nplyrs_reg_recent = len(PlayerDB.objects.get_recently_created_players()) or "0"
    nsess = len(PlayerDB.objects.get_connected_players()) or "0"

    nobjs = ObjectDB.objects.all().count()
    nrooms = ObjectDB.objects.filter(db_location__isnull=True).exclude(db_typeclass_path=_BASE_CHAR_TYPECLASS).count()
    nexits = ObjectDB.objects.filter(db_location__isnull=False, db_destination__isnull=False).count()
    nchars = ObjectDB.objects.filter(db_typeclass_path=_BASE_CHAR_TYPECLASS).count()
    nothers = nobjs - nrooms - nchars - nexits

    pagevars = {
        "page_title": "Front Page",
        "players_connected_recent": recent_users,
        "num_players_connected": nsess or "0",
        "num_players_registered": nplyrs or "no",
        "num_players_connected_recent": nplyrs_conn_recent or "0",
        "num_players_registered_recent": nplyrs_reg_recent or "0",
        "num_rooms": nrooms or "0",
        "num_exits": nexits or "0",
        "num_objects": nobjs or "0",
        "num_characters": nchars or "0",
        "num_others": nothers or "0"
    }
    return pagevars


def page_index(request):
    """
    Main root page.
    """

    # handle webclient-website shared login
    _shared_login(request)

    # get game db stats
    pagevars = _gamestats()

    return render(request, 'index.html', pagevars)


def page_faqs(request):
    """
    Frequent Questions.
    """

    pagevars = {
        "page_title": "FAQ's",
    }

    return render(request, 'faqs.html', pagevars)


def page_features(request):
    """
    Frequent Questions.
    """

    pagevars = {
        "page_title": "Features",
    }

    return render(request, 'features.html', pagevars)