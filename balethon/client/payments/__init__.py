from .send_invoice import SendInvoice
from .inquire_transaction import InquireTransaction
from .answer_pre_checkout_query import AnswerPreCheckoutQuery


class Payments(SendInvoice, InquireTransaction, AnswerPreCheckoutQuery):
    pass
