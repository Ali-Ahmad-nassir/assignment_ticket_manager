from datetime import datetime

class EventReservation:
    def __init__(self, reservation_id, user, event_name, reservation_date, status):
        self._reservation_id = reservation_id  # string
        self._user = user  # Reference to User
        self._event_name = event_name  # string
        self._reservation_date = reservation_date  # datetime
        self._status = status  # string (e.g., "Confirmed")

    # Getter and Setter for reservation_id
    def get_reservation_id(self):
        return self._reservation_id

    def set_reservation_id(self, value):
        self._reservation_id = value

    # Getter and Setter for user
    def get_user(self):
        return self._user

    def set_user(self, value):
        self._user = value

    # Getter and Setter for event_name
    def get_event_name(self):
        return self._event_name

    def set_event_name(self, value):
        self._event_name = value

    # Getter and Setter for reservation_date
    def get_reservation_date(self):
        return self._reservation_date

    def set_reservation_date(self, value):
        if isinstance(value, datetime):
            self._reservation_date = value
        else:
            raise ValueError("reservation_date must be a datetime object")

    # Getter and Setter for status
    def get_status(self):
        return self._status

    def set_status(self, value):
        if value in ["Confirmed", "Pending", "Cancelled"]:  # Example of possible valid statuses
            self._status = value
        else:
            raise ValueError("status must be one of: 'Confirmed', 'Pending', or 'Cancelled'")

    # __repr__ method for string representation
    def __repr__(self):
        return f"EventReservation(event_name={self._event_name}, status={self._status})"
