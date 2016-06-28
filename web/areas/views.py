from django.shortcuts import render


def page_index(request):
    """
    Areas
    """

    pagevars = {
        "page_title": "AREA's",
    }

    return render(request, 'areas/index.html', pagevars)
