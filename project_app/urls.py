from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    # path('uasertask/',views.UserTasksListCreate.as_view()),
    # path('usertask/<int:pk>/',views.UserTasksRetriveUpdateDestroy.as_view(),name='update')
    path('taskapi/',views.task_api),
    path('taskapi/<int:pk>/',views.task_api)

]