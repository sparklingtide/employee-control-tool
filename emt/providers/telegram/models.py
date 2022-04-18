from django.db import models
from emt.providers.models import Resource
from django.conf import settings
from telethon.tl.functions.messages import CreateChatRequest, AddChatUserRequest, DeleteChatUserRequest


class Telegram(Resource):
    group_id = models.IntegerField(null=True, blank=True, unique=True)

    @classmethod
    def create(cls, **kwargs):
        telegram = Telegram(**kwargs)

        client = cls._get_client()
        created_group = client(
            CreateChatRequest(
                title=telegram.name,
                users=settings.TELEGRAM_BASE_USERS,
            )
        )

        telegram.group_id = created_group.chats[0].id
        telegram.save()
        return telegram

    def give_access(self, employee):
        client = self._get_client()
        client(
            AddChatUserRequest(
                chat_id=self.group_id,
                user_id=employee.telegram,
                fwd_limit=0,  # won't be able to see history
            )
        )

    def revoke_access(self, employee):
        client = self._get_client()
        client(
            DeleteChatUserRequest(
                chat_id=self.group_id,
                user_id=employee.telegram,
                revoke_history=True,  # won't be able to see history
            )
        )

    @staticmethod
    def _get_client() -> settings.TelegramAPIClient:
        client = settings.TelegramAPIClient
        assert client is not None, "Telegram broken"
        client.connect()
        return client
