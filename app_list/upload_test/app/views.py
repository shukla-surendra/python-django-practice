from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
class Home(View):
    template_name = 'app/index.html'
    def get(self, request):
        # <view logic>
        # return HttpResponse('result')
        return render(request, self.template_name, {})
    def post(self, request):
        print(type(request.FILES['upload_name']))
        print(help(request.FILES['upload_name']))
        
        # <view logic>
        # return HttpResponse('result')
        return render(request, self.template_name, {})

'''
def handle_uploaded_file(f):
    nt = str(time.time())
    stamp = nt.replace(".","-")
    filename = stamp+"-"+f.name.replace(" ","-")
    filename = filename.replace(",","-")
    with open(BASE_DIR+'/static/uploads/documents/'+filename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return filename
'''