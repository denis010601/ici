from django import forms
from .models import *

class ProductFilterForm(forms.Form):
    SIZE_CHOICES = [
        ('all', 'Все'),
        ('small', 'До 2000 мм'),
        ('medium', '2000-3000 мм'),
        ('large', 'Свыше 3000 мм'),
    ]

    size = forms.ChoiceField(
        choices=SIZE_CHOICES,
        label='Размер',
        required=False
    )

    def __init__(self, *args, **kwargs):
        category = kwargs.pop('category', None)
        super(ProductFilterForm, self).__init__(*args, **kwargs)

        if category:
            sizes = Product.objects.filter(category=category, size__isnull=False).values_list('size__id', 'size__sizeL', 'size__sizeW', 'size__sizeH').distinct()
            has_sizes = bool(sizes)

            if has_sizes:
                self.fields['size'] = forms.ChoiceField(
                    choices=self.SIZE_CHOICES,
                    label='Размер',
                    required=False
                )

            if has_sizes:
                self.fields['size'] = forms.ChoiceField(
                    choices=self.SIZE_CHOICES,
                    label='Размер',
                    required=False
                )
            else:
                self.fields.pop('size', None)
            sleepers = Product.objects.filter(category=category, has_sleeper__isnull=False).values_list('has_sleeper__id', 'has_sleeper__title').distinct()
            appearances = Product.objects.filter(category=category, appearance__isnull=False).values_list('appearance__id', 'appearance__title').distinct()
            supports = Product.objects.filter(category=category, supports__isnull=False).values_list('supports__id', 'supports__title').distinct()
            armrests = Product.objects.filter(category=category, armrests__isnull=False).values_list('armrests__id', 'armrests__title').distinct()

            if sizes:
                self.fields['size'] = forms.ChoiceField(
                    choices=self.SIZE_CHOICES,
                    label='Размер',
                    required=False
                )
            print(sizes)
            if sleepers:
                self.fields['sleeper'] = forms.ModelMultipleChoiceField(
                    queryset=Sleeper.objects.filter(id__in=[item[0] for item in sleepers]),
                    widget=forms.CheckboxSelectMultiple,
                    label='Спальное место',
                    required=False
                )

            if appearances:
                self.fields['appearance'] = forms.ModelMultipleChoiceField(
                    queryset=Appearance.objects.filter(id__in=[item[0] for item in appearances]),
                    widget=forms.CheckboxSelectMultiple,
                    label='Форма спинки',
                    required=False
                )

            if supports:
                self.fields['supports'] = forms.ModelMultipleChoiceField(
                    queryset=Supports.objects.filter(id__in=[item[0] for item in supports]),
                    widget=forms.CheckboxSelectMultiple,
                    label='Опоры',
                    required=False
                )

            if armrests:
                self.fields['armrests'] = forms.ModelMultipleChoiceField(
                    queryset=Armrests.objects.filter(id__in=[item[0] for item in armrests]),
                    widget=forms.CheckboxSelectMultiple,
                    label='Подлокотники',
                    required=False
                )

        if 'size' not in self.fields:
            self.fields.pop('size', None)


        if 'sleeper' not in self.fields:
            self.fields.pop('sleeper', None)

        if 'appearance' not in self.fields:
            self.fields.pop('appearance', None)

        if 'supports' not in self.fields:
            self.fields.pop('supports', None)

        if 'armrests' not in self.fields:
            self.fields.pop('armrests', None)

