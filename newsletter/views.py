from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *

# Create your views here.


def home(request):
    latest_issue = Issue.objects.latest('id')
    latest_issue_elements = latest_issue.elements.all().order_by('id')[:10]

    context = { 'latest_issue_elements': latest_issue_elements }

    return render(request, 'newsletter/dashboard.html', context)


def newsletter(request):
    issues = Issue.objects.all()
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
        element_form = ElementForm(request.POST, request.FILES)

    if element_form.is_valid():
        element = element_form.save(commit=False)
        element.issue = issue
        element_form.save()
        return redirect(f'/edit_issue/{ pk }')

    context = { 'issue': issue, 'element_form': element_form, 'elements': elements }

    return render(request, 'newsletter/issue_edit_form.html', context)


def deleteIssue(request, pk):
    issue = Issue.objects.get(id=pk)

    if request.method == "POST":
        issue.delete()
        return redirect('/newsletter')

    context = { 'issue': issue }

    return render(request, 'newsletter/issue_delete.html', context)



def podcast(request):
    episodes = Episode.objects.all()

    context = { 'episodes': episodes }

    return render(request, 'newsletter/podcast.html', context)


def episode(request, pk):
    episode = Episode.objects.get(id=pk)

    context = { 'episode': episode }

    return render(request, 'newsletter/episode.html', context)
