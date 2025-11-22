# this program is a simple example of how to send a message to the display
# except of control sum and value of length of the message and text every other value
# is set directly as text

import serial
import time
# this function prepares message by adding its begginign and ending (02 and 03) and control sum
def prepare_message(content):
    com = content
    sum = 0
    for value in content.split(" "):
        sum += int(value, 16)
    checksum = sum % 256
    checksum = str(hex(checksum))[2:].upper()
    # control sum is calculated by adding every value in the content of the message (except of beginning 02, ending 03 and control sum)
    # and then taking rest from division by 256
    new_checksum = ""
    for char in checksum:
        new_checksum += char.encode("cp852").hex()
        new_checksum += " "
    
    print("02 " + com + " " + new_checksum + "03")
    return("02 " + com + " " + new_checksum + "03")

# this functions takes string and then converts it to CP852 form and returns along with it value of its length 
# in a form required by the display
def text_to_hex(content):
    result = ""
    for char in content:
        result += char.encode("cp852").hex()
        result += " "
    return length_value(len(content)), result.upper()[:-1]

    
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
    inHex = (hex(length))[2:4].upper()
    if(length < 16):
        inHex = '0' + inHex
    return " " + inHex[0].encode("cp852").hex() + " " + inHex[1].encode("cp852").hex() + " "

def clear_screen(display_number):
    time.sleep(0.05) 
    message_content = "                  " 
    message_length_hex, message_hex = text_to_hex(message_content)     
                                                                                       # 5  6  7  8  9 10 11 12 13 14 15 16 
    message = prepare_message(displays_adresses[display_number] + message_length_hex + "38 30 30 30 31 32 30 30 36 30 30 30 " + message_hex)
    ser.write(bytes.fromhex(message))
    time.sleep(0.05) 
    message = prepare_message(displays_adresses[display_number] + message_length_hex + "38 30 31 30 31 32 30 30 36 30 30 30 " + message_hex)
    ser.write(bytes.fromhex(message))
    time.sleep(0.05) 
# used serial port, 9600 bps
ser = serial.Serial('COM3', 9600)


# max length of text value is 243 
# displays support CP852 so both Polish alphabet but also works with German, Czech, Slovak etc. 
# more information about the messages and how to do various things with text on displays is in communication.md
# this first example message displays message_content on display number 27, as scrolling text in two lines
message_content = "śmieszny bardzo bardzo długi tekst typu lorem ipsum dolor sit amet czy leci z nami pilot?" 
display_number = 20
message_length_hex, message_hex = text_to_hex(message_content)     
                                                                                   # 5  6  7  8  9 10 11 12 13 14 15 16 
message = prepare_message(displays_adresses[display_number] + message_length_hex + "38 30 30 31 37 32 30 30 36 30 30 31 " + message_hex)
ser.write(bytes.fromhex(message))

time.sleep(5) 


# you can set text on both lines, there should be a small time gap for displays to catch up
# this example message will set 
message_content = "Przystanek:" 
message_length_hex, message_hex = text_to_hex(message_content)     
                                                                                   # 5  6  7  8  9 10 11 12 13 14 15 16 
message = prepare_message(displays_adresses[display_number] + message_length_hex + "38 30 30 30 37 30 20 30 34 56 30 30 " + message_hex)
ser.write(bytes.fromhex(message))
time.sleep(0.1) 
message_content = "Rondo ONZ" 
message_length_hex, message_hex = text_to_hex(message_content)     
                                                                                   # 5  6  7  8  9 10 11 12 13 14 15 16 
message = prepare_message(displays_adresses[display_number] + message_length_hex + "38 30 31 32 37 30 30 30 36 30 30 30 " + message_hex)
ser.write(bytes.fromhex(message))


# this example message sets numbers "190" in two lines on the left and then a non-scrolling text in first line as centered
# and in second line scrolling text, the values 11 and 12 are set in a way that two-lines text on the left doesn't interfere
# with text on the right. This example is trying to simulate how similar display would behave in a bus
time.sleep(3)
clear_screen(display_number)

message_content = "190" 
message_length_hex, message_hex = text_to_hex(message_content)     
                                                                                   # 5  6  7  8  9 10 11 12 13 14 15 16 
message = prepare_message(displays_adresses[display_number] + message_length_hex + "38 30 30 30 37 32 30 32 34 30 30 30 " + message_hex)
ser.write(bytes.fromhex(message))
time.sleep(0.1) 
message_content = "->CH MARKI" 
message_length_hex, message_hex = text_to_hex(message_content)     
                                                                                   # 5  6  7  8  9 10 11 12 13 14 15 16 
message = prepare_message(displays_adresses[display_number] + message_length_hex + "38 30 30 30 37 30 31 36 36 30 30 30 " + message_hex)
ser.write(bytes.fromhex(message))
time.sleep(0.1) 
message_content = 'Trasa: Lazurowa-Człuchowska-Powstańców Śląskich-Górczewska-Leszno-al. "Solidarności"-Radzymińska'
message_length_hex, message_hex = text_to_hex(message_content)     
                                                                                   # 5  6  7  8  9 10 11 12 13 14 15 16 
message = prepare_message(displays_adresses[display_number] + message_length_hex + "38 30 31 32 37 30 31 36 36 30 30 33 " + message_hex)
ser.write(bytes.fromhex(message))

# this example message sets number "271" on the right in both lines and text "WARSZAWA Wsch.-" in first line and
# "-Berlin Gesund." on the right in second line. This example shows similiar thing as previous one
# but with text on the right, so it is controlled by positions 13 and 14.
# This example is trying to simulate how similar display would behave in a train
time.sleep(5)
clear_screen(display_number)


message_content = "Warszawa Wsch.-" 
message_length_hex, message_hex = text_to_hex(message_content)     
                                                                                   # 5  6  7  8  9 10 11 12 13 14 15 16 
message = prepare_message(displays_adresses[display_number] + message_length_hex + "38 30 30 30 37 30 30 32 35 30 30 30 " + message_hex)
ser.write(bytes.fromhex(message))
time.sleep(0.1) 
message_content = "-Berlin Gesund."
message_length_hex, message_hex = text_to_hex(message_content) 
print(message_content)    
                                                                                   # 5  6  7  8  9 10 11 12 13 14 15 16 
message = prepare_message(displays_adresses[display_number] + message_length_hex + "38 30 31 32 37 30 30 30 34 45 30 30 " + message_hex)
ser.write(bytes.fromhex(message))

time.sleep(0.1)

message_content = "271" 
message_length_hex, message_hex = text_to_hex(message_content)     
                                                                                   # 5  6  7  8  9 10 11 12 13 14 15 16 
message = prepare_message(displays_adresses[display_number] + message_length_hex + "38 30 30 30 37 34 35 30 36 30 30 30 " + message_hex)
ser.write(bytes.fromhex(message))

