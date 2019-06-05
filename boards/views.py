from django.shortcuts import render, redirect
from .models import Board
# Create your views here.
def index(request):
    boards = Board.objects.all()
    context = {'boards': boards}
    return render(request, 'boards/index.html', context)


def new(request):
    return render(request, 'boards/new.html')


def create(request):
    # new 에서 넘어오는 제목과 내용을 저장
    # create.html 페이지를 render
    title = request.POST.get('title') # 글 제목
    content = request.POST.get('content') # 글 내용

    # orm - title 과 content 에 위에서 넘어온 값을 할당
    # 1
    # board = Board()
    # board.title = title
    # board.content = content
    # # db 에 저장
    # board.save()

    # 2
    board = Board(title=title, content=content)
    board.save()
    # Board.objects.create(title=title, content=content)

    return redirect(f'/boards/{board.pk}/')


def detail(request, pk):
    # 요청으로 들어온 pk 값으로 해당 글을 찾아옴
    board = Board.objects.get(pk=pk)
    context = {'board': board,}
    return render(request, 'boards/detail.html', context)
