from django.apps import AppConfig


class BookshelfConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookshelf'

    def ready(self):
        # CRUCIAL: Import the signals file to activate the @receiver function
        import bookshelf.signals
