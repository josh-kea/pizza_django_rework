"""
ASGI config for pizza_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os
import django
from channels.routing import get_default_application

# NEW, adding channels
from django.urls import path
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import chat.routing, notification.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pizza_project.settings')
# django.setup()
# application = get_default_application()

# application = get_asgi_application()
#NEW channels config instead of above.

application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": AuthMiddlewareStack(
        URLRouter(
            # chat.routing.websocket_urlpatterns,
            notification.routing.websocket_urlpatterns,
            #path("notifications/", NotificationConsumer),    # Url path for connecting to the websocket to send notifications.
        )
    ),
})
