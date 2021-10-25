"""dom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

# Проектът няма апове, само главна директория - това нe e проблем в този случай, но ако проектът беше мащабен
# би било много по-практично да се използват отделни апове, които позволяват за по-подредена структура на проекта
# и предпазват от конфликти, ако проектът е колаборативен. Освен това всеки ап си има собствени миграции и urls.
# Когато сайта се отвори на начален адрес http://127.0.0.1:8000/, първото нещо, което виждам е Page not found.
# Бих препоръчал да се смени на path('', views.home), за да може първо да се види таблото.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.home),
]
