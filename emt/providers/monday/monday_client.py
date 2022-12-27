from monday import MondayClient as MondayCL
from monday.resources import BoardResource as BResource
from monday.resources import (
    ComplexityResource,
    GroupResource,
    ItemResource,
    NotificationResource,
    TagResource,
    UpdateResource,
    UserResource,
    WorkspaceResource,
)


def add_users_to_board_query(board_id, user_ids, kind):
    return """mutation {
        add_subscribers_to_board (board_id: %s, user_ids: %s, kind: %s) {
            id
        }
    }""" % (
        board_id,
        user_ids,
        kind,
    )


def delete_users_from_board_query(board_id, user_ids):
    return """mutation {
        delete_subscribers_from_board (board_id: %s, user_ids: %s) {
            id
        }
    }""" % (
        board_id,
        user_ids,
    )


class BoardResource(BResource):
    def add_users_to_board(self, board_id, user_ids, kind="subscriber"):
        query = add_users_to_board_query(board_id, user_ids, kind)
        return self.client.execute(query)

    def delete_users_from_board(self, board_id, user_ids):
        query = delete_users_from_board_query(board_id, user_ids)
        return self.client.execute(query)


class MondayClient(MondayCL):
    def __init__(self, token):
        """
        :param token: API Token for the new :class:`BaseResource` object.
        """
        self.items = ItemResource(token=token)
        self.updates = UpdateResource(token=token)
        self.tags = TagResource(token=token)
        self.boards = BoardResource(token=token)
        self.users = UserResource(token=token)
        self.groups = GroupResource(token=token)
        self.complexity = ComplexityResource(token=token)
        self.workspaces = WorkspaceResource(token=token)
        self.notifications = NotificationResource(token=token)
