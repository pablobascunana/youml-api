from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, name, lastname, email, password=None):
        if not email:
            raise ValueError('must have an email address.')

        user = self.model(name=name, lastname=lastname, email=self.normalize_email(email), username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, name, lastname, email, password=None):
        user = self.model(name=name, lastname=lastname, email=self.normalize_email(email), username=username,
                          role='ADMIN')
        user.is_admin = True
        user.set_password(password)
        user.save(using=self._db)
        return user
