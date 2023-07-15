from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Contact, Book, Writer, Blog, Genre, About_us, Author, Topseller
from home import models
from django.contrib import messages
import random
from django.core.mail import send_mail
from .forms import EmailForm
import os 
from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.apps import apps



def index(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'index.html', context)


def about(request):
    about_uss = About_us.objects.all()
    return render(request, 'about.html', {'about_uss': about_uss})


def genre(request):
    genres= Genre.objects.all()
    return render(request, 'genre.html', {'genres': genres})
    
def blogs(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 4)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        # If the page is out of range, return the last page
        page_obj = paginator.page(paginator.num_pages)
    context = {'page_obj': page_obj}
    return render(request, 'blogs.html', context)

def newrelease(request):
    return render(request, 'newrelease.html')

def topsellers(request):
    topsellers = Topseller.objects.all()
    paginator = Paginator(topsellers, 6) 
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        # If the page is out of range, return the last page
        page_obj = paginator.page(paginator.num_pages)
    context = {'page_obj': page_obj}
    return render(request, 'topsellers.html', context)

def morewriters(request):
    writers = Writer.objects.all()
    paginator = Paginator(writers, 12)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj =  paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_page)
    context = {'page_obj': page_obj}
    return render(request, 'morewriters.html', context)

def writer_info(request, writer_id):
    writer = get_object_or_404(Writer, id=writer_id)
    writers = [writer]
    return render(request, 'writerinfo.html', {'writers':writers})

def author(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    authors = [author]

    return render(request, 'author_info.html', {'authors': authors})


def morerecomendation(request):
    book_list = Book.objects.all()
    paginator = Paginator(book_list, 3)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        # If the page is out of range, return the last page
        page_obj = paginator.page(paginator.num_pages)
    context = {'page_obj': page_obj}
    return render(request, 'morerec.html', context)


def blog_content(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    blogs = [blog] 
    return render(request, 'blog_content.html', {'blogs': blogs})


def genre_details(request, genre_id):
    genre = get_object_or_404(Genre, id=genre_id)
    genres = [genre] 
    return render(request, 'genre_detail.html', {'genres': genres})

def send_otp(email):
    otp = str(random.randint(100000, 999999))
    message = f"Your OTP to subcribe NIRVANA Newslatter is: {otp} Please do not share it with anyone."
    send_mail('NIRVANA OTP-', message, 'ddsingh332@gmail.com', [email])
    return otp

def subscribe(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid() and 'email' in form.cleaned_data:

            email = form.cleaned_data['email']
            otp = send_otp(email)  # Call the send_otp function to send OTP
            # Process the OTP or perform additional actions
            return render(request, 'verify_otp.html', {'email': email, 'otp': otp})
        else:
            # Form is not valid, handle the error
            return HttpResponse("Invalid form data")
    else:
        form = EmailForm()
    return render(request, 'subscribe.html', {'form': form})



def verify_otp(request):
    if request.method == 'POST':
        
        submitted_otp = request.POST.get('otp')
        expected_otp = request.POST.get('expected_otp')
        if submitted_otp == expected_otp:
            # OTP is valid
            return render(request, 'success.html')
        else:
            # OTP is invalid
            return render(request, 'error.html')
    else:
        # Handle other cases (GET request or unexpected scenarios)
        return HttpResponse('Bad Request')



def contact(request):
    if request.method == 'POST':
        # Handle form submission here
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        contact = Contact(name=name, email=email, message=message)
        contact.save()
        messages.success(request, "Message Sent! Thanks for contacting us.")
        
        # Redirect to the contact page
        return redirect('contact')
    
    # Render the contact form template
    return render(request, 'contact.html')




def download_pdf(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
        file_name = f"{book.title}.replace(' ', '_').lower().pdf"
        file_path = os.path.join('E:\BOOKS', file_name)

        if os.path.exists(file_path):
            with open(file_path, 'rb') as file:
                file_content = file.read()

            response = HttpResponse(file_content, content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{file_name}"'
            return response
        else:
            return HttpResponse('File not found.')
    except Book.DoesNotExist:
        return HttpResponse('Book not found.')
    
def first_three(request):
    return HttpResponse('Book is not avialable right now!')
   
    


    


def download_ebook(request, book_id):
    if request.method == 'GET':
        return HttpResponse('Book is not avialable right now!')
    






def search(request):
        query = request.GET.get('query')
        allresults = Book.objects.filter(title__icontains=query)
        params = {'allresults' : allresults}
        return render(request, 'search.html', params)
  


    




