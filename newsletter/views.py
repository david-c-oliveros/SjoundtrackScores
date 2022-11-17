from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from .models import *
from .forms import *
from .decorators import unauthenticated_user, allowed_users


# Create your views here.


@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            user = form .cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)

            return redirect('login')

    context = { 'form': form }
    return render(request, 'newsletter/register.html', context)


@unauthenticated_user
def loginPage(request):
    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as { username }.")
                return redirect("home")

            else:
                messages.error(request, "Invalid username or password.")

        else:
            messages.error(request, "Invalid username or password.")

    context = { 'form': form}
    return render(request, 'newsletter/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')

def home(request):
    latest_issue = Issue.objects.latest('id')
    latest_issue_elements = latest_issue.elements.all().order_by('id')[:10]

    context = { 'latest_issue_elements': latest_issue_elements }

    return render(request, 'newsletter/dashboard.html', context)


def userPage(request):
    context = {}
    return render(request, 'newsletter/user.html', context)


def newsletter(request):
    issues = Issue.objects.all()
    issue_contents = []

    for i in range(len(issues)):
        issue_contents.append([issues[i], issues[i].elements.all()])

    context = { 'issues': issue_contents }

    return render(request, 'newsletter/newsletter.html', context)


@allowed_users(allowed_roles=['admin'])
def issueAdmin(request, pk):
    issue = Issue.objects.get(id=pk)
    elements = issue.elements.all()

    context = { 'issue': issue, 'elements': elements }

    return render(request, 'newsletter/issue_admin.html', context)


def issue(request, pk):
    issue = Issue.objects.get(id=pk)
    elements = issue.elements.all()

    context = { 'issue': issue, 'elements': elements }

    return render(request, 'newsletter/issue.html', context)


@login_required(login_url='home')
@allowed_users(allowed_roles=['admin'])
def createIssue(request):

    issue = Issue()
    issue.save()
    return redirect(f'/edit_issue/{ issue.id }')


@login_required(login_url='home')
@allowed_users(allowed_roles=['admin'])
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


@login_required(login_url='home')
@allowed_users(allowed_roles=['admin'])
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
    videos = episode.videos.all()

    context = { 'episode': episode, 'videos': videos }

    return render(request, 'newsletter/episode.html', context)
