from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, user_name, email, password):
        if not user_name:
            raise ValueError('Users must have an username')
        if not email:
            raise ValueError('Users must have an email address')
        if not password:
            raise ValueError('Users must have an password')
        
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            user_name=user_name,
            email=self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)

        return user
