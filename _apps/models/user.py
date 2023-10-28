from django.db import models

class Group(models.Model):
    group = models.CharField(max_length=9, db_index=True)
    desc = models.TextField(null=True)
    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.group

class User(models.Model):
    name = models.CharField(max_length=250)
    username = models.CharField(max_length=255, unique=True, db_index=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True, null=True)
    phone = models.IntegerField(unique=True, db_index=True, null=True)
    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.judul
