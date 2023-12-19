#MADE BY AARON656 ON DISCORD
#GITHUB = Aaron-656


import tkinter as tk
from tkinter import messagebox
import requests
import json
import time  # Added for delay

def send_messages():
    webhook_url = url_entry.get()
    message_content = message_entry.get()
    num_messages = int(num_messages_entry.get())
    delay_seconds = float(delay_entry.get())  # Added for delay
    webhook_name = webhook_name_entry.get()  # Added for changing webhook name

    if not webhook_url or not message_content or not num_messages:
        messagebox.showerror("Error", "Please fill in all required fields.")
        return

    payload = {
        "content": message_content,
        "username": webhook_name  # Set the webhook's username
    }

    for _ in range(num_messages):
        requests.post(webhook_url, data=json.dumps(payload), headers={"Content-Type": "application/json"})
        time.sleep(delay_seconds)  # Added for delay

    messagebox.showinfo("Success", f"Sent {num_messages} messages to the Discord webhook.")

# GUI setup
root = tk.Tk()
root.title("Discord Webhook Sender - By Aaron656")

# Dark mode
root.configure(bg="#1E1E1E")
fg_color = "white"

# Webhook URL Entry
url_label = tk.Label(root, text="Webhook URL:", bg="#1E1E1E", fg=fg_color, font=("Segoe UI", 14))
url_label.pack(pady=(20, 5))
url_entry = tk.Entry(root, width=40, font=("Segoe UI", 12))
url_entry.pack(pady=5)

# Webhook Name Entry
webhook_name_label = tk.Label(root, text="Webhook Name:", bg="#1E1E1E", fg=fg_color, font=("Segoe UI", 14))
webhook_name_label.pack(pady=(10, 5))
webhook_name_entry = tk.Entry(root, width=40, font=("Segoe UI", 12))
webhook_name_entry.pack(pady=5)

# Message Entry
message_label = tk.Label(root, text="Message Content:", bg="#1E1E1E", fg=fg_color, font=("Segoe UI", 14))
message_label.pack(pady=(10, 5))
message_entry = tk.Entry(root, width=40, font=("Segoe UI", 12))
message_entry.pack(pady=5)

# Number of Messages Entry
num_messages_label = tk.Label(root, text="Number of Messages:", bg="#1E1E1E", fg=fg_color, font=("Segoe UI", 14))
num_messages_label.pack(pady=(10, 5))
num_messages_entry = tk.Entry(root, width=10, font=("Segoe UI", 12))
num_messages_entry.pack(pady=5)

# Delay Entry
delay_label = tk.Label(root, text="Delay Between Sends (seconds):", bg="#1E1E1E", fg=fg_color, font=("Segoe UI", 14))
delay_label.pack(pady=(10, 5))
delay_entry = tk.Entry(root, width=10, font=("Segoe UI", 12))
delay_entry.pack(pady=5)

# Send Button
send_button = tk.Button(root, text="Send Messages", command=send_messages, bg="#4CAF50", fg="white", font=("Segoe UI", 14))
send_button.pack(pady=(20, 0))

# Run the GUI
root.mainloop()
