from form_inregistrare.formular_contact import FormularInregistrare
# https://budgetandstuff.com/register/

def main():
    username = input("Introdu numele de utilizator: \n")
    first_name = input("Introdu prenumele: \n")
    last_name = input("Introdu numele: \n")
    email = input("Introdu email-ul: \n")
    password = input("Introdu parola: \n")
    confirm_password = input("Confirma parola: \n")
    formContact = FormularInregistrare(username, first_name, last_name, email, password, confirm_password)

    # verificam daca parolele coincid
    parole_coincid, mesaj = formContact.validareParola()

    # validam si trimitem formularul completat
    # formular_valid, mesaj = formContact.validare()

    # print(formContact.validare())     # DEBUGGING


    # if formular_valid:
    #     # print("Mesajul a fost trimis")
    #     print("Mesaj de confirmare: ", mesaj)
    # else:
    #     print("Eroare: ", mesaj)

    if parole_coincid:
        # print("Mesajul a fost trimis")
        print("Mesaj de confirmare: parolele coincid.", mesaj)
    else:
        print("EROARE! Parolele nu coincid!", mesaj)




main()  # = buton Trimite

