class Contact:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def __str__(self):
        return "name:" + self.first_name + ' ' + self.last_name + " email: " + self.email

address_book = []

try:
    with open("save.txt") as save_file:
        for contact in save_file:
            address_book.append(Contact(*contact.split("~")))
except FileNotFoundError as fefe:
    pass

print("Hello I am an addressbook! What do you want to do?\n1.Add contact\n2.Print out contacts\n3.Exit\n")
while True:
    choice = int(input("Choice: "))
    if choice == 1:
        address_book.append(Contact(input("First name?"), input("Last name?"), input("Email?")))
    elif choice == 2:
        print(*[contact for contact in address_book], sep="\n")
    elif choice == 3:
        with open("save.txt", "w") as save_file:
            for contact in address_book:
                save_file.write(str(contact) + "\n")
            break