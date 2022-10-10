from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import Contact
from django.views.generic.list import ListView


def create_contact(request):

    # get data from form where name="contactname"
    name = request.POST.get(
        "contactname"
    )

    # get data from form where name="phone_number"
    phone_number = request.POST.get(
        "phone_number"
    )

    # add contact
    contact = Contact.objects.create(
        name=name, phone_number=phone_number
    )

    # add contact to database
    contacts = Contact.objects.all()

    # display the list of contacts in contact-list.html
    return render(
        request, "contact-list.html", {"contacts": contacts}
    )


def delete_contact(request, pk):
    # remove the contact from list.
    contact_id = Contact.objects.get(id=pk)
    contact_id.delete()
    contacts = Contact.objects.all()
    return render(request, "contact-list.html", {"contacts": contacts})


class ContactList(ListView):

    # html file to display the list of contacts
    template_name = "contact.html"

    model = Contact

    # used in the HTML template to loop through and list contacts
    context_object_name = (
        "contacts"
    )
