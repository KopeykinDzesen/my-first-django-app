from django.shortcuts import render
from .forms import SubscriberForm


def store_opening(request):

    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        data = form.cleaned_data

        print(data["name"])
        print(data["email"])

        new_form = form.save()

    return render(request, "store_opening/store_opening.html", locals())
