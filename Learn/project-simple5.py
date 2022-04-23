log_in = False
while(log_in == False):
    log_user_name = input("Username: ")
    if log_user_name != "root":
        print("Username invalid")
    else:
        log_password = input("Password: ")
        if log_password == "pass":
            log_in = True
            print("Success")
        else:
            print("Password incorrect")