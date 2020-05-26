from django.contrib import admin
from .models import OrderItem,order, OrderSent
from import_export.admin import ImportExportActionModelAdmin

################## pdf##############
from django.urls import reverse
from django.utils.safestring import mark_safe

def order_pdf(obj):
	return mark_safe('<a href="{}">PDF</a>'.format(reverse('orders:admin_order_pdf',args=[obj.id])))
order_pdf.short_description = 'Order PDF'
########################################

class OrderItemAdmin(admin.TabularInline):
	'''
		Admin View for OrderItem
	'''
	model = OrderItem
	raw_id_fields = ['product']


class OrderAdmin(ImportExportActionModelAdmin):
	'''
		Admin View for Order
	'''
	list_display = ('id','first_name','last_name','address','email','city','postal_code','sent','paid','date',order_pdf)
	list_filter = ('paid','sent','created','updated','date')
	search_fields = ['first_name','last_name','email','sent','date']
	list_editable = ('sent', 'paid')
	inlines = [
	OrderItemAdmin
	]


admin.site.register(order, OrderAdmin)


class OrderSentAdmin(ImportExportActionModelAdmin):
	'''
		Admin View for Order
	'''
	list_display = ('leaving_time','emp_code','order_id','updated',)
	list_filter = ('emp_code','order_id','updated','leaving_time',)
	search_fields = ['order_id','updated','order_id','updated']
	list_editable = ('order_id','emp_code')


admin.site.register(OrderSent, OrderSentAdmin)