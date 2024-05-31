import os


from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

from chat.routing import websocket_urlpatterns
from chat.token_auth import TokenAuthMiddleware


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangobnb_backend.settings")
application = get_asgi_application()

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': TokenAuthMiddleware(
        URLRouter(
            websocket_urlpatterns
        )
    )
})
