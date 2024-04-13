import tkinter as tk
from tkinter import messagebox
from boto3 import Session
import boto3

root = tk.Tk()
root.geometry("400x300")
root.title("Text to Speech Converter - Amazon Polly")


# Styling
bg_color = "#f0f0f0"
entry_bg_color = "#ffffff"
button_bg_color = "#4caf50"
button_fg_color = "#ffffff"

root.config(bg=bg_color)

# Text Entry
text_entry = tk.Text(root, height=10, wrap="word", bg=entry_bg_color)
text_entry.pack(pady=10, padx=10, fill="both", expand=True)

# Function to convert text to speech
def convert_to_speech():
    aws_mag_con = boto3.session.Session(profile_name='default')
    client = aws_mag_con.client(service_name='polly', region_name='us-east-1')

    text = text_entry.get("1.0", "end").strip()
    # if not text:
    #     messagebox.showerror("Error", "Please enter some text to convert.")
    #     return

    # try:
    #     session = Session()
    #     polly = session.client("polly")
    #     response = polly.synthesize_speech(Text=text, OutputFormat="mp3", VoiceId="Joanna")
    #     with open("output.mp3", "wb") as f:
    #         f.write(response["AudioStream"].read())
    #     messagebox.showinfo("Success", "Conversion completed successfully!")
    # except Exception as e:
    #     messagebox.showerror("Error", f"An error occurred: {str(e)}")




# Convert Button
convert_button = tk.Button(root, text="Convert", command=convert_to_speech, bg=button_bg_color, fg=button_fg_color)
convert_button.pack(pady=5, ipadx=10)

root.mainloop()
