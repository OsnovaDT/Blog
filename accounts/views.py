"""Views of accounts app"""

from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect

from blog.views import add_user_id_to_request


class SignUpView(CreateView):
    """User's signup"""

    form_class = UserCreationForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('accounts:login')


@login_required
def change_password(request):
    """Change user's password"""

    add_user_id_to_request(request)

    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)

            return redirect('post:all')

        return render(request, 'accounts/password_change.html', {
            'form': form,
        })

    form = PasswordChangeForm(user=request.user)

    return render(request, 'accounts/password_change.html', {
        'form': form,
    })
