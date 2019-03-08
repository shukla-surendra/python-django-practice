from django.shortcuts import render
from django.views import View
from .forms import ProfileForm

# Create your views here.

class Home(View):
    template_name = 'client/index.html'
    def get(self, request):
        form = ProfileForm()
        return render(request, self.template_name, {"form":form})
    def post(self, request):
        form = ProfileForm(request.POST)
        return render(request, self.template_name, {"form":form})
