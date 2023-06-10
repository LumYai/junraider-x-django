from django import forms
from django.db.models.base import Model
from app_foods.models import Food
from .models import subscription

class FoodModelMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.title

class SubscriptionForm(forms.Form):
    name = forms.CharField(max_length=60, required=True, label='ชื่อ-นามสกุล')
    email = forms.EmailField(max_length=60, required=True, label='email')
    food_set = FoodModelMultipleChoiceField(
        queryset=Food.objects.order_by('-is_premium'),
        required=True,
        label='เมนูที่สนใจ',
        widget=forms.CheckboxSelectMultiple 
    )
    accepted = forms.BooleanField(required=True, label='ตกลง ยอมรับเงื่อนไข')

class SubscriptionModelForm(forms.ModelForm):
    food_set = FoodModelMultipleChoiceField(
        queryset=Food.objects.order_by('-is_premium'),
        required=True,
        label='เมนูที่สนใจ',
        widget=forms.CheckboxSelectMultiple 
    )
    accepted = forms.BooleanField(required=True, label='ตกลง ยอมรับเงื่อนไข')
    class Meta:
        model = subscription
        fields = ['name', 'email', 'food_set', 'accepted']
        labels = {
            'name': 'ชื่อ-นามสกุล',
            'email': 'email',
            'food_set': 'เมนูที่สนใจ'
        }