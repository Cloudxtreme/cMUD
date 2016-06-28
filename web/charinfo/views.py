from django.http import Http404
from django.shortcuts import render
from django.conf import settings

from evennia.utils.search import search_object
from evennia.utils.utils import inherits_from


def sheet(request, char_name):
    name = char_name
    try:
        character = search_object(name)[0]
    except IndexError:
        raise Http404("I couldn't find a character with that name.")
    if not inherits_from(character, settings.BASE_CHARACTER_TYPECLASS):
        raise Http404("I couldn't find a character with that name."
                      "Found something else instead.")
    return render(request, 'charinfo/sheet.html', {'character': character})
