from User import User
class Admin(User):
    def __init__(self, username, password, email, phone_number, admin_id, permissions):
        super().__init__(username, password, email, phone_number)
        self.admin_id = admin_id  # string
        self.permissions = permissions  # List of strings

    def __repr__(self):
        return f"Admin(username={self.username}, admin_id={self.admin_id})"
