from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . models import ToDoList, Item, Note
from . forms import CreateNewList, CreateNewNote
# Create your views here.

def viewlist(response, id):
    ls = ToDoList.objects.get(id=id)
    if response.method == "POST":
        print(response.POST)
        for item in ls.item_set.all():
            if response.POST.get("d"+str(item.id)) == "delete":
                print("to delete:",str(item.id),str(item.text))
                item.delete()
                ls.save()
        
        if response.POST.get("save"):
            for item in ls.item_set.all():
                if response.POST.get("c"+str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False
                    
                item.text = response.POST.get("item-text"+str(item.id))
                item.save()
            
        elif response.POST.get("newItem"):
            txt = response.POST.get("new")            
            if len(txt) > 2:
                ls.item_set.create(text=txt, complete=False)
            else:
                print("invalid")
            
    return render(response, "main/viewlist.html",{"ls":ls})

def home(response):
    #return HttpResponse("<h1>this is the home page</h1>"
    return render(response,"main/home.html",{"name":"test"})

def createlist(response):
    if response.method == "POST":
        print(response.POST)
        form = CreateNewList(response.POST)        
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            
        return HttpResponseRedirect("/list%i/" %t.id)
    else:
        form = CreateNewList()
    return render(response,"main/createlist.html",{"form":form})

def createnote(response):
    if response.method == "POST":
        print(response.POST)
        form = CreateNewNote(response.POST)
        if form.is_valid():
            print("in form valid")
            nobj = Note(notetext="", notetitle= form.cleaned_data["notetitle"])
            nobj.save()                
            return HttpResponseRedirect("/note%i/" %nobj.id)
    else:
        form = CreateNewNote()
    return render(response,"main/createnote.html",{"form":form})

def viewnote(response, id):
    nobj = Note.objects.get(id=id)
    if response.method == "POST":
        print(response.POST)        
        if response.POST.get("save"):
            nobj.notetext = response.POST.get("note-text"+str(nobj.id))
            nobj.save()
            
        if response.POST.get("d"+str(nobj.id)) == "delete":
            print("delete item",nobj.notetitle)
            nobj.delete()
            return HttpResponseRedirect("/home/")
                         
    return render(response, "main/viewnote.html",{"nobj":nobj})
