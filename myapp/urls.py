from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),                
    path('catalogo/', views.catalogo, name='catalogo'),         
    #path('about.html', views.about, name='about_html'), 
    path('nosotros/', views.nosotros, name='nosotros'),
    #path('nosotros.html', views.nosotros, name='nosotros_html'),
    path('contacto/', views.contacto, name='contacto'),
    #path('contacto.html', views.contacto, name='contacto_html'),
    path('iniciar/', views.iniciar, name='iniciar'),
    #path('iniciarsecion.html', views.iniciarsecion, name='iniciarsecion_html'),
    path('registrar/', views.registrar, name='registrar'),
    #path('registrar.html', views.registrar, name='registrar_html'),
    #
    path('hello/<str:username>', views.hello, name="hello"),
    path('projects/', views.projects, name="projects"),
    path('projects/<int:id>', views.project_detail, name="project_detail"),
    path('tasks/', views.tasks, name="tasks"),
    path('create_task/', views.create_task, name="create_task"),
    path('create_project/', views.create_project, name="create_project"),
]