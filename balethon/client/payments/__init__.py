from .send_invoice import SendInvoice
from .inquire_transaction import InquireTransaction


class Payments(SendInvoice, InquireTransaction):
    pass
