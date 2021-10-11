from django.shortcuts import render,redirect
from .forms import EntryForm
from django.utils import timezone
import datetime
from .models import NewEntry, User ,Socials
from django.http import Http404,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.views.generic import ListView
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.

def login(request):
	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']
		check_user = User.objects.filter(email = email)
		check_user_pass = User.objects.filter(password = password)

		valid_user = (len(list(check_user)) == 1)
		if (valid_user):
			current_user = email
			user_name = check_user.first().username
			request.session['current_user'] = current_user
			request.session['user_name'] = user_name
			#encoded = jwt.encode(payload, secret, algorithm='HS256')
			return redirect( 'home')
		else:
			return render(request, 'Mydiary/login.html', {})
	else:
		return render(request, 'Mydiary/login.html')


def signup(request):
	if request.method == 'POST':
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		print(request.POST)
		existing_email = User.objects.filter(email = email)
		is_new_user = (len(list(existing_email)) == 0)
		print(is_new_user)
		if (is_new_user):
			new_user = User.objects.create(username=username, email=email, password=password)
			new_user.save()
			return redirect('login')
		else:
			return render(request, 'Mydiary/signup.html', {})
	else:
		return render(request, 'Mydiary/signup.html')


def logout(request):
	#clear session
	try:
		del request.session['current_user']
		del request.session['user_name']
	except KeyError:
		pass
	return render(request, 'Mydiary/landing.html')

    
		
        	

    


def home(request):
	entries =NewEntry.objects.filter(date__lte=timezone.now()).order_by('-date')
	return render(request, 'Mydiary/home.html', {'entries':entries}) 

@login_required
def settings(request):
	if request.method == "POST" :
		bio = request.POST['bio']
		current_user = request.session['user_name']
		linkedin = request.POST['linkedin']
		twitter = request.POST['twitter']
		facebook = request.POST['facebook']
		instagram = request.POST['instagram']
		biolink= Socials.objects.create(username=current_user,bio=bio,linkedin=linkedin,twitter=twitter,facebook=facebook,instagram=instagram)
		biolink.save()
		

	return render(request, 'Mydiary/settings.html', {}) 

@login_required
def profile(request):
	current_user = request.session['user_name']
	biolinks = [Socials.objects.filter(username = current_user,date__lte=timezone.now()).last()]
	users=User.objects.filter(username=current_user)
	entries =NewEntry.objects.filter(username = current_user,date__lte=timezone.now()).order_by('-date')
	
	context = { 'entries' : entries,
	             'users':users,
	          'biolinks':biolinks
	 }
	return render(request, 'Mydiary/profile.html', context)			
	
@login_required
def search(request):
	if request.method == 'GET':
		query = request.GET.get('q')
		object_list = NewEntry.objects.filter(Q(Topic__icontains=query) | Q(TodaysEntry__icontains=query) |Q(date__icontains=query))
		return render(request,'Mydiary/search.html',{"entry":object_list})
	else:
		return render(request,'Mydiary/search.html',{})

@login_required
def newentry(request):
	if request.method == "POST" :
		Topic = request.POST['Topic']
		TodaysEntry = request.POST['TodaysEntry'] 
		current_user = request.session['user_name']
		entry = NewEntry.objects.create(Topic=Topic, TodaysEntry=TodaysEntry,username=current_user)
		entry.date = timezone.now()
		entry.save()

		return redirect ('viewentry')
	else:
			return render(request, 'Mydiary/newentry.html')

@login_required
def viewentry(request):
	current_user = request.session['user_name']
	entries =NewEntry.objects.filter(username = current_user,date__lte=timezone.now()).order_by('-date')
	return render(request, 'Mydiary/viewentry.html', {'entries':entries})


@login_required
def landing(request):
	return render(request, 'Mydiary/landing.html', {})
