from django.shortcuts import render, redirect

def chat_view(request, *args, **kwargs):
    if request.user.is_authenticated:
        return redirect("login-user")
    context ={}
    return render(request, "chat/chat_page.html", context=context)
