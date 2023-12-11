from django.shortcuts import render


def sandbox(request):

    context = {

    }

    return render(request, 'sandbox/template.html', context)