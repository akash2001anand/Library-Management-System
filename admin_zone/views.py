from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib import messages
from .models import *
# Create your views here.

def admin_home(request):
    Books = Book.objects.all()
    return render(request, 'admin_home.html',{'Books':Books})

def books(request):
    Books = Book.objects.all()   
    return render(request,'books.html',{'Books':Books})

def members(request):
    members = Member.objects.all()   
    return render(request,'members.html',{'members':members})

def add_bookpage(request):
    return render(request,'add_book.html')

def add_book(request):
    if request.method=='POST':
        name = request.POST.get('name')
        author = request.POST.get('author')
        pages = request.POST.get('pages')        
        b = Book(book_title=name,book_author=author,book_pages=pages)
        b.save()
        messages.success(request, 'Book Added Successfully!!!')
    return redirect('books')

def delete_bookpage(request):
    return render(request,'delete_book.html')

def delete_book(request):
    try:
        if request.method=='POST':
            id = request.POST.get('id')
            Book.objects.get(id = id).delete()
            messages.success(request, 'Book Deleted Successfully!!!')
    except Book.DoesNotExist:
            messages.error(request, 'No data Found!!!')
            return redirect('delete_bookpage')
        
    return redirect('books')


def add_member(request):
    if request.method=='POST':
        name = request.POST.get('name')
        mobno = request.POST.get('mobno')
        email = request.POST.get('email')       
        m = Member(name=name,mobno=mobno,email=email)
        m.save()
        messages.success(request, 'Member Added Successfully!!!')
    return redirect('members')

def add_memberpage(request):
    return render(request,'add_member.html')

def delete_memberpage(request):
    return render(request, 'delete_member.html')

def delete_member(request):
    if request.method == 'POST':
        try:
            id = request.POST.get('id')
            Member.objects.get(id=id).delete()
            messages.success(request, 'Member Deleted Successfully!!!')
        except Member.DoesNotExist:
            messages.error(request, 'No data Found!!!')
            return redirect('delete_memberpage')

    return redirect('members')


def admin_logout(request):
    logout(request)
    messages.success(request, 'Logout Successfully!!!')
    return redirect('index')
