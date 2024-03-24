from datetime import datetime, timezone
from django.shortcuts import render, get_object_or_404, redirect
from users.models import Profile
from real_estate.models import RealEstate, Photo, CityDistrict, Metro, DealRequest
from django.contrib.auth.decorators import login_required
from real_estate.forms import RealEstateForm, DealRequestForm, PhotoForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.models import User
from real_estate.estate_filters import estate_filters
from real_estate.messages import new_message_count, see_all_messages


def index(request):
    message = None
    new_messages = new_message_count(request)
    city_district = CityDistrict.objects.all()
    metro_station = Metro.objects.all()
    estates = estate_filters(request)

    paginator = Paginator(estates, 3)
    page = request.GET.get('page')
    try:
        estates = paginator.page(page)
    except PageNotAnInteger:
        estates = paginator.page(1)
    except EmptyPage:
        estates = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {
        'estates': estates, 'message': message,
        'city_district': city_district, 'metro_station': metro_station,
        'new_messages': new_messages})


def detail_estate(request, estate_id):
    new_messages = new_message_count(request)
    try:
        users_profile = Profile.objects.get(user=request.user)
    except (TypeError, Profile.DoesNotExist):
        users_profile = None
    estate = get_object_or_404(RealEstate, id=estate_id)
    profile = get_object_or_404(Profile, pk=estate.owner)
    photos = Photo.objects.filter(estate=estate)
    return render(request, 'details.html', {'estate': estate,
                                            'profile': profile, 'photos': photos, 'users_profile': users_profile,
                                            'new_messages': new_messages})


@login_required(login_url='login')
def personal_account(request, *args, **kwargs):
    new_messages = new_message_count(request)
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = None
    estates = RealEstate.objects.filter(owner=request.user)
    return render(request, 'personal_account.html', {'profile': profile, 'estates': estates,
                                                     'new_messages': new_messages})


@login_required(login_url='login')
def create_announcement(request):
    new_messages = new_message_count(request)
    message = None
    if request.method == 'POST':
        form = RealEstateForm(request.POST, request.FILES)
        if form.is_valid():
            estate = form.save(commit=False)
            estate.owner = request.user
            estate.save()
            form.save_m2m()
            return redirect('personal_account')
        else:
            message = 'you must fill out'
    else:
        form = RealEstateForm()

    return render(request, 'create_announcement.html', {'form': form, 'message': message,
                                                        'new_messages': new_messages})


@login_required(login_url='login')
def edit_announcement(request, estate_id):
    new_messages = new_message_count(request)
    estate = get_object_or_404(RealEstate, id=estate_id)
    if estate.owner != request.user:
        return redirect('personal_account')
    message = None
    if request.method == 'POST':
        form = RealEstateForm(request.POST, request.FILES)
        if form.is_valid():
            estate = form.save(commit=False)
            estate.id = estate_id
            estate.owner = request.user
            estate.created_at = datetime.now(timezone.utc)
            estate.save()
            form.save_m2m()
            return redirect('personal_account')
        else:
            message = 'you must fill out'
    else:
        form = RealEstateForm(instance=estate)

    return render(request, 'edit_announcement.html', {'form': form, 'estate': estate,
                                                      'message': message, 'new_messages': new_messages})


@login_required(login_url='login')
def delete_announcement(request, estate_id):
    estate = get_object_or_404(RealEstate, id=estate_id)
    if estate.owner != request.user:
        return redirect('personal_account')
    estate.delete()
    return redirect('personal_account')


def all_sellers_announcements(request, user_id):
    new_messages = new_message_count(request)
    seller = get_object_or_404(User, id=user_id)
    profile = get_object_or_404(Profile, user=seller)
    estates = RealEstate.objects.filter(owner=seller)
    return render(request, 'all_sellers_announcements.html', {"estates": estates,
                                                              "profile": profile, 'new_messages': new_messages})


@login_required(login_url='login')
def deal_request_view(request, estate_id):
    new_messages = new_message_count(request)
    if not request.user.profile:
        return redirect('create_profile')
    message = None
    if request.method == 'POST':
        form = DealRequestForm(request.POST, request.FILES)
        if form.is_valid():
            deal_request = form.save(commit=False)
            deal_request.buyer = request.user
            deal_request.estate = RealEstate.objects.get(id=estate_id)
            deal_request.save()
            form.save_m2m()
            return redirect('personal_account')
        else:
            message = 'you must fill out'
    else:
        form = DealRequestForm()

    return render(request, 'deal_request.html', {'form': form, 'message': message,
                                                 'new_messages': new_messages})


@login_required(login_url='login')
def read_all_messages(request):
    new_messages = new_message_count(request)
    all_messages = see_all_messages(request)
    return render(request, 'read_all_messages.html', {'new_messages': new_messages,
                                                      'all_messages': all_messages})


@login_required(login_url='login')
def read_detail_message(request, deal_request_id):
    new_messages = new_message_count(request)
    deal_request = DealRequest.objects.get(id=deal_request_id)
    photos = Photo.objects.filter(estate=deal_request.estate)
    deal_request.is_read = True
    deal_request.save()
    return render(request, 'read_detail_message.html', {'new_messages': new_messages,
                                                        'deal_request': deal_request, 'photos': photos})


@login_required(login_url='login')
def add_photo(request, estate_id):
    new_messages = new_message_count(request)
    estate = get_object_or_404(RealEstate, id=estate_id)
    if estate.owner != request.user:
        return redirect('personal_account')
    message = None
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.estate = estate
            photo.save()
            form.save_m2m()
            return redirect('edit_announcement', estate_id=estate_id)
        else:
            message = 'you must fill out'
    else:
        form = PhotoForm()

    return render(request, 'add_photo.html', {'form': form, 'estate': estate,
                                              'message': message, 'new_messages': new_messages})
