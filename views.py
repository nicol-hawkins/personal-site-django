import requests
from django.http import HttpResponse
from django.shortcuts import render



def blog(request):
    blog_html = open("templates/blog.html").read()
    context = {
        'title': 'Blog',
        'content': blog_html,
    }
    return render(request, 'base.html', context)
    



def about_me(request):
    about_html = open("templates/about.html").read()
    context = {
        'title': 'About',
        'content': about_html,
    }
    return render(request, 'base.html', context)


def resume(request):
    resume_html = open("templates/resume.html").read()
    context = {
        'title': 'Resume',
        'content': resume_html,
    }
    return render(request, 'base.html', context)



def git_api(request):
    response = requests.get('https://api.github.com/users/nicol-hawkins/repos')
    repos = response.json()
    context = {
        'github_repos': repos,
    }
    return render(request, 'github.html', context)




