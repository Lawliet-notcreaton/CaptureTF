from django.shortcuts import render
# views.py


# views.py

from django.shortcuts import render


def index(request):
    user_input = request.GET.get('input', '')
    flag = "CTF{SSt1salsom4d}"

    if user_input.strip() == "get_flag()":
        output = flag
    else:
        try:
            output = str(eval(user_input))
        except Exception as e:
            output = f"Error: {e}"

    return render(request, 'CTF/lessons/ssti/ssti_example.html', {'output': output})


def start(request):
    return render(request, 'CTF/lessons/ssti/index.html')