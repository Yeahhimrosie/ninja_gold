from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('reset', views.reset),
    path('gold', views.process_gold)
]




# from django.urls import path
# from . import views
# urlpatterns = [
#     path('', views.index),
#     path('process', views.process),
#     path('reset', views.reset),
# ]
