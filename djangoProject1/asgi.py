import os
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter

from socialnetwork import urls

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject1.settings')
django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,

    "websocket": AuthMiddlewareStack(URLRouter(urls.websocket_urlpatterns)),
})
