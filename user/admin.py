from django.contrib import admin
from .models import Category,Product, Table, Contact, Careers
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
	'''
		Admin View for Category
	'''
	list_display = ('name','slug',)
	prepopulated_fields = {'slug':('name',)} # معناها قيمة سلاج هي نفس قيمة الاسم

admin.site.register(Category, CategoryAdmin)



class ProductAdmin(admin.ModelAdmin):
	'''
		Admin View for Product
	'''
	list_display = ('name','slug','category','price','available','created','updated',)
	list_filter = ('available','created','updated','category',) #تستخدم للبحث
	list_editable = ('price','available',) #قابلة للتعديل برا الفورم
	prepopulated_fields = {'slug':('category',)}

admin.site.register(Product, ProductAdmin)


class TableReservation(admin.ModelAdmin):
	'''
		Admin View for Reservation
	'''
	list_display = ('name', 'email', 'phone', 'many','date', 'time', 'message','attendance','created' ,'updated',)
	list_filter = ('attendance','email', 'created', 'updated','date', 'time',)  # تستخدم للبحث
	list_editable = ('phone','date', 'time', 'many','attendance')  # قابلة للتعديل برا الفورم

admin.site.register(Table, TableReservation)


class ContactMessages(admin.ModelAdmin):
	'''
		Admin View for Contact
	'''
	list_display = ('name', 'email','message','created','updated','date')
	list_filter = ('email', 'created','updated','date')  # تستخدم للبحث

admin.site.register(Contact, ContactMessages)


class Applying(admin.ModelAdmin):
	'''
		Admin View for Reservation
	'''
	list_display = ('name', 'email', 'phone', 'role','work', 'experience', 'cv','created' ,'updated','date')
	list_filter = ('email', 'created', 'updated','role', 'work','experience','date')  # تستخدم للبحث

admin.site.register(Careers, Applying)