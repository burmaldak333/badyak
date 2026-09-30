from django.contrib import admin
from django.urls import path
from main.views import gender_view, name_view, result_view, reset_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', gender_view, name='gender'),      # ← вот это важно
    path('name/', name_view, name='name'),
    path('result/', result_view, name='result'),
    path('reset/', reset_view, name='reset'),
]