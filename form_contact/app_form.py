from form_contact.formular_contact import ContactFormular
# https://www.fundatiapascupas.ro/contact/

def main():
    nume_prenume = input("Introdu numele: \n")
    email = input("Introdu email-ul: \n")
    telefon = input("Introdu numarul de telefon: \n")
    mesaj = input("Introdu mesajul: \n")
    formContact = ContactFormular(nume_prenume, email, telefon, mesaj)
    print("Alege proiectul in care vrei sa te implici: ")

    for i, (proiect, proiect_ales) in enumerate(formContact.proiect):
        print(f"{i+1}. {proiect_ales}")

    # print(formContact.proiect)

    while True:
        try:
            nr_proiect = int(input("Scrie numarul proiectului ales: \n"))
            if 1 <= nr_proiect <= len(formContact.proiect):
                formContact.proiect = formContact.proiect[nr_proiect - 1][0]
                break
            else:
                print("Numarul introdus nu este valid")
        except ValueError:
            print("Te rugam sa introduci un numar astfel incat sa stim care este proiectul in care vrei sa te implici")

    # validam si trimitem formularul completat
    formular_valid, mesaj = formContact.validare()

    # print(formContact.validare())     # DEBUGGING

    if formular_valid:
        # print("Mesajul a fost trimis")
        print("Mesaj de confirmare: ", mesaj)
    else:
        print("Eroare: ", mesaj)



main()  # = buton Trimite

