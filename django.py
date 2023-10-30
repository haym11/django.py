from django.db import models
from django.core.exceptions import ValidationError

class Company(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    tax_code = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        if not self.pk and Company.objects.exists():
            raise ValidationError('There can be only one Company instance.')
        return super(Company, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=200)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Position(models.Model):
    title = models.CharField(max_length=200)
    job_description = models.TextField()

    def __str__(self):
        return self.title

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'phone_number')

admin.site.register(Employee, EmployeeAdmin)