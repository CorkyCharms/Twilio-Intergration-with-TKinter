from tkinter import *
from tkinter import ttk
from twilio.rest import Client


client = Client(
"{{Account-SID}}",
"{{Key}}"
)

def main():
    root = Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text="West Michigan Broadband texter").grid(column=0, row=0)
    ttk.Button(frm, text="Send a message", command=user_messageSend).grid(column=0, row=1)
    ttk.Button(frm, text="Receive text log", command=root.destroy).grid(column=1, row=1)
    ttk.Button(frm, text="Send mass text", command=root.destroy).grid(column=2, row=1)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=2, row=2)
    root.mainloop()

def user_messageSend():
    msg = client.messages.create(
        to="{{Number}}",
        from_="{{Number}}",
        body="Your text goes here"
    )
    # Unique ID
    print(f"Created a new message: {msg.sid}")

main()