from django.shortcuts import render, redirect
from note.models import *

def index(request):
    return render(request, "index.html")

def notepad(request):
    name = request.POST.get("name")
    id = request.POST.get("id")
    user_dict = {"name":name, "id":id}
    if request.POST.get("log"):
        obj = User.objects.create(user_name = name, user_id = id)
        obj.save()
        print(obj.user_id)
        return render(request, "notepad.html", user_dict)
    elif name == None:
        obj = User.objects.get(user_id = id)
        nam = obj.user_name
        return render(request, "notepad.html", {"name":nam, "id":id})
    elif User.objects.get(user_id = id, user_name = name):
        return render(request, "notepad.html", user_dict)
    else:
        return render(request, "error.html")


def save(request):
    name = request.POST.get("name")
    id = request.POST.get("id")
    user_notes = request.POST.get("notes")
    user_title = request.POST.get("note_title")

    user_dict = {"name":name, "id":id}

    obj1 = User.objects.get(user_id=id)
    user_notes = user_notes.replace('\n', '<br>')
    obj2 = Notes.objects.create(user_id = id, user_notes_title = user_title, user_notes = user_notes)
    obj2.save()
    obj1.save()
    
    return render(request, "notepad.html", user_dict)

def delete(request):
    title = request.POST.get("title")
    ob1 = Notes.objects.filter(user_notes_title = title)
    ob1.delete()
    return diary(request)

def update(request):
    return notepad(request)

def diary(request):
    id = request.POST.get("id")
    name = request.POST.get("name")
    obj = Notes.objects.filter(user_id=id)
    # for ob in obj:
    #     print("here ", ob.user_notes)
    return render(request, "diary.html", {"notes":obj, "id":id, "name":name})

def note_(request):
    title = request.POST.get("note_title")
    note = request.POST.get("note_")
    #print(title, note)
    user_dict = {"title":title, "notes":note}
    return render(request, "user_note.html", user_dict)

def sign_in(request):
    return render(request, "sign_in.html")


