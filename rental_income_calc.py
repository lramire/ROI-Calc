

class Property():

    def __init__(self, name): #create list for income/expense. User inputs cost
        self.name = name
        self.cost = 0
        self.income = []
        self.expense= []
    

    def expenses(self): #multiple expenses
        self.mortgage = int(input("Enter mortgage amount here: "))
        self.insurance = int(input("Enter insurance amount here: "))
        self.tax = int(input("Enter tax amount here: "))
        self.utilites = int(input("Enter utilites amount here: "))
        self.hoa = int(input("Enter hoa amount here: "))
        self.repairs = int(input("Enter repairs amount here: "))
        self.capex = int(input("Enter capital expenditure amount here: "))
        self.pmanager = int(input("Enter pmanager amount here: "))
        self.vacancy = int(input("Enter vacancy amount here: "))



    def income(self, rent, laundry, parking, pets): #some income sources of a rental
        self.rent = rent
        self.laudry = laundry
        self.carport = parking
        self.pets = pets

    def roi_calculation(self):
        total_expenses = sum(expense.amount for expense in self.expenses)
        total_incomes = sum(income.amount for income in self.incomes)
        self.roi = ((total_incomes - total_expenses) / self.purchase_price) * 100


class User():
    def __init__(self, username):
        self.prop_list = []  # hold properties user has
        self.username = username # allow specific user to access their info

    def add_property(self, add_prop):
        self.prop_list.append(add_prop) #appending to property list
 


def run():
    users = []

    while True:
        print("\n")
        print("\t ------ Behold the ROI Rental Income Calculator ------")
        print("Enter 'new' to create a new user")
        print("Enter 'login' to login to your user")
        print("Enter 'exit' to exit the calculator")

        choice = input("Enter your response here: ")

        if choice == "new":
            username = input("Enter username here: ")
            user = User(username)
            users.append(user)
            print(f"{username} has been created.")

        elif choice == "login":
            print("Enter username here: ")
            if username in users:
                user = users[username]

                while True:
                    print("Enter 'add' to add property")
                    print("Enter 'exit' to return to the main menu, or exit completely..bugs to work out still")
                    print("Enter 'calculate' to crunch numbers on that sweet property")

                    login_choice = input("Enter your response here: ")

                    if login_choice == "add":
                        print("Enter new property")
                        name = input("Enter new property name here: ")
                        cost = input("Enter new property cost here: ")
                        add_prop = Property(name, cost)
                        user.add_property = User(name, cost)
                        print(f"{name} has been created")

                        print("Enter expected income from new property.")
                        total_income = int(input(" ")) #Avenues of new property income going here


                    elif login_choice == "calculate":
                        if not user.prop_list:
                            print("Please add a property first")






        elif choice == "exit":
            print("Happy renting!")
            break
        else:
            print("Error. Please try again.")


run()