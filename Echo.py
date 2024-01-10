from rich.console import Console
from rich.prompt import Prompt
import pyttsx3
import datetime
import spacy
import spacy.cli

# Download the spaCy English NLP model if not already installed
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    print("Downloading 'en_core_web_sm' model...")
    spacy.cli.download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

# Initialize speech engine outside the loop
engine = pyttsx3.init()

def extract_entities(user_input):
    doc = nlp(user_input)
    return [ent.text for ent in doc.ents]

def chatbot_response(user_input):
    entities = extract_entities(user_input)
    user_input_lower = user_input.lower()

    if any(keyword in user_input_lower for keyword in ["hello", "hi"]):
        return "Hello, how are you doing?"
    elif "how are you" in user_input_lower:
        return "I'm just a computer program, but thanks for asking!"
    elif "your name" in user_input_lower:
        return "I'm Vinple AI."
    
    elif any(keyword in entities or keyword in user_input_lower for keyword in ["date", "day", "time"]):
        if any(date_keyword in user_input_lower for date_keyword in ["date", "today"]):
            current_date = datetime.datetime.now().strftime("%Y-%m-%d")
            return f"Today's date is {current_date}."
        elif any(day_keyword in user_input_lower for day_keyword in ["day", "today"]):
            current_day = datetime.datetime.now().strftime("%A")
            return f"Today is {current_day}."
        elif any(time_keyword in user_input_lower for time_keyword in ["time", "now"]):
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            return f"The current time is {current_time}."
    
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase or ask something else?"


def generate_cli_box(message, is_user_input=True):
    console = Console()

    if is_user_input:
        console.print(f"[bold magenta]User Input:[/bold magenta] {message}")
    else:
        console.print(f"[bold white on blue]AI Response:[/bold white on blue] {message}")

def speak(text, voice_id):
    try:
        engine.setProperty('rate', 150)
        engine.setProperty('voice', voice_id)
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Error during speech synthesis: {e}")

def ai_interaction_cli():
    console = Console()
    console.print("[cyan]Welcome to Vinple AI Interaction CLI![/cyan]")

    # Print available voices for reference
    voices = engine.getProperty('voices')

    console.print("[bold]Available Voices:[/bold]")
    for voice in voices:
        console.print(f"ID: {voice.id}, Name: {voice.name}, Lang: {voice.languages[0] if voice.languages else 'N/A'}")

    # Choose the appropriate voice ID for Zira on your system
    zira_voice_id = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0'

    while True:
        user_input = Prompt.ask("[bold magenta]Type your message[/bold magenta] (type 'exit' to quit):", default="")

        if user_input.lower() == 'exit':
            console.print("[cyan]Exiting Vinple AI Interaction CLI. Goodbye![/cyan]")
            break

        # Use the chatbot to generate AI response
        ai_response = chatbot_response(user_input)

        generate_cli_box(user_input)
        generate_cli_box(ai_response, is_user_input=False)

        # Use Microsoft Zira voice to speak the AI response if the chosen voice ID exists
        if any(voice.id == zira_voice_id for voice in voices):
            speak(f"I said: {ai_response}", zira_voice_id)
        else:
            console.print("[bold red]Error:[/bold red] Chosen voice ID not found.")

if __name__ == "__main__":
    ai_interaction_cli()




