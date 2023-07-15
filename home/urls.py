from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('genre', views.genre, name='genre'),
    path('contact', views.contact, name='contact'),
    path('blogs', views.blogs, name='blogs'),
    path('newrelease', views.newrelease, name='newrelease'),
    path('topsellers', views.topsellers, name='topsellers'),
    path('morewriter', views.morewriters, name='morewriters'),
    path('morerecomendation', views.morerecomendation, name='morerecomendation'),
    path('blogs/<int:blog_id>/content', views.blog_content, name='blog_content'),
    path('genres/<int:genre_id>/details', views.genre_details, name='genre_details'),
    path('subscribe', views.subscribe, name='subscribe'),
    path('verify-otp/', views.verify_otp, name='verify_otp'),
    path('download/<int:book_id>/pdf', views.download_pdf, name='download_pdf'),
    path('download/<int:book_id>/ebook', views.download_ebook, name='download_ebook'),
    path('first_three', views.first_three, name='first_three'),
    path('search', views.search, name='search'),
    path('writer/<int:writer_id>/info', views.writer_info, name='writerinfo'),
    path('author/<int:author_id>/', views.author, name='author')

]



