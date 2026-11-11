from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import StudentForm
from .models import Student

# Create your views here.
def Index(request):
    return redirect("home")


def Homepage(request):
    return render(request, "index.html", {"form": StudentForm()})

def Aboutpage(request):
    return render(request,"about.html")

def Servicepage(request):
    return render(request,"service.html")

def Contactpage(request):
    return render(request,"contact.html")

def Studentpage(request):
    form = StudentForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Student added successfully.")
        return redirect("students")
    return render(request, "studentpage/add.html", {"form": form, "is_edit": False})


def Studentlist(request):
    students = Student.objects.order_by("name", "id")
    return render(request, "studentpage/list.html", {"students": students})


def Studentedit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST or None, instance=student)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Student updated successfully.")
        return redirect("students")
    return render(
        request,
        "studentpage/add.html",
        {"form": form, "is_edit": True, "student": student},
    )


@require_POST
def Studentdelete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    messages.success(request, "Student deleted successfully.")
    return redirect("students")