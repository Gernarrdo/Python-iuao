# Funzioni
import random
# Variabili
elementi = "123456789qwertyuiopasdfghjklzxcvbnm?ì!èòàù£$%&"
lunghezza = int(input("Quanto vuoi lunga la password? "))
password = ""

# Programma Principale ( il codice )
for i in range(lunghezza):
    password += random.choice(elementi)

print(password)