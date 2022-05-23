from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Boards , Topics , Post
from django.contrib.auth.models import User
from .forms import NewTopicForm
# Create your views here.
def home(request):
    boards = Boards.objects.all()
    return render(request,'home.html',{'boards':boards})
def board_topic(request,boardid):

    board = get_object_or_404(Boards,pk=boardid)
    return render(request,'topics.html',{'board':board})
def new_topic(request,boardid):
    board = Boards.objects.get(pk=boardid)
    #board = get_object_or_404(Boards,pk=board_id)
    form = NewTopicForm()
    user = User.objects.first()
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.creata_by  = user
            topic.save()
            print(topic)
            post = Post(
                message = form.cleaned_data.get('message'),
                posted_by = user,
                topic = topic
            )
            post.save()
            print(post)
            return redirect('board_topic',boardid = board.pk)
        else :
            form = NewTopicForm()
    return render(request,'new_topics.html',{'board':board,'form':form})
