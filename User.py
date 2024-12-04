class User:
    def __init__(self, username, password, email, phone_number):
        self._username = username  # string
        self._password = password  # string (hashed for security)
        self._email = email  # string
        self._phone_number = phone_number  # string
        self._purchase_history = []  # List of PurchaseOrder objects

    # Methods for username
    def get_username(self):
        return self._username

    def set_username(self, username):
        if isinstance(username, str) and username.strip():
            self._username = username
        else:
            raise ValueError("Username must be a non-empty string.")

    # Methods for password
    def get_password(self):
        return self._password

    def set_password(self, password):
        if isinstance(password, str) and password.strip():
            self._password = password  # In practice, hash the password here
        else:
            raise ValueError("Password must be a non-empty string.")

    # Methods for email
    def get_email(self):
        return self._email

    def set_email(self, email):
        if isinstance(email, str) and "@" in email:
            self._email = email
        else:
            raise ValueError("Email must be a valid email address.")

    # Methods for phone number
    def get_phone_number(self):
        return self._phone_number

    def set_phone_number(self, phone_number):
        if isinstance(phone_number, str) and phone_number.strip():
            self._phone_number = phone_number
        else:
            raise ValueError("Phone number must be a non-empty string.")

    # Methods for purchase history
    def get_purchase_history(self):
        return self._purchase_history

    def set_purchase_history(self, purchase_history):
        if isinstance(purchase_history, list):
            self._purchase_history = purchase_history
        else:
            raise ValueError("Purchase history must be a list.")

    def __repr__(self):
        return f"User(username={self._username}, email={self._email}, pass={self._password})"
