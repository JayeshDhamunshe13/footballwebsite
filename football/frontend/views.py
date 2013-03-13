import os
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from mako.lookup import TemplateLookup

from utils.utility import CSRF_Token
from frontend.models import Player, Coach

template_path = os.path.normpath(os.path.join(os.path.dirname(__file__),"../" "design/" "tpls/"))
tpl_lookup = TemplateLookup(directories=[template_path])

def home(request):
    """
    home page
    """
    if request.method == 'GET':
        tpl = tpl_lookup.get_template('home.mako')
        return HttpResponse(tpl.render(csrf_token=CSRF_Token(request)))

def register(request):
    """
    To register players & coach
    """
    if request.method == 'GET':
        tpl = tpl_lookup.get_template('register.mako')
        return HttpResponse(tpl.render(csrf_token=CSRF_Token(request)))

    elif request.method == 'POST':
        username = request.POST.get('username')
        age = request.POST.get('age')
        phoneno = request.POST.get('phoneno')
        address = request.POST.get('address')
        email = request.POST.get('email')
        status =request.POST.get('status')

        if status == "Player":
            player=Player()
            result = player.register(username, age, phoneno, address, email)
            return HttpResponse("Registraion Sucessfully")

        elif status == "Coach":
            coach=Coach()
            result = player.register(username, age, phoneno, address, email)
            return HttpResponse("Registraion Sucessfully")

        else:
            return HttpResponse('/')

    else:
        return HttpResponse('/')