from django.shortcuts import render, redirect
from .form import GymMemberModel, GymMemberForm


# Create your views here.
def index(request):
    allEntries = GymMemberModel.objects.all()
    context = {
        "allEntries": allEntries
    }
    return render(request, 'BootCRUDApp/index.html', context)


def addMember(request):
    form = GymMemberForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("index")
    context = {
        "form": form
    }
    return render(request, "BootCRUDApp/addMember.html", context)
