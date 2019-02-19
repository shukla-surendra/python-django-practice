from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.core.files.storage import FileSystemStorage

# Create your views here.
class Home(View):
    template_name = 'app/index.html'
    def get(self, request):
        return render(request, self.template_name, {})
    def post(self, request):
        myfiles = request.FILES.getlist('upload_name')
        for file_s in myfiles:
            fs = FileSystemStorage() # MEDIA_URL or MEDIA_ROOT if given in settings else takes BASE_DIR
            filename = fs.save(file_s.name, file_s)
            uploaded_file_url = fs.url(filename)
            print(uploaded_file_url)
        return render(request, self.template_name, {})
