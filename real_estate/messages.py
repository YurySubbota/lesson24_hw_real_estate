from users.models import Profile
from real_estate.models import DealRequest


def new_message_count(request):
    try:
        users_profile = Profile.objects.get(user=request.user)
    except (TypeError, Profile.DoesNotExist):
        users_profile = None
    if users_profile:
        if users_profile.role == 'owner':
            new_messages = DealRequest.objects.filter(estate__owner=request.user, is_read=False).count()
            if new_messages >= 1:
                return new_messages
        elif users_profile.role == 'applicant':
            new_messages = DealRequest.objects.filter(buyer=request.user, is_read=False).count()
            if new_messages >= 1:
                return new_messages


def see_all_messages(request):
    try:
        users_profile = Profile.objects.get(user=request.user)
    except (TypeError, Profile.DoesNotExist):
        users_profile = None
    if users_profile:
        if users_profile.role == 'owner':
            return DealRequest.objects.filter(estate__owner=request.user).order_by('-created_at')
        if users_profile.role == 'applicant':
            return DealRequest.objects.filter(buyer=request.user).order_by('-created_at')
