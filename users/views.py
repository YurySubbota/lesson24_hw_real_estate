from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from users.forms import ProfileForm
from users.models import Profile


# Create your views here.

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/singup.html'
    success_url = reverse_lazy('login')


@login_required(login_url='login')
def create_profile(request):
    action = 'Create Profile'
    message = None
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            form.save_m2m()
            return redirect('personal_account')
        message = 'you must fill out Phone Number'
    else:
        form = ProfileForm()

    return render(request, 'registration/profile.html', {'form': form,
                                                         'message': message, 'action': action})


@login_required(login_url='login')
def edite_profile(request):
    action = 'Edite Profile'
    message = None
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            form.save_m2m()
            return redirect('personal_account')
        message = 'you must fill out Phone Number'
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'registration/profile.html', {'form': form,
                                                         'message': message, 'action': action})
