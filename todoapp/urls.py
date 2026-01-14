# from django.urls import path
# from.import views

# urlpatterns = [

#     # add task
#     path('addTask/',views.addTask, name = 'addTask'),
#     # mark as done
#     path('mark_as_done/<int:pk>/',views.mark_as_done,name = "mark_as_done"),
#     # mark as undone
#     path('mark_as_UnDone/<int:pk>/',views.mark_as_UnDone,name ='mark_as_UnDone'),
# #    delete task for add_task section
#     path('delete_task/<int:pk>/',views.delete_task,name ='delete_task'),
#     # delete task for completedt_ask section
#     path('delete_UnDone_task/<int:pk>/',views.delete_UnDone_task,name ='delete_UnDone_task'),
#     # edit task
#     path('edit_task/<int:pk>/',views.edit_task,name ='edit_task'),

#     # authentication_urls
#      path('register/', views.register_view, name='register'),
#      path('login/', views.login_view, name='login'),
#      path('logout/', views.logout_view, name='logout'),

#      path('todo', views.home, name='home'),


# ]

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('add/', views.addTask, name='addTask'),
#     path('done/<int:pk>/', views.mark_as_done, name='mark_as_done'),
#     path('undone/<int:pk>/', views.mark_as_UnDone, name='mark_as_UnDone'),
#     path('delete/<int:pk>/', views.delete_task, name='delete_task'),
#     path('edit/<int:pk>/', views.edit_task, name='edit_task'),

#     path('register/', views.register_view, name='register'),
#     path('login/', views.login_view, name='login'),
#     path('logout/', views.logout_view, name='logout'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home),

    path('add/', views.addTask, name='addTask'),
    path('done/<int:pk>/', views.mark_as_done, name='mark_as_done'),
    path('undone/<int:pk>/', views.mark_as_UnDone, name='mark_as_UnDone'),
    path('delete/<int:pk>/', views.delete_task, name='delete_task'),
    path('edit/<int:pk>/', views.edit_task, name='edit_task'),
    path('delete-undone/<int:pk>/',views.delete_UnDone_task, name='delete_UnDone_task'
),

    

    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
