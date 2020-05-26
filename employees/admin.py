from django.contrib import admin
from .models import Departments, Employees
# Register your models here.


class DepartmentAdmin(admin.ModelAdmin):
	'''
		Admin View for Departments
	'''
	list_display = ('dep_name','need_emp','dep_need','created')
	list_filter = ('dep_name','dep_need','need_emp','created') #تستخدم للبحث
	list_editable = ('need_emp','dep_need',) #قابلة للتعديل برا الفورم

admin.site.register(Departments, DepartmentAdmin)


class EmployeeAdmin(admin.ModelAdmin):
	'''
		Admin View for Employees
	'''
	list_display = ('dep','emp_name','emp_code','national_id','active','created')
	list_filter = ('dep','emp_code','emp_name','created') #تستخدم للبحث
	list_editable = ('active',) #قابلة للتعديل برا الفورم

admin.site.register(Employees, EmployeeAdmin)