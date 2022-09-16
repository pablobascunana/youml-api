from django.contrib.auth.base_user import BaseUserManager


class UserRepository(BaseUserManager):
    def create_user(self, username, name, lastname, email, password):
        user = self.model(name=name, lastname=lastname, email=self.normalize_email(email), username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, name, lastname, email, password, role='ADMIN'):
        user = self.model(name=name, lastname=lastname, email=self.normalize_email(email), username=username, role=role)
        user.set_password(password)
        user.save(using=self._db)
        return user
