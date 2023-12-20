from django.shortcuts import render,redirect
from django.contrib.auth import logout
from .models import *
# Create your views here.
def books(request):
    books = Book.objects.all()   
    return render(request,'books.html',{'books':books})

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
    return redirect('books')

def delete_bookpage(request):
    return render(request,'delete_book.html')

def delete_book(request):
    if request.method=='POST':
        name = request.POST.get('name')
        Book.objects.filter(book_title = name).delete()
        
    return redirect('books')


def add_member(request):
    if request.method=='POST':
        name = request.POST.get('name')
        mobno = request.POST.get('mobno')
        email = request.POST.get('email')
        
        m = Member(name=name,mobno=mobno,email=email)
        m.save()
    return redirect('members')

def add_memberpage(request):
    return render(request,'add_member.html')

def delete_memberpage(request):
    return render(request,'delete_member.html')

def delete_member(request):
    if request.method=='POST':
        name = request.POST.get('name')
        Member.objects.filter(name = name).delete()
        
    return redirect('members')

def admin_logout(request):
    logout(request)
    return redirect('index')
