from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *

# Create your views here.


def home(request):
    return render(request, 'newsletter/dashboard.html')


def newsletter(request):
    issues = Issue.objects.all()
    element_sets = []
    issue_contents = []

    for i in range(len(issues)):
        issue_contents.append([issues[i], issues[i].elements.all()])

    context = { 'issues': issue_contents }

    return render(request, 'newsletter/newsletter.html', context)


def issue(request, pk):
    issue = Issue.objects.get(id=pk)
    elements = issue.elements.all()

    context = { 'issue': issue, 'elements': elements }

    return render(request, 'newsletter/issue.html', context)


def createIssue(request):

    issue = Issue()
    issue.save()
    return redirect(f'/edit_issue/{ issue.id }')


def editIssue(request, pk):
    issue = Issue.objects.get(id=pk)
    elements = issue.elements.all()
    element_form = ElementForm()

    if request.method == 'POST':
        element_form = ElementForm(request.POST)

    if element_form.is_valid():
        print('valid')
        element = element_form.save(commit=False)
        element.issue = issue
        element_form.save()
        print('redirecting')
        return redirect(f'/edit_issue/{ pk }')

    context = { 'issue': issue, 'element_form': element_form, 'elements': elements }

    return render(request, 'newsletter/issue_edit_form.html', context)



def podcast(request):
    episodes = Episode.objects.all()

    context = { 'episodes': episodes }

    return render(request, 'newsletter/podcast.html', context)


def episode(request, pk):
    episode = Episode.objects.get(id=pk)

    context = { 'episode': episode }

    return render(request, 'newsletter/episode.html', context)
