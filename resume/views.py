from django.shortcuts import render
from django.http import JsonResponse
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError

# Create your views here.

# Returns Resume
def index(request):
    form = ContactForm()
    return render(request, "resume/index.html", {'form':form})


# Processes the conract form
def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = "Contact Me Copy From Delight"
			full_name = form.cleaned_data['full_name']
			email = form.cleaned_data['email_address']
			message_body = form.cleaned_data['message']
			message = f"Fullname: {full_name}\n Email: {email} \n Message: {message_body}"

			try:
				send_mail(subject, message, 'dfelastevetest@gmail.com', ['dfelastevetest@gmail.com', form.cleaned_data['email_address']]) 
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
            # Redirects to Success Page on Message sent successfully
			return render (request, "resume/success.html", {'name':full_name})
      
	form = ContactForm()
	return render(request, "resume/index.html", {'form':form})


def success(request):
    return render(request, "resume/success.html")