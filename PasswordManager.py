from cryptography.fernet import Fernet


def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
       key_file.write(key)

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)
    
def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:",
                 fer.decrypt(passw.encode()).decode())

def add():
    name = input('Account name: ')
    pwd = input('Password: ')
    
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
  mode = input("Do you want to add a password or view exisiting passwords (v for view, a for add, q for quit")

  if mode == 'q':
      break

  if mode == "v":
      pass

  elif mode == "a":
      add()

  else:
      print("Invalid input")
      continue
    
