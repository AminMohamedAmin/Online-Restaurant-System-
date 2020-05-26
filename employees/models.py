from django.db import models

# Create your models here.


class Departments(models.Model):
    dep_name = models.CharField(max_length=150, db_index=True, unique=True)
    need_emp = models.BooleanField(default=False)
    dep_need = models.IntegerField(default=0, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('dep_name',)
        verbose_name = "Department"
        verbose_name_plural = "Departments"

    def __str__(self):
        return self.dep_name


class Employees(models.Model):
    dep = models.ForeignKey(Departments, related_name='employee', on_delete=models.CASCADE)
    emp_name = models.CharField(max_length=150)
    emp_code = models.CharField(max_length=150)
    national_id = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    leave = models.DateTimeField(null=True, default=None, blank=True)

    class Meta:
        ordering = ('dep',)
        verbose_name = "Employee"
        verbose_name_plural = "Employees"
