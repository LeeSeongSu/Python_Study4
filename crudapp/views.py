from django.shortcuts import render,redirect
from .models import Post
from .forms import CreateForm

# Create your views here.
def home(request):
    posts = Post.objects
    return render(request,'crudapp/home.html', {'posts':posts})

def create(request):
    if request.method == 'POST':
       form = CreateForm(request.POST)
       if form.is_valid():
           form = form.save(commit=False)
           form.author = request.user
           form.save()
           return redirect('home')
    else:
        form = CreateForm()
        return render(request, 'crudapp/new.html', {'form':form})
    