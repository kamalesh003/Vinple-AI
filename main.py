
import subprocess

def execute_echo():
    subprocess.run(["python", "Echo.py"])

def execute_sel():
    subprocess.run(["python", "Browse.py"])

def exceute_tess():
    subprocess.run(["python", "tesseract.py"])

def show_commands():
    print("Available Commands: (Help Initialised)")
    print("1. sel - Surf Through Google")
    print("2. ocr - Perform Optical Character Recognition")
    print("3. echo - Perform Simple Chat Responses")


def main():
    while True:
        user_input = input("Enter a command: ").lower()

        if user_input == 'exit':
            print("Exiting program. Goodbye!")
            break
        elif user_input == 'echo':
            execute_echo()
        elif user_input == 'sel':
            execute_sel()
        elif user_input == 'ocr':
            exceute_tess()
        elif user_input == 'help':
            show_commands()
        else:
            print("Invalid command. Please enter 'echo', 'sel', or 'exit'.")

if __name__ == "__main__":
    main()
