from django.http import HttpResponse
import sys
from django.shortcuts import render

def home(request):
    context = {'error':False, 'output':""} 
    return render(request, 'base/index.html', context)


def execute_code(request):
    if(request.method == "POST"):
        code = request.POST['code']
        try:
            original_stdout = sys.stdout
            sys.stdout = open('file.txt', 'w')
            exec(code)
            sys.stdout.close()
            sys.stdout = original_stdout
            output = open('file.txt', 'r').read()
            context = {'error':False, 'output':output}

        except Exception as e:
            sys.stdout = original_stdout
            context = {'error':True, 'output':e}
    print(context)
    return render(request, 'base/index.html', context)

