from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *

# Create your views here.


def home(request):
    return render(request, 'newsletter/dashboard.html')


def newsletter(request):
    issues = Issue.objects.all()

    context = { 'issues': issues }

    return render(request, 'newsletter/newsletter.html', context)


def issue(request, pk):
    issue = Issue.objects.get(id=pk)
    elements = issue.elements.all()
    print(elements)

    context = { 'issue': issue, 'elements': elements }

    return render(request, 'newsletter/issue.html', context)


def createIssue(request):
    element_form = ElementForm()

    if request.method == 'POST':
        element_form = ElementForm(request.POST)

        if element_form.is_valid():
            issue = Issue()
            issue.save()
            element = element_form.save(commit=False)
            element.issue = issue
            element_form.save()
            return redirect('/')

    context = { 'element_form': element_form }

    return render(request, 'newsletter/issue_form.html', context)


def podcast(request):
    episodes = Episode.objects.all()

    context = { 'episodes': episodes }

    return render(request, 'newsletter/podcast.html', context)


def episode(request, pk):
    episode = Episode.objects.get(id=pk)

    context = { 'episode': episode }

    return render(request, 'newsletter/episode.html', context)
