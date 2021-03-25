from django.http import HttpResponse

from .models import User


def index(request):
    all_users = list(User.objects.all())
    return HttpResponse(" ".join(map(str, all_users)))
