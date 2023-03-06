arr = []
spaces = 0
space = " "
edit = ""
edit_temp_line = ''
vehicle_details = ['make', 'model', 'mileage', 'year', 'owner_info', 'ask_price', 'sell_price']
customer_details = [["name","phone number","selling price","address","make","model","year"],["company_name","phone number","selling price","adddress","make","model","year"]]
maintainance_info = ["customer name","phone number","make","model","address","service date"]
choice = 0
arr_vehicles = []
arr_appoinments = []

f = open("admin.txt","r")
g = f.readlines()
appoinment_details = ["Make","model","mileage","year","customer_name","appointment_date"]

for i in range (len(g)):
    j = g[i].split("|")
    arr_vehicles.append(j)



def view_vehicles():
    f = open("admin.txt", "r")
    file_content = f.readlines()
    file_content_len = len(file_content)

    for x in range(file_content_len):
        file_content_split = file_content[x].split("|")
        arr.append(file_content_split)

    for k in range(len(vehicle_details)):
        spaces = 15 - len(vehicle_details[k])
        if k == 0:
            print(space * 3, vehicle_details[k], space * spaces, end='')
        else:
            print(vehicle_details[k], space * spaces, end='')
    print()

    for i in range(file_content_len):
        print(i + 1, '.', end=" ")
        for y in range(8):
            spaces = 15 - len(arr[i][y])
            if y == 7:
                spaces = 0
            print(arr[i][y], space * spaces, end='')
    f.close()

def add_vehicle():
    edit_temp_line = ""
    f = open("admin.txt", "a")

    for x in range(len(vehicle_details)):
        e = "\n"
        edit_temp = str(input("Enter the vehicles " + vehicle_details[x] + " :"))
        if x == 6:
            edit_temp_line = edit_temp_line + edit_temp + "|\n"
        else:
            edit_temp_line = edit_temp_line + edit_temp + "|"

    f.write(edit_temp_line)
    f.close()

def edit_vehicle():
    f = open("admin.txt", "r")
    file_content = f.readlines()
    file_content_len = len(file_content)
    edit_temp_line = ""
    edit = int(input("Enter the line number of the vehicle you want to edit :"))
    print(arr[edit - 1])

    for i in range(len(vehicle_details)):
        edit_temp = str(input("Enter the vehicles " + vehicle_details[i] + " :"))
        if i == 6:
            edit_temp_line = edit_temp_line + edit_temp + "|" + "\n"
        else:
            edit_temp_line = edit_temp_line + edit_temp + "|"

        file_content[edit - 1] = edit_temp_line
        print(file_content)

    f = open("admin.txt", "w")
    for i in range(len(file_content)):
        f.write(file_content[i])
    f.close()

def buy_vehicle():
    customer_details_temp = []
    customer_details_string = ""
    vehicle = int(input("Enter the line number of the vehicle to be bought :"))
    print("please choose the customer type\n1. individual\n2. company")
    cus_type = int(input("Enter the customer type :"))

    for i in range(4):
        temp = str(input("Enter the customers " + customer_details[cus_type-1][i] + " :" ))
        customer_details_string = customer_details_string + temp + "|"


    for x in range (4):
        if x == 6:
            customer_details_string = customer_details_string + arr[vehicle-1][x] + "|\n"
        else:
            customer_details_string = customer_details_string + arr[vehicle - 1][x] + "|"


    f = open("customer_details.txt","a")
    f.write(customer_details_string)
    f.close

    f = open("admin.txt","r")
    file_content = f.readlines()
    del file_content[vehicle-1]

    f = open("admin.txt","w")
    for i in range (len(file_content)):
        f.write(file_content[i])
    f.close


def request_maintainance():
    maintainance_info_temp_string = ""

    for i in range (len(maintainance_info)-1):
        temp = str(input("Enter the " + maintainance_info[i] + " :"))
        maintainance_info_temp_string = maintainance_info_temp_string + temp + "|"

    maintainance_info_temp_string = maintainance_info_temp_string + "TBD" + "|\n"

    f = open("maintainance_requests.txt","a")
    f.write(maintainance_info_temp_string)
    f.close()

def view_maintainance_request():
    maintainance_info_temp = []
    f = open("maintainance_requests.txt", "r")
    file_content = f.readlines()
    file_content_len = len(file_content)

    for x in range(file_content_len):
        file_content_split = file_content[x].split("|")
        print(file_content_split)
        maintainance_info_temp.append(file_content_split)

    for k in range(len(maintainance_info)):
        spaces = 15 - len(maintainance_info[k])
        if k == 0:
            print(space * 3, maintainance_info[k], space * spaces, end='')
        else:
            print(maintainance_info[k], space * spaces, end='')
    print()

    for i in range(file_content_len):
        print(i + 1, '.', end=" ")
        for y in range(6):
            spaces = 15 - len(maintainance_info_temp[i][y])
            if y == 5:
                spaces = 0
            print(maintainance_info_temp[i][y], space * spaces, end='')
        print()
    f.close()

def assign_date_maintainance():
    edit_temp_line = ""
    f = open("maintainance_requests.txt", "r")
    file_content = f.readlines()
    file_content_len = len(file_content)
    edit_temp_line = ""
    edit = int(input("Enter the line number to assign a date :"))
    date = str(input("Enter the date to be assigned for the test drive :"))
    file_content_split = file_content[edit - 1].split("|")

    file_content_split[5] = date

    for x in range(len(file_content_split) - 1):
        if x == 5:
            edit_temp_line = edit_temp_line + file_content_split[x] + "|\n"
        else:
            edit_temp_line = edit_temp_line + file_content_split[x] + "|"
    print(edit_temp_line)
    file_content[edit - 1] = edit_temp_line

    f = open("maintainance_requests.txt", "w")
    for i in range(len(file_content)):
        f.write(file_content[i])
    f.close()

def mileage_asc():
    for i in range (len(arr_vehicles)-1,0,-1):
        for x in range (i):
          if int(arr_vehicles[x][2]) > int(arr_vehicles[x+1][2]):
              temp = arr_vehicles[x]
              arr_vehicles[x] = arr_vehicles[x+1]
              arr_vehicles[x+1] = temp

    for k in range(len(vehicle_details)):
        spaces = 15 - len(vehicle_details[k])
        if k == 0:
            print(space * 3, vehicle_details[k], space * spaces, end='')
        else:
            print(vehicle_details[k], space * spaces, end='')
    print()

    for i in range(len(arr_vehicles)):
        print(i + 1, '.', end=" ")
        for y in range(8):
            spaces = 15 - len(arr_vehicles[i][y])
            if y == 7:
                spaces = 0
            print(arr_vehicles[i][y], space * spaces, end='')
    f.close()

def mileage_dsc():
    for i in range (len(arr_vehicles)-1,0,-1):
        for x in range (i):
          if int(arr_vehicles[x][2]) < int(arr_vehicles[x+1][2]):
              temp = arr_vehicles[x]
              arr_vehicles[x] = arr_vehicles[x+1]
              arr_vehicles[x+1] = temp

    for k in range(len(vehicle_details)):
        spaces = 15 - len(vehicle_details[k])
        if k == 0:
            print(space * 3, vehicle_details[k], space * spaces, end='')
        else:
            print(vehicle_details[k], space * spaces, end='')
    print()

    for i in range(len(arr_vehicles)):
        print(i + 1, '.', end=" ")
        for y in range(8):
            spaces = 15 - len(arr_vehicles[i][y])
            if y == 7:
                spaces = 0
            print(arr_vehicles[i][y], space * spaces, end='')
    f.close()

def price_asc():
    for i in range (len(arr_vehicles)-1,0,-1):
        for x in range (i):
          if int(arr_vehicles[x][6]) > int(arr_vehicles[x+1][6]):
              temp = arr_vehicles[x]
              arr_vehicles[x] = arr_vehicles[x+1]
              arr_vehicles[x+1] = temp

    for k in range(len(vehicle_details)):
        spaces = 15 - len(vehicle_details[k])
        if k == 0:
            print(space * 3, vehicle_details[k], space * spaces, end='')
        else:
            print(vehicle_details[k], space * spaces, end='')
    print()

    for i in range(len(arr_vehicles)):
        print(i + 1, '.', end=" ")
        for y in range(8):
            spaces = 15 - len(arr_vehicles[i][y])
            if y == 7:
                spaces = 0
            print(arr_vehicles[i][y], space * spaces, end='')
    f.close()

def price_dsc():
    for i in range (len(arr_vehicles)-1,0,-1):
        for x in range (i):
          if int(arr_vehicles[x][6]) < int(arr_vehicles[x+1][6]):
              temp = arr_vehicles[x]
              arr_vehicles[x] = arr_vehicles[x+1]
              arr_vehicles[x+1] = temp

    for k in range(len(vehicle_details)):
        spaces = 15 - len(vehicle_details[k])
        if k == 0:
            print(space * 3, vehicle_details[k], space * spaces, end='')
        else:
            print(vehicle_details[k], space * spaces, end='')
    print()

    for i in range(len(arr_vehicles)):
        print(i + 1, '.', end=" ")
        for y in range(8):
            spaces = 15 - len(arr_vehicles[i][y])
            if y == 7:
                spaces = 0
            print(arr_vehicles[i][y], space * spaces, end='')
    f.close()

def view_appointments():
    space = " "

    f = open("appoinment.txt","r")
    file_content = f.readlines()
    file_content_len = len(file_content)

    for x in range(file_content_len):
        file_content_split = file_content[x].split("|")
        print(file_content_split)
        arr_appoinments.append(file_content_split)
        print(arr_appoinments)

    for k in range(len(appoinment_details)):
        spaces = 15 - len(appoinment_details[k])
        if k == 0:
            print(space * 3, appoinment_details[k], space * spaces, end='')
        else:
            print(appoinment_details[k], space * spaces, end='')
    print()

    for i in range(file_content_len):
        print(i + 1, '.', end=" ")
        for y in range(7):
            spaces = 15 - len(arr_appoinments[i][y])
            if y == 6:
                spaces = 0
            print(arr_appoinments[i][y], space * spaces, end='')
    f.close()

def request():
    arr_appoinments_temp = []
    arr_appoinments_temp_string = ''
    name = str(input("Enter your name :"))
    choice = int(input("Enter the line number of the relevant vehicle you want to test drive :"))

    for i in range (4):
        arr_appoinments_temp.append(arr_vehicles[choice-1][i])
    arr_appoinments_temp.append(name)
    arr_appoinments_temp.append("TBD")


    for x in range (len(arr_appoinments_temp)):
        if x == 5:
            arr_appoinments_temp_string = arr_appoinments_temp_string + arr_appoinments_temp[x] + "|\n"
        else:
            arr_appoinments_temp_string = arr_appoinments_temp_string + arr_appoinments_temp[x] + "|"

    f = open("appoinment.txt","a")
    f.write(arr_appoinments_temp_string)
    f.close()


def assign_appointment_date():
    edit_temp_line = ""
    f = open("appoinment.txt", "r")
    file_content = f.readlines()
    file_content_len = len(file_content)
    edit_temp_line = ""
    edit = int(input("Enter the line number to assign a date :"))
    date = str(input("Enter the date to be assigned for the test drive :"))
    print(arr_appoinments[edit - 1])
    print(file_content)
    file_content_split = file_content[edit-1].split("|")
    print (file_content_split)

    file_content_split[5] = date
    print(file_content_split)

    for x in range (len(file_content_split)-1):
        if x == 5:
            edit_temp_line = edit_temp_line + file_content_split[x] + "|\n"
        else:
            edit_temp_line = edit_temp_line + file_content_split[x] + "|"
    print(edit_temp_line)
    file_content[edit - 1] = edit_temp_line


    f = open("appoinment.txt", "w")
    for i in range(len(file_content)):
        f.write(file_content[i])
    f.close()

def view_maintainance_request():
    maintainance_info_temp = []
    f = open("maintainance_requests.txt", "r")
    file_content = f.readlines()
    file_content_len = len(file_content)

    for x in range(file_content_len):
        file_content_split = file_content[x].split("|")
        print(file_content_split)
        maintainance_info_temp.append(file_content_split)

    for k in range(len(maintainance_info)):
        spaces = 15 - len(maintainance_info[k])
        if k == 0:
            print(space * 3, maintainance_info[k], space * spaces, end='')
        else:
            print(maintainance_info[k], space * spaces, end='')
    print()

    for i in range(file_content_len):
        print(i + 1, '.', end=" ")
        for y in range(6):
            spaces = 15 - len(maintainance_info_temp[i][y])
            if y == 5:
                spaces = 0
            print(maintainance_info_temp[i][y], space * spaces, end='')
        print()
    f.close()



