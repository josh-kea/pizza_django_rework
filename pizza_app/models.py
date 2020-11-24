from django.contrib.auth.models import User
from django.db import models
import random


class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=250)
    number = models.IntegerField(default=0)
    balance = models.IntegerField(default=0)

    @classmethod
    def create(cls, user, text, number, balance):
        account = cls()
        account.user = user
        account.text = text
        account.number = number
        account.balance = balance
        account.save()

    def withdraw(number, amount):
        transactionID = random.randint(100000, 400000)
        account = Account.objects.get(number=number)
        account.balance = account.balance - amount
        account.save()

        # CREATE account TRANSACTION WITH NEW TRANSACTION ID
        Account_Transaction.create(account.user, account.number,
                                   account.balance, transactionID)

    def deposit(number, amount):
        transactionID = random.randint(100000, 400000)
        account = Account.objects.get(number=number)
        account.balance = account.balance + amount
        account.save()

        # CREATE account TRANSACTION WITH NEW TRANSACTION ID
        Account_Transaction.create(account.user, account.number,
                                   account.balance, transactionID)

    def toggle_status(self):
        # self.text = not self.text
        self.save()

    def __str__(self):
        return f"Account: {self.number} User: {self.user}"


class Account_Transaction(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.IntegerField(null=False)
    balance = models.IntegerField(null=False)
    transactionID = models.IntegerField(default=0)
    transactionType = models.CharField(default="Not Stated", max_length=250)
    transactionAmount = models.IntegerField(default=0, null=False)

    @classmethod
    def create(cls, user, number, balance, transactionID, transactionType, transactionAmount):
        account_transaction = cls()
        account_transaction.user = user
        account_transaction.number = number
        account_transaction.balance = balance
        account_transaction.transactionID = transactionID
        account_transaction.transactionType = transactionType
        account_transaction.transactionAmount = transactionAmount
        account_transaction.save()

    def __str__(self):
        return f"Transaction ID: {self.transactionID} Account Number: {self.number} User: {self.user}"
