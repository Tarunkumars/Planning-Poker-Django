from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import RequestContext
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from PlanningPoker.forms import SignUpForm, GameForm
from PlanningPoker.models import Game


def index(request):
    template_name = 'PlanningPoker/index.html'
    return render(request, template_name)


def signup(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = SignUpForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass

            # Process the data in form.cleaned_data
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]

            # At this point, user is a User object that has already been saved
            # to the database. You can continue to change its attributes
            # if you want to change other fields.
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name

            # Save new user attributes
            user.save()

            return HttpResponseRedirect(reverse('gameList'))  # Redirect after POST
    else:
        form = SignUpForm()

    context = {
        'form': form,
    }
    template_name = 'PlanningPoker/signup.html'
    return render(request, template_name, context)


@login_required(login_url='/login')
def gameList(request):
    game_list = Game.objects.all().filter(Q(user=request.user) | Q(players__in=[request.user])).distinct()
    template_name = 'PlanningPoker/Game/list.html'

    context = {
        'game_list': game_list,
    }
    return render(request, template_name, context)


@login_required(login_url='/login')
def gameDetail(request, game_id):
    game = Game.objects.get(id=game_id)

    template_name = 'PlanningPoker/Game/detail.html'
    context = {
        'game': game,
    }
    return render(request, template_name, context)


@login_required(login_url='/login')
def gameAdd(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = GameForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass

            # Process the data in form.cleaned_data
            name = form.cleaned_data["name"]
            players = form.cleaned_data["players"]

            # Create, but don't save the new author instance.
            new_game = form.save(commit=False)

            # Modify the author in some way.
            new_game.user = request.user

            # Save the new instance.
            new_game.save()

            # Now, save the many-to-many data for the form.
            form.save_m2m()
            # At this point, user is a User object that has already been saved
            # to the database. You can continue to chang

            return HttpResponseRedirect(reverse('uStoriesAdd'))  # Redirect after POST
    else:
        form = GameForm()

    context = {
        'form': form,
    }
    template_name = 'PlanningPoker/Game/add.html'
    return render(request, template_name, context)


@login_required(login_url='/login')
def gameEdit(request, game_id):

    edited_game = Game.objects.get(id=game_id)

    if request.method == 'POST':  # If the form has been submitted...
        form = GameForm(request.POST, instance=edited_game)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass

            # Process the data in form.cleaned_data
            name = form.cleaned_data["name"]
            players = form.cleaned_data["players"]

            # Create, but don't save the new author instance.
            new_game = form.save(commit=False)

            # Modify the author in some way.
            new_game.user = request.user

            # Save the new instance.
            new_game.save()

            # Now, save the many-to-many data for the form.
            form.save_m2m()
            # At this point, user is a User object that has already been saved
            # to the database. You can continue to chang

            return HttpResponseRedirect(reverse('gameList'))  # Redirect after POST
    else:
        form = GameForm(instance=edited_game)

    context = {
        'form': form,
        'game': edited_game
    }
    template_name = 'PlanningPoker/Game/edit.html'
    return render(request, template_name, context)


@login_required(login_url='/login')
def deleteGame(request, game_id):
    Game.objects.get(id=game_id).delete()

    return HttpResponseRedirect(reverse('gameList'))
