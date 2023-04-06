from django.http import HttpResponse
import sys
from django.shortcuts import render
from base.utils import debug_code

def home(request):
    context = {'error':False, 'output':"", 'code':"", 'input':""} 
    return render(request, 'base/index.html', context)


def execute_code(request):
    if(request.method == "POST"):
        if("execute" in request.POST):
            code = request.POST['editor']
            user_input = request.POST['input']

            d = user_input.split("\n")

            def input():
                try:
                    out = d[0]
                    d.pop(0)
                except:
                    raise Exception("Incomplete Inputs")

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

        if("debug" in request.POST):
            code = request.POST['editor']
            user_input = request.POST['input']

            d = user_input.split("\n")

            f = open("test.py", "w")
            s = """def input():
    try:
        out = d[0]
        d.pop(0)
    except:
        raise Exception("Incomplete Inputs")

    return out 
"""+"\n"
            f.write("d = "+str(d)+"\n")
            f.write(s)
            f.write(code)
            f.close()
            context = debug_code()
            context['line_order'].pop(0)
            context['line_order'].pop(0)
            context['outputs'].pop(0)
            context['outputs'].pop(0)
            for i in range(len(context['outputs'])):
                context['line_order'][i] -= 10

            print(context)
            context['error'] = False
            context['code'] = code
            context['input'] = user_input
            context['output'] = ''
            return render(request, 'base/index.html', context)
