from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, template_name='signup/index.html')

def signup(request):
    # this signup_page.html loads by default irrespective of adding the template settings as BASE_DIR / 'templates' or not
    return render(request, template_name='signup/signup_page.html')