from django.shortcuts import render
from django.http import HttpResponse
from second_app.models import Users
# Create your views here.
def index(request):
    return render(request, 'second_app/index.html')
    

def user(request):
    users_list = Users.objects.order_by('first_name')
    user_dict = {'users': users_list}
    return render(request, 'second_app/user.html', context=user_dict)
