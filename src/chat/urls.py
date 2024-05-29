from django.urls import path
from chat.views import chat_view
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("", chat_view, name="chat_view"),

    # Authentication routing
    path("auth/login/", LoginView.as_view(template_name="chat/login.html"), name="Login"),
    path("auth/logout/", LogoutView.as_view(template_name="chat/logout.html"), name="Logout"),

]
