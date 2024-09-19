class ContactFormular:

    def __init__(self, nume_prenume, email, telefon, mesaj):   # am sters proiect
        self.nume_prenume = nume_prenume
        self.email = email
        self.telefon = telefon
        self.proiect = [("la atelier", "la atelier"), ("next steps", "next steps"), ("pasi impreuna", "pasi impreuna"), ("community engagement", "community engagement")]   # lista de tupluri
        self.mesaj = mesaj

    def validare(self):
        # verificam daca toate campurile au fost completate
        if not all([self.nume_prenume, self.email, self.telefon, self.mesaj]):
            return False, "Toate campurile sunt obligatorii"
        else:
            return True, "Toate campurile au fost completate"
