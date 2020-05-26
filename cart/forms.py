from django import forms

PRODUCT_QUANTITY_CHOICES = [(i,str(i)) for i in range(1,21)]


class CartAddProductForm(forms.Form):
    # TODO: Define form fields here
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES,coerce=int)  #choices mean choice from 1 to 20.   #coerce means convert savig quantities to integer
    update = forms.BooleanField(required=False,initial=False,widget=forms.HiddenInput)  #لو عملت ابديت هيديني ترو لو معملتش هيديني فولص