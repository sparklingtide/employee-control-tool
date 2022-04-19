from django.utils.functional import cached_property


class ShortcutsMixin:
    """
    Serializer mixin with shortcuts to ViewSet data
    """
    @cached_property
    def current_action(self):
        return getattr(self.current_view, 'action', '')

    @cached_property
    def current_kwargs(self):
        return getattr(self.current_view, 'kwargs', {})

    @cached_property
    def current_query_params(self):
        return getattr(self.current_request, 'query_params', {})

    @cached_property
    def current_request(self):
        return self.context.get('request')

    @cached_property
    def current_user(self):
        return getattr(self.current_request, 'user', None)

    @cached_property
    def current_view(self):
        return self.context.get('view')
