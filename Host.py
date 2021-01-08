
import socket
import threading , sys

s= socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
s.bind(('192.168.101.9',5967))
s.listen(5)

name=['sdf','sdf','sdf']
connname=[]
print("HOST SUCCESFULLY \n")
def connect():
    while True:
        try:
            conn, addr = s.accept()
            user_name = conn.recv(1024)
            user_name = user_name.decode()
            print(f"Name :- {user_name}  has connected")
            conn.send(f"Hello {user_name} you successfully connected to {conn.getsockname()}".encode())
            connname.append(conn)
            message_for_all_users = f"{user_name} has Joined the chatroom"
            sent(conn, message_for_all_users)
            t = threading.Thread(target=recv, args=(conn, user_name,))
            t.start()
        except Exception as e:
            print(e)


def sent(conn_name,recv_msg):
    for namess in connname:
        if conn_name!= namess:
            namess.send(recv_msg.encode())

def recv(conn,user_name):
    while True:
        recv_msg = conn.recv(1024)
        if not recv_msg:
            sys.exit(0)
        recv_msg = recv_msg.decode()
        recv_msg=f"{user_name}>>  {recv_msg}"
        sent(conn, recv_msg)



t=threading.Thread(target=connect)
t.start()










