from django.http import HttpResponseRedirect
from django.http import Http404
from django.contrib.auth.models import User
from employee.models import Employee

class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if 'employers' in request.path:
            try: 
                emp = Employee.objects.get(user = request.user)
                if not request.user.is_authenticated and emp.is_emp == False:
                    return HttpResponseRedirect('/login/')
            except:
                return HttpResponseRedirect('/login/')

            
            

        if 'admin' in request.path:

            if not request.user.is_authenticated:
                raise Http404

            
            
            if request.user.is_superuser == False:
                raise Http404

        response = self.get_response(request)

        return response