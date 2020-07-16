"""Global views."""
from django.http import JsonResponse


def ping(request):
    """
    Ping test.

    for testing ping
    :param request:
    :return:
    """
    data = {"ping": "pong"}
    return JsonResponse(data)
