from django.shortcuts import render


def page_index(request):
    """
    Curses
    """

    pagevars = {
        "page_title": "Curses",
    }

    return render(request, 'curses/index.html', pagevars)


def page_vampire(request):
    """
    Curses
    """

    pagevars = {
        "page_title": "Vampire",
    }

    return render(request, 'curses/vampire.html', pagevars)


def page_werewolf(request):
    """
    Curses
    """

    pagevars = {
        "page_title": "Werewolf",
    }

    return render(request, 'curses/werewolf.html', pagevars)


def page_genie(request):
    """
    Curses
    """

    pagevars = {
        "page_title": "Genie",
    }

    return render(request, 'curses/genie.html', pagevars)