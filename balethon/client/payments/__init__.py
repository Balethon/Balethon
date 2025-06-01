from .answer_pre_checkout_query import AnswerPreCheckoutQuery
from .inquire_transaction import InquireTransaction
from .send_invoice import SendInvoice


class Payments(AnswerPreCheckoutQuery, InquireTransaction, SendInvoice):
    pass
