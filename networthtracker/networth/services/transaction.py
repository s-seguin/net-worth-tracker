import logging

from networth.models.assets.asset import Asset
from networth.models.liabilities.liability import Liability
from users.models import User

from ..models.transaction import Transaction


class TransactionService:
    @staticmethod
    def get_transactions(*, user: User):
        logging.debug("getting transactions via service")
        transactions = Transaction.objects.filter(user=user).order_by(
            "-updated_on"
        )

        return transactions

    @staticmethod
    def create_transaction(
        *,
        asset: Asset,
        liability: Liability,
        user: User,
        transaction_date,
        settlement_date,
        action: str,
        description: str,
        quantity: float,
        gross_amount: float,
        commission: float,
    ):
        net_amount = gross_amount - commission
        logging.debug("creating a transaction via service")
        transaction = Transaction.objects.create(
            asset=asset,
            liability=liability,
            user=user,
            transaction_date=transaction_date,
            settlement_date=settlement_date,
            action=action,
            description=description,
            quantity=quantity,
            gross_amount=gross_amount,
            net_amount=net_amount,
            commission=commission,
        )
        return transaction
