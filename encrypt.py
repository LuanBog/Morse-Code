import pyperclip
import sys

morse_dict = {"a": "·−",  "b": "−···", "c": "−·−·", "d": "−··", "e": "·", "f": "··−·", "g": "−−·", "h": "····", "i": "··", "j": "·−−−", "k": "−·−", "l": "·−··", "m": "−−", "n": "−·", "o": "−−−", "p": "·−−·", "q": "−−·−", "r": "·−·", "s": "···", "t": "−", "u": "··−", "v": "···−", "w": "·−−", "x": "−··−", "y": "−·−−", "z": "−−··", "1": "·−−−−", "2": "··−−−", "3": "···−−", "4": "····−", "5": "·····", "6": "−····", "7": "−−···", "8": "−−−··", "9": "−−−−·", "0": "−−−−−", ",": "−−··−−", ".": "·−·−·−", "/": "−··−·", "?": "··−−··", "!": "−·−·−−", "@": "·−−·−·", "&": "·−···", "(": "−·−−·", ")": "−·−−·−", "−": "−····−", "+": "·−·−·", "\"": "·−··−·", "\'": "·−−−−·", ";": "−·−·−·", ":": "−−−···"}

def clipboard(text):
	pyperclip.copy(text)
	pyperclip.paste()

def translate(n):
    translation = ""

    n = str(n)
    n = n.lower()
    
    for letter in n:
        if letter.lower() in morse_dict:
            translation = translation + morse_dict[letter.lower()] + " "
        else:
            translation = translation + letter
    
    return translation

def translate_to_valid(morse):
	# new = morse.replace("·", ".")
	# new = morse.replace("−", "-")
	new = morse
	new = new.replace("·", ".")
	new = new.replace("−", "-")

	return new

if __name__ == "__main__":
	if len(sys.argv) > 1:
		phrase = str(sys.argv[1])
	
		translation = translate(phrase)

		print("\nMorse Code: " + translation)
		print("\nComputer Translation: " + translate_to_valid(translation))

		clipboard_choice = input("\nCopy Morse Code/Computer Translation:\n(mc/ct): ")

		if clipboard_choice.lower() == "mc":
			clipboard(translation)
		elif clipboard_choice.lower() == "ct":
			clipboard(translate_to_valid(translation))

			sys.exit()

	print("Morse Code Encrypter\n")

	phrase = input("Enter Plaintext: ")

	translation = translate(phrase)

	print("\nMorse Code: " + translation)
	print("\nComputer Translation: " + translate_to_valid(translation))

	clipboard_choice = input("\nCopy Morse Code/Computer Translation:\n(mc/ct): ")

	if clipboard_choice.lower() == "mc":
		clipboard(translation)
	elif clipboard_choice.lower() == "ct":
		clipboard(translate_to_valid(translation))

	sys.exit()

