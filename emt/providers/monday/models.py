from django.conf import settings
from django.db import models

from emt.providers.models import Resource

from .monday_client import MondayClient


class Monday(Resource):
    board_id = models.CharField(max_length=100)

    def give_access(self, employee):
        if not employee.monday_user_id:
            employee.monday_user_id = self._get_user_id(employee.email)
            employee.save()

        monday_cl = self._get_client()
        monday_cl.boards.add_users_to_board(self.board_id, employee.monday_user_id)

    def revoke_access(self, employee):
        if not employee.monday_user_id:
            employee.monday_user_id = self._get_user_id(employee.email)
            employee.save()

        monday_cl = self._get_client()
        monday_cl.boards.delete_users_from_board(self.board_id, employee.monday_user_id)

    @staticmethod
    def _get_client() -> MondayClient:
        return MondayClient(settings.MONDAY_TOKEN)

    def _get_user_id(self, employee_email) -> str:
        monday_cl = self._get_client()
        monday_users = monday_cl.users.fetch_users()
        for user_data in monday_users.get("data").get("users"):
            if user_data.get("email") == employee_email:
                return user_data.get("id")
