from cruftbot.infrastructure.settings.components.base import MIDDLEWARE


MIDDLEWARE.append("querycount.middleware.QueryCountMiddleware")
