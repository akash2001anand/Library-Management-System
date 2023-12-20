from django.urls import path
from . import views

urlpatterns=[
    path('books/',views.books,name='books'),
    path('add_bookpage/',views.add_bookpage,name='add_bookpage'),
    path('add_book/',views.add_book,name='add_book'),
    path('delete_book/',views.delete_book,name='delete_book'),
    path('delete_bookpage/',views.delete_bookpage,name='delete_bookpage'),
    
    path('members/',views.members,name='members'),
    path('add_member/',views.add_member,name='add_member'),
    path('add_memberpage/',views.add_memberpage,name='add_memberpage'),
    path('delete_member/',views.delete_member,name='delete_member'),
    path('delete_memberpage/',views.delete_memberpage,name='delete_memberpage'),
    path('admin_logout/',views.admin_logout,name='admin_logout'),
    # path('delete_member/',views.delete_member,name='delete_member'),
]