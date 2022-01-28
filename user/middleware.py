"""Middlewares for user"""

from django.contrib.auth.models import User

from user.models import UserLastRequest


def update_user_last_request_middleware(get_response):
    """Update UserLastRequest's object"""

    def middleware(request):
        response = get_response(request)
        user_id = request.POST.get('user_id', None)

        if user_id:
            user = User.objects.get(id=int(user_id))

            if UserLastRequest.objects.filter(user=user):
                user_last_request = UserLastRequest.objects.get(user=user)
                user_last_request.save()
            else:
                UserLastRequest.objects.create(user=user)

        return response

    return middleware
