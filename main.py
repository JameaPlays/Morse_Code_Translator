# Morse Code Dictionary
TEXT_TO_MORSE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                      'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                      'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                      'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
                      '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ', ': '--..--',
                      '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': ' '}

MORSE_TO_TEXT_DICT = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
                      '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
                      '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
                      '-.--': 'Y', '--..': 'Z', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5',
                      '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0', '--..--': ', ',
                      '.-.-.-': '.', '..--..': '?', '-..-.': '/', '-....-': '-', '-.--.': '(', '-.--.-': ')', ' ': ' '}


def text_to_morse():
    """Translates normal text to morse code."""
    user_input = input('Type the message to be converted to Morse Code.\n').upper()
    converted_text = ""
    for char in user_input:
        if char == " ":
            converted_text += "| "
        else:
            converted_text += TEXT_TO_MORSE_DICT[char]
            converted_text += " "
    return converted_text


def morse_to_text():
    """Translate morse code to normal text"""
    user_input = input('Type the message to be converted to Text.\n'
                       'Use space to separate each character and "|" to separate each word.\n')
    # Splits the user input into characters
    input_list = user_input.split(" ")
    converted_text = ""
    for char in input_list:
        if char == " ":
            pass
        elif char == '|':
            converted_text += " "
        else:
            converted_text += MORSE_TO_TEXT_DICT[char]
    return converted_text


converter_mode = input("A) Text to Morse Code\n"
                       "B) Morse Code to Text\n"
                       "What would you like to convert? Type A or B: ").upper()

running = True
while running:
    if converter_mode == "A":
        print(text_to_morse())
        break
    elif converter_mode == "B":
        print(morse_to_text())
        break
    else:
        print("Invalid input, please try again.")
