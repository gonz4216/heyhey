# def myfun():
#   message = 'Hey enter password'
#   print(message)
#   password_input = input()
#   print("Password: " + password_input)

# myfun()



# # message = "Hey Please enter password"
# # print(message)

# # password_input = input()
# # print("Password:" + password_input)


# # message = "Please confirm password"
# # print(message)


# # password_input2 = input()
# # print("Password:" + password_input2)

# # if password_input == password_input2:
# #   print("Congrats on the password change")
# # else:
# #   print('Password wasnt the same please try again')
# #   message = " enter password"
# # print(message)

# # password_input = input()
# # print("Password:" + password_input)


# # message = "Please confirm password"
# # print(message)


# # password_input2 = input()
# # print("Password:" + password_input2)


username = input("What is your username: ")
password = input("What is your password: ")
password_stars = "*" * len(password)
password_len = len(password)
print(f"{username}, your password {password_stars} is {password_len} long letters long")

