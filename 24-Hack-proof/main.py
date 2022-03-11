import os

# Hack-proof

# Create a program that will only open a text document if the correct password is entered. The user should choose the username and password first and it should also verify
# the password before allowing it.

def clearScreen():
  os.system('clear')

USERNAME = 'pawelpow'
PASSWORD = 'Pawel_2022'

class SecretsManager:
  def fetchSecret(username, password):
    if USERNAME == username and PASSWORD == password:
      with open('secrets.txt', 'r') as f:
        fileContent = f.read()
        return fileContent
    
    return 'Access Denied'

def main():
  username = input('Enter admin username: ')
  password = input('Enter admin password: ')

  secret = SecretsManager.fetchSecret(username, password)
  clearScreen()

  print(secret)

if __name__ == '__main__':
  main()