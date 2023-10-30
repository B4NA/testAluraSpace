from django.shortcuts import render, redirect
from users.forms import LogInForm, LogOnForm
from django.contrib.auth.models import User
from django.contrib import auth, messages

def login(request):
    forms = LogInForm()

    if request.method == 'POST':
        forms = LogInForm(request.POST)

        if forms.is_valid():
            NomeOrEmail = forms['NomeOrEmailLogIn'].value()
            password = forms['password'].value()

            if '@' in NomeOrEmail or '.com' in NomeOrEmail:
                NomeOrEmail = User.objects.get(email=NomeOrEmail).username
                account = auth.authenticate(
                    request,
                    username=NomeOrEmail,
                    password=password,
                )
            else:
                account = auth.authenticate(
                    request,
                    username=NomeOrEmail,
                    password=password,
                )

            if account is not None:
                auth.login(request, account)
                messages.success(request, f'Seja novamente bem-vindo(a) {NomeOrEmail}!')
                return redirect('index')
            else:
                messages.error(request, f'Senha ou nome ou Email incorreto.')
                return redirect('login')

    
    return render(request, 'users/login.html', {'form' : forms})

def logon(request):
    forms = LogOnForm()

    if request.method == 'POST':
        forms = LogOnForm(request.POST)

        if forms.is_valid():    
            nome = forms['nome'].value()
            email = forms['email'].value()
            password = forms['password'].value()

            if User.objects.filter(username=nome).exists():
                messages.error(request, 'Nome de usuário já existente. Tente novamente.')
                return redirect('logon')
            
            if User.objects.filter(email=email).exists():
                messages.error(request, ' O Correiro Eletrônico (E-mail) já está sendo utilizado. Tente novamente.')
                return redirect('logon')
            
            account = User.objects.create_user(
                username=nome,
                email=email,
                password=password
            )
            account.save()

            messages.success(request, f'Cadastro de {nome} efetuado.')
            return redirect('login')

    return render(request, 'users/logon.html', {'form': forms})

def logout(request):
    auth.logout(request)
    messages.success(request, 'Log Out efetuado.')
    return redirect('login')
