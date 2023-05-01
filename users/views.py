from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy

from roomit_app.views import update_scores
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, ImageForm, OfferPropertyForm
from .models import PropertyForOffer, Image, Profile

from roomit_app.forms import UpdateRequirementsPForm, UpdateRequirementsRForm
from roomit_app.models import RequirementsR, RequirementsP
from django.views.generic.edit import FormView
from django.views.generic import CreateView, UpdateView, TemplateView

from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, 'Hi {}, welcome to ROOMIT! You can now edit your profile'.format(username))
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],)
            login(request, new_user)
            return redirect('fill_info', new_user)
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    u_form = UserUpdateForm(instance=user)
    p_form = ProfileUpdateForm(instance=user)
    read_only = False
    if request.user.username != username:
        read_only = True

    if request.method == 'POST' and request.user.username == username:
        # if request.user == user:
        print('in if')
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            update_scores(request)
            messages.success(request, f'Your profile has been updated!')
            return redirect('profile', request.user)

    context = {
        'user_profile': user,
        'u_form': u_form,
        'p_form': p_form,
        'read_only': read_only,
    }
    print(f'username:{user.username}\nemail: {user.email}')
    return render(request, 'users/other_profile.html', context)


# @login_required
# def profile(request, username):
#     if request.method == 'POST':
#         u_form = UserUpdateForm(request.POST, instance=request.user)
#         p_form = ProfileUpdateForm(request.POST,
#                                    request.FILES,
#                                    instance=request.user.profile)
#         if u_form.is_valid() and p_form.is_valid():
#             u_form.save()
#             p_form.save()
#             update_scores(request)
#             messages.success(request, f'Your profile has been updated!')
#             return redirect('profile', request.user)

#     else:
#         u_form = UserUpdateForm(instance=request.user)
#         p_form = ProfileUpdateForm(instance=request.user.profile)

#     context = {
#         'u_form': u_form,
#         'p_form': p_form
#     }
#     return render(request, 'users/profile.html', context)

@login_required
def info(request, username):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, "Your personal details have been saved and your profile has been created. You can see your profile and edit it at any time by clicking on the 'profile' tab on the top right of the screen.")
            return render(request, 'users/choose_status.html')
            # return redirect('profile', username=request.user.username, permanent=False)

    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'p_form': p_form
    }
    return render(request, 'users/fill_info.html', context)


@login_required
def create_property_offer_view(request):
    user = request.user
    if request.method == 'POST':
        pOffer_form = OfferPropertyForm(request.POST)
        if pOffer_form.is_valid():
           # check if the property for the current user already exists
            if PropertyForOffer.objects.filter(user_id=user.id).exists():
                # update the existing property instance
                property = PropertyForOffer.objects.get(user_id=user.id)
                pOffer_form = OfferPropertyForm(
                    request.POST, instance=property)
            else:
                # create a new property instance for the user
                property = pOffer_form.save(commit=False)
                property.user_id = user.id
            pOffer_form.save()
            # process images only if they were uploaded
            if request.FILES:
                images = request.FILES.getlist('image')
                for image in images:
                    Image.objects.create(property=property, image=image)
            messages.success(request, "Your property info has been saved")
            update_scores(request)
            # Redirect to the property detail page
            return redirect('requirementsR', request.user)
    else:
        try:
            property = get_object_or_404(PropertyForOffer, user=user)
            pOffer_form = OfferPropertyForm(instance=property)
            image_form = ImageForm()
        except:
            pOffer_form = OfferPropertyForm()
            image_form = ImageForm()

        context = {
            'pOffer_form': pOffer_form,
            'image_form': image_form,
        }

    return render(request, 'users/let_in_form.html', context)


@login_required
def set_status(request):
    if request.method == 'GET':
        Profile.objects.filter(user=request.user).update(
            profile_status=request.GET['status'])
        if request.GET['status'] == 'insert in':
            return redirect('property-offer-create')
        else:
            return redirect('requirementsP', request.user)
