import os
path = os.path.dirname(os.path.abspath(__file__))
new_file = open(path + "motto.txt","w")
new_file.write("Fiat Lux!")
new_file.close()
with open ("motto.txt","a") as file:
    file.write("\nLet there be light!")
file.close()
with open ("motto.txt", "r") as file:
    file.read()
file.close()
file = open("motto.txt", "r")
print(file.read())