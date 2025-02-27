from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,email,first_name,last_name,username,password=None,password2=None,is_doctor=False):
        if not email:
            raise ValueError('user must have a valid email') 
        user = self.model(
            email = self.normalize_email(email),
            first_name=first_name,
            last_name = last_name,
            username = username,
            is_doctor = is_doctor,
        )
        user.set_password(password)
        user.save(using=self.db)
        return user
    

    def create_superuser(self, email, first_name,last_name,username, password=None):
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            username=username,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
    
class User(AbstractBaseUser):
    email = models.EmailField(unique=True,max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    blocked = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','username']

    def __str__(self):
        return self.email
    
    def has_perm(self,perm,obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_admin
    

class Doctors(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='doctors')
    department = models.CharField(max_length=155,null=True,blank=True)
    hospital = models.CharField(max_length=155,null=True,blank=True)    

    is_verified = models.BooleanField(default=False)






