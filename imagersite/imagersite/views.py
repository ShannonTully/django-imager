from django.shortcuts import render


def home_view(request):
    '''
    Gets the home view
    '''
    return render(request, 'generic/home.html')
