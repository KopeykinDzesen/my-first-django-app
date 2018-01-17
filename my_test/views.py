from django.shortcuts import render

def my_test(request):
    return render(request, "my_test/my_test.html", locals())
