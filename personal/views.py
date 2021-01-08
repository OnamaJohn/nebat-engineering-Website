from django.shortcuts import render
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
# from django.core.mail import send_mail

# from django.core.mail import EmailMultiAlternatives
# from django.utils.html import strip_tags

from . models import (
	Achievement,
	Partners,
	Header,
	AboutStatement,
	Values,
	Service,
	Project,
	Testimonial,
	Team,
)

def home_screen_views(request, *args, **kwargs):
	achvs = Achievement.objects.all()
	partners = Partners.objects.all()
	headers = Header.objects.all()
	abouts = AboutStatement.objects.all()
	values = Values.objects.all()
	services = Service.objects.all()
	projects = Project.objects.all()
	testimonials = Testimonial.objects.all()
	teams = Team.objects.all()
	context = {
		'achvs':achvs, 
		'partners':partners,
		'headers':headers,
		"abouts":abouts,
		"values":values,
		"services":services,
		"projects":projects,
		"testimonials":testimonials,
		"teams":teams,
	}
	return render(request, "personal/home.html", context)

def sendEmail(request):
	if request.method == 'POST':
		template = render_to_string('personal/home.html',
			{
				'subject':request.POST['subject'],
				'name':request.POST['name'],
				'email':request.POST['email'],
				'message':request.POST['message'],
			})
		
		email = EmailMessage(
			request.POST['subject'],
			template,
			settings.EMAIL_HOST_USER,
			['bukenyalukman@gmail.com'],
		)
		email.fail_silently=False
		email.send()
	return HttpResponse('Email was sent')