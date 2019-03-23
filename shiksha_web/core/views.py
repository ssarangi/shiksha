from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def index(request):
    print(request.user)
    return render(request, 'core/base.html', {})
