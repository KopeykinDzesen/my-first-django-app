from django import forms
import re


class CheckoutContactForm(forms.Form):
    name = forms.CharField(required=True, error_messages={'required': 'Укажите имя'})
    phone = forms.CharField(required=True, error_messages={'required': 'Укажите телефон'})

    def clean(self):

        print(str(self.cleaned_data.get('name')))
        print(str(self.cleaned_data.get('phone')))

        patternDigit = re.compile('\d')
        patternSpace = re.compile('\s')
        patternPhone = re.compile('^\+\d')

        isValidName = True
        if patternSpace.findall(str(self.cleaned_data.get('name'))) or \
                patternDigit.findall(str(self.cleaned_data.get('name'))):
            isValidName = False

        isValidPhone1 = True
        print(patternPhone.findall(str(self.cleaned_data.get('phone'))))
        if not patternPhone.findall(str(self.cleaned_data.get('phone'))):
            isValidPhone1 = False

        isValidPhone2 = True
        print(patternSpace.findall(str(self.cleaned_data.get('phone'))))
        print(str(self.cleaned_data.get('phone')).isalpha())
        if patternSpace.findall(str(self.cleaned_data.get('phone'))) or \
                str(self.cleaned_data.get('phone')).isalpha():
            isValidPhone2 = False

        isValidPhone3 = True
        print(len(str(self.cleaned_data.get('phone'))) != 13)
        if len(str(self.cleaned_data.get('phone'))) != 13:
            isValidPhone3 = False

        if not isValidName:
            print('name is not valid!')
            raise forms.ValidationError('В имени содержатся не допустимые символы')

        if not isValidPhone1:
            print('phone is not valid (1)!')
            raise forms.ValidationError('Введите телефон в соответствии с шаблоном (+375447662313)')

        if not isValidPhone2:
            print('phone is not valid (2)!')
            raise forms.ValidationError('Не допустимые символы в телефоне')

        if not isValidPhone3:
            print('phone is not valid (3)!')
            raise forms.ValidationError('Не верное количество символов в телефоне')

        return self.cleaned_data