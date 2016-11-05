"""PlanningPokerDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from PlanningPoker import views
from django.contrib import admin
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', views.index, name='index'),

    url(r'^signup$', views.signup, name='signup'),
    url(r'^login$', login, {'template_name': 'PlanningPoker/login.html', }, name="login"),
    url(r'^logout$', logout, {'template_name': 'PlanningPoker/index.html', }, name="logout"),

    url(r'^games$', views.gameList, name='gameList'),
    url(r'^games/add$', views.gameAdd, name='gameAdd'),
    url(r'^games/(?P<game_id>[0-9]+)$', views.gameDetail, name='gameDetail'),
    url(r'^games/(?P<game_id>[0-9]+)/edit$', views.gameEdit, name='gameEdit'),
    url(r'^games/(?P<game_id>[0-9]+)/delete$', views.deleteGame, name='deleteGame'),
]




