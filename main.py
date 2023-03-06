import user_roles
user = 0

print ("Welcome!\nPlease select your role to continue\n1. Admin\n2. Customer\n3. Owner\n4. Technician")
user = int(input("Enter the number relevant to your role :"))

if user == 1:
    user_roles.admin()

elif user == 2:
    user_roles.customer()

elif user == 4:
    user_roles.technician()
