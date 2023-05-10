# Django middleware for DDOS defense

from django.http import HttpResponseForbidden
from django.core.cache import cache
from django.conf import settings

class DDOSMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.ip = None
        self.user_agent = None

    def __call__(self, request):
        self.ip = request.META.get('REMOTE_ADDR')
        self.user_agent = request.META.get('HTTP_USER_AGENT')

        if self.is_request_valid():
            return self.get_response(request)
        else:
            return HttpResponseForbidden()

    def is_request_valid(self):
        if self.ip is None or self.user_agent is None:
            return False

        cache_key = f'ddos:{self.ip}:{self.user_agent}'
        request_count = cache.get(cache_key, 0)
        if request_count >= settings.DDOS_LIMIT:
            return False

        cache.set(cache_key, request_count + 1, settings.DDOS_EXPIRATION)
        return True
