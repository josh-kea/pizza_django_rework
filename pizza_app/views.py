from django.shortcuts import render, get_object_or_404, reverse
from .models import Account, Account_Transaction
from login_app.models import UserProfile
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

import random
# Create your views here.


@login_required
def index(request):
    if request.method == 'POST':
        uuid = random.randint(100000, 199999)

        Account.create(
            request.user, request.POST['account_name'], uuid, request.POST['starting_balance'])

        transactionID = random.randint(100000, 199999)

        transactionAmount = request.POST['starting_balance']

        Account_Transaction.create(
            request.user, uuid, request.POST['starting_balance'], transactionID, "Initial Deposit", transactionAmount)

    #accounts = Account.objects.filter(status=False).filter(user=request.user)
    accounts = Account.objects.filter(user=request.user)

    userProfiles = UserProfile.objects.filter(user=request.user)

    context = {
        'accounts': accounts,
        'userProfiles': userProfiles,
    }
    return render(request, 'pizza_app/index.html', context)


@login_required
def completed_accounts(request):
    accounts = Account.objects.filter(status=True)
    context = {
        'accounts': accounts,
    }
    return render(request, 'pizza_app/completed_accounts.html', context)


@login_required
def account_details(request):
    account_number = request.POST['account_number']
    accounts = Account.objects.filter(number=account_number)

    accountTransactions = Account_Transaction.objects.filter(
        number=account_number)

    context = {
        'accounts': accounts,
        'accountTransactions': accountTransactions,
    }

    return render(request, 'pizza_app/account_details.html', context)


@login_required
def account_withdraw(request):
    # Account.withdraw(request.POST['account_number'], request.POST['withdraw_amount'])
    # NO LONGER USING ABOVE FUNCTION, WILL RATHER IMPLEMENT THE FUNCTION HERE.

    transactionID = random.randint(100000, 200000)
    account_number = request.POST['account_number']
    account = Account.objects.get(number=account_number)

    account.balance = account.balance - int(request.POST['withdraw_amount'])
    account.save()

    transactionAmount = request.POST['withdraw_amount']

    # CREATE Account TRANSACTION WITH NEW TRANSACTION ID
    Account_Transaction.create(account.user, account.number,
                               account.balance, transactionID, "Withdraw", transactionAmount)

    accounts = Account.objects.filter(number=account_number)
    accountTransactions = Account_Transaction.objects.filter(
        number=account_number)

    context = {
        'accounts': accounts,
        'accountTransactions': accountTransactions,
    }

    return render(request, 'pizza_app/account_details.html', context)


@login_required
def account_deposit(request):
    # Account.deposit(request.POST['account_number'], request.POST['deposit_amount'])
    # NO LONGER USING ABOVE FUNCTION, WILL RATHER IMPLEMENT THE FUNCTION HERE.
    transactionID = random.randint(100000, 200000)

    account_number = request.POST['account_number']
    account = Account.objects.get(number=account_number)
    account.balance = account.balance + int(request.POST['deposit_amount'])
    account.save()

    transactionAmount = request.POST['deposit_amount']

    # CREATE Account TRANSACTION WITH NEW TRANSACTION ID
    Account_Transaction.create(account.user, account.number,
                               account.balance, transactionID, "Deposit", transactionAmount)

    accounts = Account.objects.filter(number=account_number)
    accountTransactions = Account_Transaction.objects.filter(
        number=account_number)

    context = {
        'accounts': accounts,
        'accountTransactions': accountTransactions,
    }

    return render(request, 'pizza_app/account_details.html', context)


@login_required
def account_transfer(request):
    fromAccountNumber = request.POST['transfer_from_account']
    toAccountNumber = request.POST['transfer_to_account']

    fromAccount = Account.objects.get(number=fromAccountNumber)
    toAccount = Account.objects.get(number=toAccountNumber)

    transferAmount = request.POST['transfer_amount']

    fromAccount.balance = fromAccount.balance - int(transferAmount)
    toAccount.balance = toAccount.balance + int(transferAmount)

    fromAccount.save()
    toAccount.save()

    # CREATE Account TRANSACTION WITH NEW TRANSACTION ID
    transactionID = random.randint(100000, 200000)

    Account_Transaction.create(fromAccount.user, fromAccount.number,
                               fromAccount.balance, transactionID, "Transfer Out", transferAmount)

    Account_Transaction.create(toAccount.user, toAccount.number,
                               toAccount.balance, transactionID, "Transfer In", transferAmount)

    return HttpResponseRedirect(request.META['HTTP_REFERER'])
