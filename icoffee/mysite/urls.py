from django.urls import path
from . import views

urlpatterns = [
    path('', views.wow, name='wow'),
    path('instagram', views.instagram, name='instagram'),
    path('mercadolibre', views.mercadolibre, name='mercadolibre'),
    path('facebook', views.facebook, name='facebook'),
    path('pagamenos', views.pagamenos, name='pagamenos'),
    path('wow', views.wow, name='wow')
]
