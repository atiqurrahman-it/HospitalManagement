from django.shortcuts import render


# Create your views here.

def Admin_dasboard_page(request):
    return render(request, 'admin_panel/pages/admin_dashboard.html')
