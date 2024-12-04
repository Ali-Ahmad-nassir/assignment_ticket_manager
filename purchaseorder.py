from User import User

class PurchaseOrder:
    def __init__(self, order_id, user, ticket, purchase_date, quantity):
        self._order_id = order_id  # string
        self._user = user  # Reference to User
        self._ticket = ticket  # Reference to Ticket
        self._purchase_date = purchase_date  # datetime
        self._quantity = quantity  # int
        self._total_price = quantity * (ticket.get_price() - (ticket.get_price() * ticket.get_discount() / 100))  # float

    # Methods for order_id
    def get_order_id(self):
        return self._order_id

    def set_order_id(self, order_id):
        if isinstance(order_id, str) and order_id.strip():
            self._order_id = order_id
        else:
            raise ValueError("Order ID must be a non-empty string.")

    # Methods for user
    def get_user(self):
        return self._user

    def set_user(self, user):
        # Assuming User is a class, perform type checking
        if isinstance(user, User):
            self._user = user
        else:
            raise ValueError("User must be a valid User object.")

    # Methods for ticket
    def get_ticket(self):
        return self._ticket

    def set_ticket(self, ticket):
        # Assuming Ticket is a class, perform type checking
        if hasattr(ticket, "price") and hasattr(ticket, "discount"):
            self._ticket = ticket
            # Recalculate total price when ticket changes
            self.set_total_price()
        else:
            raise ValueError("Ticket must be a valid Ticket object.")

    # Methods for purchase_date
    def get_purchase_date(self):
        return self._purchase_date

    def set_purchase_date(self, purchase_date):
        if hasattr(purchase_date, "isoformat"):  # Basic check for datetime-like objects
            self._purchase_date = purchase_date
        else:
            raise ValueError("Purchase date must be a valid datetime object.")

    # Methods for quantity
    def get_quantity(self):
        return self._quantity

    def set_quantity(self, quantity):
        if isinstance(quantity, int) and quantity > 0:
            self._quantity = quantity
            # Recalculate total price when quantity changes
            self.set_total_price()
        else:
            raise ValueError("Quantity must be a positive integer.")

    # Methods for total_price
    def get_total_price(self):
        return self._total_price

    def set_total_price(self):
        self._total_price = self._quantity * (self._ticket.get_price() - (self._ticket.get_price() * self._ticket.get_discount() / 100))

    def __repr__(self):
        return f"PurchaseOrder(order_id={self._order_id}, user={self._user.get_username()}, total_price={self._total_price})"
