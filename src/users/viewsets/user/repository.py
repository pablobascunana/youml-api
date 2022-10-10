from django.contrib.auth.base_user import BaseUserManager


class UserRepository(BaseUserManager):
    def create_user(self, username: str, name: str, lastname: str, email: str, password: str, role: str):
        user = self.model(name=name, lastname=lastname, email=self.normalize_email(email), username=username, role=role)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_company_user(self, username: str, name: str, lastname: str, email: str, password: str, role: str,
                            company_uuid: str):
        user = self.model(name=name, lastname=lastname, email=self.normalize_email(email), username=username, role=role,
                          company_id=company_uuid)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, name, lastname, email, password, role='ADMIN'):
        user = self.model(name=name, lastname=lastname, email=self.normalize_email(email), username=username, role=role)
        user.set_password(password)
        user.save(using=self._db)
        return user
