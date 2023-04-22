from django.shortcuts import render

# Create your views here


def get_my_portfolio_index(request):
    return render(request, 'my_portfolio_app/my_portfolio_index.html')
    