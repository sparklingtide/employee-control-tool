import factory


class CustomDjangoModelFactory(factory.django.DjangoModelFactory):
    @classmethod
    def _after_postgeneration(cls, instance, create, results=None):
        instance.refresh_from_db()
        instance.clean()
