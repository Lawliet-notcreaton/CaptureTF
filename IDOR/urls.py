from django.urls import path
from IDOR.views import *
from . import views
urlpatterns = [
    path('', lesson1),
    path('tickets.php', createticket),
    path('ticket/<int:id>/', views.ticket, name='ticket_detail'),
    path('ticket/<int:pk>/delete/', views.DeleteItemView.as_view(), name='delete_ticket'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', views.register, name='register'),
    path('logout/', logout_user, name='logout'),
]