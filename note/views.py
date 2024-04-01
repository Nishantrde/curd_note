from django.shortcuts import render, redirect, HttpResponse
from note.models import *
from django.contrib.auth.models import User
from django.contrib import messages
import uuid
from django.contrib.auth import authenticate, login, logout
from .utils import * 
from django.contrib.auth.decorators import login_required

@login_required(login_url="/")
def login_page(request):
    if request.method == "POST":
        first_name = request.POST.get('First_name')
        last_name = request.POST.get('Last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        user = User.objects.filter(username = username)

        if user.exists():
            messages.info(request, 'Username alredy taken')
            return redirect('/login')
         
        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username
        )

        user.set_password(password)
        user.save()
        p_obj = UserProfile.objects.create(
                user = user,
                email_token = str(uuid.uuid4())
            )

        send_email_token(email, p_obj.email_token)
        
        return HttpResponse("We have send aN Email lol.....")
    return render(request, "index.html")

def notepad(request):
    name = request.POST.get("username")

    return render(request, "notepad.html", {"name":name})
    
    # user_dict = {"name":username, "id":id, "title":None, "notes":None}
        
    # else:
    #     return render(request, "error.html")


def save(request):
    username = request.POST.get("name")
    user_notes = request.POST.get("notes")
    user_title = request.POST.get("note_title")
    prv_title = request.POST.get("prv_title")

    user_dict = {"name":username,"prv_title":user_title, "title":user_title, "notes":user_notes}

    user_notes = user_notes.replace('\n', '<br>')
    
    if request.POST.get("msg") == "update":
        print(request.POST.get("msg"))
        user_dict["msg"] = "update"
        Notes.objects.filter(user_notes_title = prv_title, profile_name = username).update(profile_name = username, user_notes_title = user_title, user_notes = user_notes)
        return render(request, "notepad.html", user_dict)
    else:
        obj2 = Notes.objects.create(profile_name = username, user_notes_title = user_title, user_notes = user_notes)
        obj2.save()
        return render(request, "notepad.html", {"name" : username})
    

def delete(request):
    title = request.POST.get("title")
    ob1 = Notes.objects.filter(user_notes_title = title)
    ob1.delete()
    return diary(request)

def update(request):
    username = request.POST.get("name")
    title = request.POST.get("title")
    notes = request.POST.get("notes")
    print("lol_ok")
    return render(request, "notepad.html", {"name":username,"prv_title":title, "title":title, "notes":notes, "msg":"update"})

def diary(request):
    name = request.POST.get("name")
    obj = Notes.objects.filter(profile_name=name)
    # for ob in obj:
    #     print("here ", ob.user_notes)
    return render(request, "diary.html", {"notes":obj, "id":id, "name":name})

def note_(request):
    title = request.POST.get("note_title")
    note = request.POST.get("note_")
    #print(title, note)
    user_dict = {"title":title, "notes":note}
    return render(request, "user_note.html", user_dict)

def log_out(request):
    logout(request)
    return redirect('/')

def verify(request, token):
    try:
        obj = UserProfile.objects.get(email_token = token)
        obj.is_verified = True
        obj.save()
        print(token)
        return render(request, "sign_in.html")
    except Exception as e:
        return 

def sign_in(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not User.objects.filter(username = username).exists():
            messages.error(request, 'Invalid Username')
            return redirect("/")
        user = authenticate(username = username, password = password)

        if user is None:
            messages.error(request, "Invalid password")
            return redirect("/")

        else:

            login(request, user)
            return render(request, "notepad.html", {"name" : username})
    
    return render(request, "sign_in.html")


