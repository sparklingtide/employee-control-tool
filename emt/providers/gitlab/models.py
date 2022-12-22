from django.conf import settings
from django.db import models
from gitlab import Gitlab as GitlabCLient
from emt.providers.models import Resource


class Role(models.IntegerChoices):
    MINIMAL_ACCESS = 5, "minimal access"
    GUEST = 10, "guest"
    REPORTER = 20, "reporter"
    DEVELOPER = 30, "developer"
    MAINTAINER = 40, "maintainer"
    OWNER = 50, "owner"


class Gitlab(Resource):
    project_id = models.IntegerField(null=True, blank=True)
    role = models.IntegerField(choices=Role.choices, default=Role.MINIMAL_ACCESS)

    def give_access(self, employee):
        gitlab_cl = self._get_client()
        employee_gitlab = gitlab_cl.users.list(username=employee.gitlab_username)[0]
        project = gitlab_cl.projects.get(self.project_id)
        project.members.create(
            {"user_id": employee_gitlab.id, "access_level": self.role}
        )
        project.save()

    def revoke_access(self, employee):
        gitlab_cl = self._get_client()
        employee_gitlab = gitlab_cl.users.list(username=employee.gitlab_username)[0]
        project = gitlab_cl.projects.get(self.project_id)
        project.members.delete(employee_gitlab.id)

    @staticmethod
    def _get_client() -> GitlabCLient:
        client = settings.GITLAB_API_CLIENT
        assert client is not None, "Gitlab broken"
        return client
