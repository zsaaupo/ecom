from django.shortcuts import render

def landin_page(request):
    return render(request, "index.html")