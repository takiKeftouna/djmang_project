from boards import views
from django.urls import path
urlpatterns = [
    path('',views.home,name='index'),
    path('boards/<int:boardid>/',views.board_topic,name='board_topic'),
    path('boards/<int:boardid>/add/',views.new_topic,name='new_topic')
]