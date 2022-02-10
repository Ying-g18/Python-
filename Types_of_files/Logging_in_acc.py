
def credential_(data):
    data = list(map(lambda d: d.strip("\n "), data))
    tmp = []
    credentials = {}
    for item in data:
        if "name" not in item:
            tmp.append(item)
    for i in range(0, len(tmp), 2):
        credentials[tmp[i].split(" : ")[1]] = tmp[i+1].split(" : ")[1]
    return credentials


with open("credentials.txt", "a") as f:
    pass
with open("credentials.txt", "r") as file:
    data = file.readlines()

credential = credential_(data)
def create_account():
    name = input("Enter your fullname: ")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username not in credential.keys():
        with open("credentials.txt", "a+") as f:
            f.write(f"name : {name}\n username : {username}\n password : {password}")

def login_account():
    username = input("Enter your username : ")
    password = input("Enter your password : ")
    if username not in credential.keys():
        wanna = input("Invalid username ! Do you want to create an account [y/n] : ")
        if wanna == 'y':
            create_account()
        elif wanna == "n":
            print("Piss off !")
    elif password == credential[username]:
        print("You have logged in !")
    else:
        print("Wrong username or password ")

if __name__ == "__main__":
    choice = input("Do you want to login or create new account [login/create] : ")
    if choice.lower() == "create":
        create_account()
    if choice.lower() == "login":
        login_account()