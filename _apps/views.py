from django.shortcuts import render
# Create your views here.
def login(request):
    # books = Buku.objects.all()
    # # books = Buku.objects.filter(kelompok__nama='Shounen')[:3]
    # data = {
    #     'books': books
    # }
    return render(request, 'login.html')
