from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied

from . import models


def submit(request):
    if request.method != "POST":
        raise PermissionDenied()

    addressee = request.POST.get("addressee")
    college = request.POST.get("college")
    message = request.POST.get("message")

    if not all((addressee, college, message)):
        return redirect("/")
    
    if not len(message) <= 280:
        return redirect("/")
    
    if not len(addressee) <= 50:
        return redirect("/")

    letter = models.Letter(
        addressee=addressee,
        college=college,
        message=message,
        status=models.Letter.LetterStatus.SENT,
    )
    letter.save()

    return redirect("/")
