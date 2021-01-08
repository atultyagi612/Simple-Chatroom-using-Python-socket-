
import socket
from threading import Thread
from tkinter import *
import sys


def receive():
    while True:
        recv_msg = s.recv(1024)
        if not recv_msg:
            sys.exit(0)
        recv_msg = recv_msg.decode()
        print("          ", recv_msg)
        msg_list.insert(END, recv_msg)


def send(event):
    msg = my_msg.get()
    my_msg.set("")

    s.send(bytes(msg, 'utf-8'))


def on_closing(event):
    my_msg.set("{quit}")
    send()

root=Tk()
root.title("Chatter")

messages_frame =Frame(root)
my_msg =StringVar()
my_msg.set("")
scrollbar =Scrollbar(messages_frame)

msg_list =Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
scrollbar.pack(side=RIGHT, fill=Y)
msg_list.pack(side=LEFT, fill=BOTH)
msg_list.pack()
messages_frame.pack()

entry_field =Entry(root, textvariable=my_msg)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button =Button(root, text="Send", command=send)
send_button.pack()



name="Client one"
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
s.connect(('192.168.101.9',5967))
s.send(name.encode())

receive_thread = Thread(target=receive)
receive_thread.start()
root.mainloop()  # Starts GUI execution.
s.close()