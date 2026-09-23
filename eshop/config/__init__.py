from .celery_base import app as worker_app

__all__ = ('worker_app',)