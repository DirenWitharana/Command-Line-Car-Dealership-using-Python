import functions
def admin():
    print ("1. Before sales\n2. Sales and After sales")
    m_option = int(input("Enter your option :"))

    if m_option == 1:
        print("1. Enter '1' to check added vehicles\n2. Enter '2' to add a new vehicle\n3. Enter '3' to edit vehicle information")
        option = int(input("Enter your option :"))

        if option == 1:
            functions.view_vehicles()

        if option == 2:
            functions.view_vehicles()
            functions.add_vehicle()

        if option == 3:
            functions.view_vehicles()
            functions.edit_vehicle()
    if m_option == 2:
        print("1. Sell vehicle\n2. Maintaince of vehicle")
        option = int(input("Enter your option :"))
        if option == 1:
            functions.view_vehicles()
            functions.buy_vehicle()
        if option == 2:
            functions.view_maintainance_request()
            functions.assign_date_maintainance()

def customer():
    print("Welcome to the car dealership\n1. Enter '1' to view available cars\n2. Enter '2' for test drive\n3. Enter '3' for maintainance")
    m_option = int(input("Enter your option :"))

    if m_option == 1:
        functions.view_vehicles()
        print("Would you like to sort the data?\nplease choose the criteria you want to sort in\n1. mileage\n2. price")
        option_1 = int(input("Enter your option :"))

        if option_1 == 1:
            print("would you like ascending order or descending order\n1. ascending order\n2. descending order")
            option_2 = int(input("Enter your option :"))
            if option_2 == 1:
                functions.mileage_asc()
            elif option_2 == 2:
                functions.mileage_dsc()

        elif option_1 == 2:
            print("would you like ascending order or descending order\n1. ascending order\n2. descending order")
            option_2 = int(input("Enter your option :"))
            if option_2 == 1:
                functions.price_asc()
            elif option_2 == 2:
                functions.price_dsc()


    if m_option == 2:
        print("1. Enter '1' to book test drive\n2. Enter '2' for status on test drive")
        option_3 = int(input("Enter your choice :"))
        if option_3 == 1:
            functions.view_vehicles()
            functions.request()

        elif option_3 == 2:
            functions.view_appointments()

    if m_option == 3:
        print("1. Enter '1' to request maintainance\n2. Enter '2' for status on maintainance")
        option_3 = int(input("Enter your choice :"))
        if option_3 == 1:
            functions.request_maintainance()

        elif option_3 == 2:
            functions.view_maintainance_request()

def technician():
    technician_details = ["make", "model", "cost", "description"]

    edit_temp_line = ""
    f = open("technician.txt", "a")

    for x in range(len(technician_details)):
        e = "\n"
        edit_temp = str(input("Enter the " + technician_details[x] + " :"))
        if x == 3:
            edit_temp_line = edit_temp_line + edit_temp + "|\n"
        else:
            edit_temp_line = edit_temp_line + edit_temp + "|"

    f.write(edit_temp_line)
    f.close()