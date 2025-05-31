from .answer_pre_checkout_query import AnswerPreCheckoutQuery
from .send_invoice import SendInvoice


class Payments(AnswerPreCheckoutQuery, SendInvoice):
    pass
