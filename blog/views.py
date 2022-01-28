"""Views for blog project"""

def add_user_id_to_request(request):
    """Add user's id to request.POST"""

    request.POST._mutable = True
    request.POST.update({'user_id': request.user.id})
    request.POST._mutable = False
