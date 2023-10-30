from django import forms

class LogInForm(forms.Form):
    NomeOrEmailLogIn = forms.CharField(label='Nome ou Email', required=True, max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Digite o nome ou o Email do usuário'
    }))
    password = forms.CharField(label='Senha', required=True, max_length=70, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Digite sua senha'
    }))

class LogOnForm(forms.Form):
    nome = forms.CharField(label='Nome', required=True, max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Digite o nome do usuário'
    }))
    email = forms.EmailField(label='Email', required=True, max_length=100, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Digite o seu Email'
    }))
    password = forms.CharField(label='Senha', required=True, max_length=70, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Digite a sua senha'
    }))
    confirmPassword = forms.CharField(label='Confirmar Senha', required=True, max_length=70, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Confirme sua senha'
    }))

    def clean_nome(self):
        nome = self.cleaned_data.get("nome")

        if nome:
            nome = nome.strip()
            if ' ' in nome:
                raise forms.ValidationError('O valor do campo Nome contém espaços.')
            else:
                return nome

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if email:
            email = email.strip()

            if ' ' in email:
                raise forms.ValidationError('O valor do campo Email possuem espaços.')
            elif not '@' in email:
                raise forms.ValidationError('O valor do campo Email não possui o caractere @.')
            else:
                return email
            
    def clean_confirmPassword(self):
        password = self.cleaned_data.get("password")
        confirmPassword = self.cleaned_data.get("confirmPassword")

        if password and confirmPassword:
            if password != confirmPassword:
                raise forms.ValidationError('Os valores dos campos Senha e Confirmar Senha são diferentes.')
            else:
                return confirmPassword
            