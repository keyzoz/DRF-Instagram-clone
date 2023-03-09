from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    
    def create_user(self, email, password, **another_fiels):
        email = self.normalize_email()
        user = self.model.create_user(email=email,**another_fiels)
        user.set_password(password)
        user.save()
        return user
        
    def create_superuser(self, email, password, **another_fiels):
        
        another_fiels.setdefault('is_active',True)
        another_fiels.setdefault('is_staff',True)
        another_fiels.setdefault('is_superuser',True)
        
        if another_fiels.get('is_staff') is not True:
            raise ValueError('Superuser must be is_staff = True')
        
        if another_fiels.get('is_superuser') is not True:
            raise ValueError('Superuser must be is_superuser = True')
        
        return self.create_user(email, password, **another_fiels)