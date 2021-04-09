from django.http import HttpResponse, response
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.messaging_response import MessagingResponse


@csrf_exempt
def message(request):
    user = request.POST.get('From')
    message = request.POST.get('Body')
    print('\n *** New Message ***')
    print(f'\n{user} says {message}')
    print('\n *******************\n')

    response = MessagingResponse()
    response.message(
        'Thank you for your message! A member of our team will be in touch with you soon.'
        )

    return HttpResponse(str(response))