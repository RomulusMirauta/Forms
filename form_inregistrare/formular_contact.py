class FormularInregistrare:

    def __init__(self, username, first_name, last_name, email, password, confirm_password):   # del proiect
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.confirm_password = confirm_password

    def validare(self):
        # verificam daca toate campurile au fost completate
        if not all([self.username, self.first_name, self.last_name, self.email, self.password, self.confirm_password]):
            return False, "Toate campurile sunt obligatorii!"
        else:
            return True, "Toate campurile au fost completate."

    def validareParola(self):
        # verificam daca password = confirm_password
        if self.password != self.confirm_password:
            return False, "Parolele nu coincid!"
        else:
            return True, "Parolele coincid."

# add username
# del nume_prenume
# add first_name
# add last_name
# del telefon
# add password
# add confirm_password
# del proiect
