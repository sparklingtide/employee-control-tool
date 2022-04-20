from unittest.mock import Mock

from telethon.tl import TLRequest


def mocked_client(client_request: TLRequest) -> Mock:
    client = Mock()
    chat = Mock()
    chat.id = 111
    client.chats = [chat]
    return client
