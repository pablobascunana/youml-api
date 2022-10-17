from django.contrib.auth.base_user import BaseUserManager

from api.viewsets.company.model import Company


class UserRepository(BaseUserManager):
    def create_user(self, username: str, name: str, lastname: str, email: str, password: str, role: str):
        user = self.model(name=name, lastname=lastname, email=self.normalize_email(email), username=username, role=role)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_company_user(self, username: str, name: str, lastname: str, email: str, password: str, role: str,
                            company: Company):
        user = self.model(name=name, lastname=lastname, email=self.normalize_email(email), username=username, role=role,
                          company=company)
        user.set_password(password)
        user.save(using=self._db)
        return user
