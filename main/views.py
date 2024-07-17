from django.shortcuts import render
from django.http import HttpResponse
from . import predict
def home(request):
    if request.method == 'POST':
        # Assuming the form has a textarea named 'mail'
        submitted_mail = request.POST.get('mail', '')
        result=predict.linear_regression(submitted_mail)
        context = {
            'result': result
        }
        print(submitted_mail)
        return render(request, 'result.html', context)
    else:
        return render(request, 'home.html')
