class Ticket:
    def __init__(self, ticket_id, ticket_type, price, validity, discount, limitations):
        self._ticket_id = ticket_id  # string
        self._ticket_type = ticket_type  # string (e.g., "Single-Day Pass")
        self._price = price  # float
        self._validity = validity  # string (e.g., "1 Day", "1 Year")
        self._discount = discount  # float (e.g., 10.0 for 10%)
        self._limitations = limitations  # string

    # Methods for ticket_id
    def get_ticket_id(self):
        return self._ticket_id

    def set_ticket_id(self, ticket_id):
        if isinstance(ticket_id, str) and ticket_id.strip():
            self._ticket_id = ticket_id
        else:
            raise ValueError("Ticket ID must be a non-empty string.")

    # Methods for ticket_type
    def get_ticket_type(self):
        return self._ticket_type

    def set_ticket_type(self, ticket_type):
        if isinstance(ticket_type, str) and ticket_type.strip():
            self._ticket_type = ticket_type
        else:
            raise ValueError("Ticket type must be a non-empty string.")

    # Methods for price
    def get_price(self):
        return self._price

    def set_price(self, price):
        if isinstance(price, (int, float)) and price >= 0:
            self._price = float(price)
        else:
            raise ValueError("Price must be a non-negative number.")

    # Methods for validity
    def get_validity(self):
        return self._validity

    def set_validity(self, validity):
        if isinstance(validity, str) and validity.strip():
            self._validity = validity
        else:
            raise ValueError("Validity must be a non-empty string.")

    # Methods for discount
    def get_discount(self):
        return self._discount

    def set_discount(self, discount):
        if isinstance(discount, (int, float)) and 0 <= discount <= 100:
            self._discount = float(discount)
        else:
            raise ValueError("Discount must be a number between 0 and 100.")

    # Methods for limitations
    def get_limitations(self):
        return self._limitations

    def set_limitations(self, limitations):
        if isinstance(limitations, str):
            self._limitations = limitations
        else:
            raise ValueError("Limitations must be a string.")

    def __repr__(self):
        return f"Ticket(ticket_type={self._ticket_type}, price={self._price})"
