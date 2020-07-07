from django.urls import path,include
from . import views 
from home.dash_apps.finished_apps import app1,app2,app3
#from home.dash_apps.finished_apps import simpleexample
urlpatterns=[
    path('home/',views.home,name='home'),
    path('charts/',views.charts,name='charts'),
    #path('plots/',views.plotreq,name='plotreq')
    path('graphs/',views.graphView,name='graphview'),
    path('home/page<int:num>',views.getListValues,name='listvals'),
    path('bubbles/',views.bubbleView,name='bubbles'),
    path('topic_bubble/',views.getCharts,name='chart')
]