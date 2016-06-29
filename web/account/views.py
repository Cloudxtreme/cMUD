from django.shortcuts import render


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
    login
    """

    pagevars = {
        "page_title": "PROFILE",
    }

    return render(request, 'account/index.html', pagevars)
