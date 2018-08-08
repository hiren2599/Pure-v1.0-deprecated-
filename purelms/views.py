from django.shortcuts import render
from django.http import HttpResponse
from django.views import View,generic

from .models import course

# Create your views here.
class indexView(generic.ListView):
    template_name='devnet/courses/index.html'
    context_object_name='allcourses'

    def get_queryset(self):
        return course.objects.all()


class backdoorloginView(View):
    template_name='devnet/courses/backdoorlogin.html'

    def get(self,request):
        return render(request,self.template_name)

class courseHomeView(View):
    template_name='devnet/courses/courseHome.html'

    def get(self,request,coursecode):
        return render(request,self.template_name,self.get_context_data(coursecode))

    def get_context_data(self,coursecode,**kwargs):
        context= {'thiscourse':course.objects.get(coursecode=coursecode)}
        return context



def trys(request):
    return HttpResponse("hello")
