from django.contrib import admin
from django.urls import path
from app.views import home, sistemas, get_live_data, ia, grafico, ask_gemini, perfil, toggle_ev_charger, sus, \
    remove_button

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('ia/', ia, name='ia'),
    path('grafico/', grafico, name='grafico'),
    path('perfil/', perfil, name='perfil'),
    path('api/live-data/', get_live_data, name='live_data'),
    path('api/ask-gemini/', ask_gemini, name='ask_gemini'),
    path('api/toggle-ev-charger/', toggle_ev_charger, name='toggle_ev_charger'),
    path('sus/',sus,name='sus'),
    path('sistemas/',sistemas,name='sistemas'),
    path('remove_button/',remove_button,name='remove_button')
]