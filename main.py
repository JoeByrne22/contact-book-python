class Contact:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def __str__(self):
        return "~".join([self.first_name, self.last_name, self.email])

address_book = []
try:
    with open("save.txt") as save_file:
        for contact in save_file:
            address_book.append(Contact(*contact.split("~")))
except FileNotFoundError as fefe:
    pass

print("Hello I am an addressbook! What do you want to do?\n1.Add contact")
print("2.Print out contacts\n3.Search for and edit a contact\n4.Exit\n")
while True:
    choice = int(input("Choice: "))
    if choice == 1:
        address_book.append(Contact(input("First name?"), input("Last name?"), input("Phone number?"), input("Email?")))
    elif choice == 2:
        print(*[contact for contact in address_book], sep="\n")
    elif choice == 3:
        pass
    elif choice == 4:
        with open("save.txt", "w") as save_file:
            for contact in address_book:
                save_file.write(str(contact) + "\n")
            break