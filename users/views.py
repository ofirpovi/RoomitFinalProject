from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, OfferPropertyForm, ImageForm
from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import login_required
from .models import PropertyForOffer, Image, Profile

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
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your profile has been updated!')
            return redirect('profile', request.user)

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)

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
                #return redirect('profile', username=request.user.username, permanent=False)

    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'p_form': p_form
    }
    return render(request, 'users/fill_info.html', context)

@login_required
def insert_in_status(request):
    user = request.user
    if request.method == 'POST':
        form = OfferPropertyForm(request.POST)
        images= request.FILES.getlist('image')
        if form.is_valid():
            # set the user for the PropertyForOffer instance
            property = form.save(commit=False)
            property.user = user
            form.save()
            for image in images:
                Image.objects.create(property= property, image= image)
            messages.success(request, "Your peoperty info is save")    
            # Redirect to the property detail page
            return redirect('home')
    else:
        try: 
            property = get_object_or_404(PropertyForOffer, user=user)
            form = OfferPropertyForm(instance=property)
            imageform = ImageForm()
        except:
            form = OfferPropertyForm()
            imageform = ImageForm()
        
    return render(request, 'users/let_in_form.html', {'form': form, 'imageform': imageform})

def set_status(request):
    user = request.user
    if request.method == 'GET':
        #profile['status'] = request.POST['status']
        profile = Profile.objects.get(user=user)
        profile.status = request.GET['status']
        profile.save()
        if request.GET['status'] == 'insert in':
            return redirect('insert-in-status-form')