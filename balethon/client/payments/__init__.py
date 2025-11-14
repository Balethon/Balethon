from .answer_pre_checkout_query import AnswerPreCheckoutQuery
from .create_invoice_link import CreateInvoiceLink
from .inquire_transacion import InquireTransaction
from .send_invoice import SendInvoice


class Payments(
    AnswerPreCheckoutQuery,
    CreateInvoiceLink,
    InquireTransaction,
    SendInvoice
):
    pass
