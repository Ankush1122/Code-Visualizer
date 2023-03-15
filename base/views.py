from django.http import HttpResponse
import sys
from django.shortcuts import render

def home(request):
    context = {'error':False, 'output':"", 'code':"", 'input':""} 
    return render(request, 'base/index.html', context)


def execute_code(request):
    if(request.method == "POST"):
        code = request.POST['code']
        user_input = request.POST['input']

        d = user_input.split("\n")

        def input():
            try:
                out = d[0]
                d.pop(0)
            except:
                raise Exception("Enter Inputs")

            return out

        try:
            original_stdout = sys.stdout
            sys.stdout = open('file.txt', 'w')
            exec(code)
            sys.stdout.close()
            sys.stdout = original_stdout
            output = open('file.txt', 'r').read()
            context = {'error':False, 'output':output, 'code':code, 'input':user_input}

        except Exception as e:
            sys.stdout = original_stdout
            context = {'error':True, 'output':e, 'code':code, 'input':user_input}
    print(context)
    return render(request, 'base/index.html', context)

