from decimal import Decimal
from django.conf import settings  # نستدعي key session
from user.models import Product
from coupons.models import Coupons


class Cart(object):
	"""docstring for Cart"""

	def __init__(self, request):  # normal request to make visitors who save sessions, يعني مش لازم يعمل حساب عشان يقدر يحفظ
		"""initalize the cart"""
		self.session = request.session  # make CRUD method accessible for visitors
		cart = self.session.get(settings.CART_SESSION_ID)  #لو فيه قيمة في الكارت هاتها وسيفها في الكارت

		if not cart:  #لو الكارت فاضية
			cart = self.session[settings.CART_SESSION_ID] = {}
		self.cart = cart
		self.coupon_id = self.session.get('coupon_id')


	def add(self,product,quantity=1,update_quantity=False):
		product_id = str(product.id)  # لأن السيشن لاتتعامل الا مع جسون والجسوت تتعامل بالاسترينج

		if product_id not in self.cart:
			self.cart[product_id] = {'quantity':0,'price':str(product.price)}  #ضيفه

		if update_quantity:
			self.cart[product_id]['quantity'] = quantity
		else:
			self.cart[product_id]['quantity'] += quantity
		self.save()


	def save(self):
		self.session[settings.CART_SESSION_ID] = self.cart  #هيعمل سيف للسيشن في الكارت اي دي
		self.session.modified = True  #هيسيف السيشن في الستنجس بعد الاضافة اللى حصلت

	def remove(self,product):
		product_id = str(product.id)
		if product_id in self.cart:
			del self.cart[product_id]
			self.save()

	def __iter__(self):  #يعدي علي كل العناصر اللى في الكارت ثم يعرضها
		product_ids = self.cart.keys()
		products = Product.objects.filter(id__in=product_ids)
		for product in products:
			self.cart[str(product.id)]['product'] = product

		for item in self.cart.values():
			item['price'] = Decimal(item['price'])
			item['total_price'] = item['price'] * item['quantity']
			yield item

	def __len__(self):  #مجموع العناصر اللى في الكارت
		return sum(item['quantity'] for item in self.cart.values())

	def get_total_price(self):  #مجموع فلوس المشتريات في الكارت
		return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

	def clear(self):  #امسح السيشن من الكارت بعد الاوردر مايتم ويتبعت
		del self.session[settings.CART_SESSION_ID]
		self.session.modified = True



	@property
	def coupon(self):
		if self.coupon_id:
			return Coupons.objects.get(id=self.coupon_id)
		return None

	def get_discount(self):
		if self.coupon:
			return (self.coupon.discount / Decimal('100')) * self.get_total_price()
		return Decimal('0')

	def get_total_price_after_discount(self):
		return self.get_total_price() - self.get_discount()