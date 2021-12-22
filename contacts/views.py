from django.shortcuts import render
from home.views import *
from django.core.mail import send_mail

# Create your views here.
def contactPage(request):
    myFilter=search(request)
    amt = Cart.objects.count()
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']

        send_mail(
            
            subject,
            message,
            email,
            ['venocrypt@gmail.com'],
            fail_silently=False,
        )
        sent='Email successfully sent'
        context = {'amt':amt,'myFilter':myFilter,'sent':sent}
        return render(request, 'contact.html', context)
    context = {'amt':amt,'myFilter':myFilter}
    return render(request, 'contact.html', context)
