def prepare_message(content):
    com = content
    sum = 0
    for value in content.split(" "):
        sum += int(value, 16)
    checksum = sum % 256
    checksum = (str(hex(checksum))[2:]).upper()
    print(checksum)
    # suma kontrolna to suma tego co w komunikacie modulo 256
    new_checksum = ""
    for char in checksum:
        new_checksum += (char).encode("cp852").hex()
        new_checksum += " "
    return("02 " + com + " " + new_checksum + " 03")

def text_to_hex(content):
    result = ""
    for char in content:
        result += char.encode("cp852").hex()
        result += " "
    return length_value(len(content)), result.upper()
def select_line(selection):
    if(selection == 1):
        return "31"
    elif(selection == 2):
        return "32"
def select_text_align(selection):
    if(selection == "l"):
        return "30"
    elif(selection == "c"):
        return "31"
    elif(selection == "r"):
        return "32"
    
displays_adresses = {
    27: "36 46",
    26: "36 42",
    25: "36 37",
    24: "36 33",
    23: "35 46",
    22: "35 42",
    21: "35 37",
    20: "35 33",
    19: "34 46",
    18: "34 42",
    17: "34 37",
    16: "34 33",
    16: "34 33",
    15: "33 45",
    14: "33 41",
    13: "33 37",
    12: "33 33",
    11: "32 46",
    10: "32 42",
    9: "32 37",
    8: "32 33",
    7: "31 45",
    6: "31 41",
    5: "31 36",
    4: "31 32",
    3: "30 45",
    2: "30 41",
    1: "30 37",
}
def length_value(length):
    length += 12
    inHex = ((hex(length))[2:4]).upper()
    return " " + (inHex[0]).encode("cp852").hex() + " " + (inHex[1]).encode("cp852").hex() + " "
import serial
#trzeba wybrać stosowny port pod którym jest port szeregowy na RS-485
ser = serial.Serial('COM3', 9600)

# 1 i 2 pozycja - adres
# 3 i 4 - długość tekstu
# 5 i 6 - (nie wiadomo)
# 7 - wybór 1 lub 2 linijki wyświetlania 30/31 (używając tekstu na dwie linijki należy wybrać linijkę 1)
# 8 - pozycja tekstu (30 - do lewej, 31 - środkuj, 32 - do prawej)
# 9 - (nie wiadomo)
# 10 - rodzaj fontu (30, 31 - są na jedną linijkę, 32 - dwie linijki)
# 11 - pozycja
# 13 - jak bardzo do lewej
# 14 - jak bardzo do prawej (56 maks)
# 15 - ilość scrollowań tekstu dziesiątki
# 16 - ilość scrollowań tekstu jednostki (jak będzie na 0 tj. 30 to na stałe jest tekst)

#tekst - maksymalna długość - 243 znaki
message_content = "śmieszny bardzo bardzo dlugi tekst typu lorem ipsum dolor sit amet czy leci z nami pilot?" 
display_number = 27 #numer wyświetlacza ustawiany deepswitchami
message_length_hex, message_hex = text_to_hex(message_content)                     # 5  6  7  8  9 10 11 12 13 14 15 16 
message = prepare_message(displays_adresses[display_number] + message_length_hex + "38 30 31 31 37 30 20 30 34 56 20 31 " + message_hex[:-1])
print(message)
ser.write(bytes.fromhex(message))
