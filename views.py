import requests
from django.http import HttpResponse
from django.shortcuts import render


def blog(request):
    context = {}
    return render(request, 'blog.html', context)
    

def resume(request):
    context = {}
    return render(request, 'resume.html', context)


def about_me(request):
    context = {}
    return render(request, 'about.html', context)


def git_api(request):
    response = requests.get('https://api.github.com/users/nicol-hawkins/repos')
    repos = response.json()
    context = {
        'github_repos': repos,
    }
    return render(request, 'github.html', context)




