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

    context = { 'issue': issue }

    return render(request, 'newsletter/issue.html', context)


def createIssue(request):
    issue_form = IssueForm()
    summary_form = SummaryForm()

    if request.method == 'POST':
        issue_form = IssueForm(request.POST)
        summary_form = SummaryForm(request.POST)
        if issue_form.is_valid() and summary_form.is_valid():
            issue_form.save()
            summary_form.save()
            return redirect('/')

    context = { 'issue_form': issue_form, 'summary_form': summary_form }
    return render(request, 'newsletter/issue_form.html', context)


def podcast(request):
    episodes = Episode.objects.all()

    context = { 'episodes': episodes }

    return render(request, 'newsletter/podcast.html', context)


def episode(request, pk):
    episode = Episode.objects.get(id=pk)

    context = { 'episode': episode }

    return render(request, 'newsletter/episode.html', context)
