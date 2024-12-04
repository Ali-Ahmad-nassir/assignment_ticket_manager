# CoreService Class
class CoreService:
    def __init__(self):
        self.users = []  # List of User objects
        self.tickets = []  # List of Ticket objects
        self.purchase_orders = []  # List of PurchaseOrder objects
        self.reservations = []  # List of EventReservation objects
        

    # User Management
    def add_user(self, user):
        self.users.append(user)

    def find_user(self, username):
        for u in self.users:
         print(u)
        return next((user for user in self.users if user.get_username() == username), None)

    def delete_user(self, username):
        user = self.find_user(username)
        if user:
            self.users.remove(user)
            return True
        return False

    # Ticket Management
    def add_ticket(self, ticket):
        self.tickets.append(ticket)

    def find_ticket(self, ticket_id):
        return next((ticket for ticket in self.tickets if ticket.get_ticket_id() == ticket_id), None)

    def delete_ticket(self, ticket_id):
        ticket = self.find_ticket(ticket_id)
        if ticket:
            self.tickets.remove(ticket)
            return True
        return False

    # Purchase Order Management
    def add_purchase_order(self, purchase_order):
        self.purchase_orders.append(purchase_order)

    def find_purchase_order(self, order_id):
        return next((order for order in self.purchase_orders if order.order_id == order_id), None)

    # Reservation Management
    def add_reservation(self, reservation):
        self.reservations.append(reservation)

    def find_reservation(self, reservation_id):
        return next((reservation for reservation in self.reservations if reservation.reservation_id == reservation_id), None)

    def delete_reservation(self, reservation_id):
        reservation = self.find_reservation(reservation_id)
        if reservation:
            self.reservations.remove(reservation)
            return True
        return False
    
    def print_data(self):
        print(self.users)
        print(self.tickets)
        print(self.purchase_orders)
        print(self.reservations)

    def __repr__(self):
        return (f"CoreService(users={len(self.users)}, tickets={len(self.tickets)}, "
                f"purchase_orders={len(self.purchase_orders)}, reservations={len(self.reservations)})")


