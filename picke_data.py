import pickle
from pathlib import Path
from ticket import Ticket
from purchaseorder import PurchaseOrder
from User import User
from eventreserve import EventReservation
from CoreService import CoreService

# File paths for storing mock data
DATA_DIR = Path("mock_data")
DATA_DIR.mkdir(exist_ok=True)
USER_FILE = DATA_DIR / "users.pkl"
TICKET_FILE = DATA_DIR / "tickets.pkl"
ORDER_FILE = DATA_DIR / "purchase_orders.pkl"
RESERVATION_FILE = DATA_DIR / "reservations.pkl"

# Sample data generator
def generate_sample_data():
    from datetime import datetime

    # Users
    sample_users = [
        User("john_doe", "password123", "john@example.com", "1234567890"),
        User("jane_doe", "securepass", "jane@example.com", "0987654321"),
        User("superuser", "root", "root@example.com", "0987654321")
    ]

    # Tickets
    sample_tickets = [
        Ticket("T1", "Single-Day Pass", 275.0, "1 Day", 0.0, "Valid only on selected date"),
        Ticket("T2", "Two-Day Pass", 480.0, "2 Days", 10.0, "Cannot be split over multiple trips"),
        Ticket("T3", "Annual Membership", 1840.0, "1 Year", 15.0, "Must be used by the same person"),
        Ticket("T4", "Child Ticket", 185.0, "1 Day", 0.0, "Valid only on selected date, must be accompanied by an adult")
    ]

    # Purchase Orders
    #def __init__(self, order_id, user, ticket, purchase_date, quantity):
    sample_orders = [
        PurchaseOrder("O1", sample_users[0], sample_tickets[0], datetime.now() , 5),
        PurchaseOrder("O2", sample_users[1], sample_tickets[1],  datetime.now() , 10)
    ]

    # Reservations
    #def __init__(self, reservation_id, user, event_name, reservation_date, status):
    sample_reservations = [
        EventReservation("R1", sample_users[0], "Fireworks Show", datetime.now(), "Mone"),
        EventReservation("R2", sample_users[1], "VIP Lounge", datetime.now() , "None")
    ]

    return {
        "users": sample_users,
        "tickets": sample_tickets,
        "purchase_orders": sample_orders,
        "reservations": sample_reservations
    }

# Save data to pickle files
def save_mock_data(users, tickets, orders, reservations):
    with open(USER_FILE, "wb") as uf, open(TICKET_FILE, "wb") as tf, \
            open(ORDER_FILE, "wb") as of, open(RESERVATION_FILE, "wb") as rf:
        pickle.dump(users, uf)
        pickle.dump(tickets, tf)
        pickle.dump(orders, of)
        pickle.dump(reservations, rf)

# Load data from pickle files
def load_mock_data():
    users, tickets, orders, reservations = [], [], [], []

    if USER_FILE.exists():
        with open(USER_FILE, "rb") as uf:
            users = pickle.load(uf)
    if TICKET_FILE.exists():
        with open(TICKET_FILE, "rb") as tf:
            tickets = pickle.load(tf)
    if ORDER_FILE.exists():
        with open(ORDER_FILE, "rb") as of:
            orders = pickle.load(of)
    if RESERVATION_FILE.exists():
        with open(RESERVATION_FILE, "rb") as rf:
            reservations = pickle.load(rf)

    return users, tickets, orders, reservations

# Initialize the mock service with loaded or sample data
def initialize_mock_service(service):
    users, tickets, orders, reservations = load_mock_data()

    # Load data into service
    data = generate_sample_data()
    service.users = users or data["users"]
    service.tickets = tickets or data["tickets"]
    service.purchase_orders = orders or data["purchase_orders"]
    service.reservations = reservations or data["reservations"]

# Usage
if __name__ == "__main__":
    # Create a CoreService instance
    mock_service = CoreService()

    # Initialize it with data
    initialize_mock_service(mock_service)

    # Simulate saving data on close
    save_mock_data(mock_service.users, mock_service.tickets, mock_service.purchase_orders, mock_service.reservations)

    print("Mock data initialized and saved successfully.")
