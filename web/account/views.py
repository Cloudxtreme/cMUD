from django.shortcuts import render
from models import PlayerChars


def page_login(request):
    """
    login
    """

    pagevars = {
        "page_title": "LOGIN",
    }

    return render(request, 'account/login.html', pagevars)


def page_index(request):
    """
    account index page
    """
    current_user = request.user
    p_id = current_user.id
    player_chars = PlayerChars.objects.filter(player_id=p_id)
    pagevars = {'chars': player_chars}
    return render(request, 'account/index.html', pagevars)
