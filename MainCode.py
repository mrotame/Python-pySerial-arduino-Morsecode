import serial
import time

code = {'A': '.-',     'B': '-...',   'C': '-.-.', 
	'D': '-..',    'E': '.',      'F': '..-.',
	'G': '--.',    'H': '....',   'I': '..',
	'J': '.---',   'K': '-.-',    'L': '.-..',
	'M': '--',     'N': '-.',     'O': '---',
	'P': '.--.',   'Q': '--.-',   'R': '.-.',
	'S': '...',    'T': '-',      'U': '..-',
	'V': '...-',   'W': '.--',    'X': '-..-',
	'Y': '-.--',   'Z': '--..',

	'0': '-----',  '1': '.----',  '2': '..---',
	'3': '...--',  '4': '....-',  '5': '.....',
	'6': '-....',  '7': '--...',  '8': '---..',
	'9': '----.' 
}

port = "COM4"
speed = 9600
connect = serial.Serial(port, speed)

while True:
	print("Digite a palavra")
	print('"/quit" para sair')
	word = input()
	if word == "/quit":
		break

	result = []
	for item in word:
		result.append(code[item.upper()]) 
	print ("traduzido:", result)
	print ("Emitindo para o arduino...")

	for lista in result:
		time.sleep(0.7)
		for item in lista:

			time.sleep(0.3)
			if item == ".":
				opt = "1"
				connect.write(opt.encode())
				time.sleep(0.1)
				opt = "0"
				connect.write(opt.encode())
			elif item =="-":
				opt = "1"
				connect.write(opt.encode())
				time.sleep(0.5)
				opt = "0"
				connect.write(opt.encode())

connect.close()

