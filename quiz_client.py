import socket
from threading import Thread
from tkinter import *

class GUI :
  def __init__ (self) :
    self.Window = Tk()
    self.Window.withdraw()

    self.loginscreen = Toplevel()
    self.loginscreen.title("Login")
    self.loginscreen.resizable(width = False, height = False)
    self.loginscreen.configure(width = 400, height = 300)

    self.title = Label(self.loginscreen, text = "Please Login", justify = CENTER, font = "Calibri 16 bold")
    self.title.place(relheight = 0.15, relx = 0.2, rely = 0.07)
    
    self.input = Entry(self.loginscreen, font = "Calibri 12")
    self.input.place(relwidth = 0.4, relheight = 0.12, relx = 0.35, rely = 0.2)
    self.input.focus()

    self.nickname = Button(self.loginscreen, text = "Continue", font = "Calibri 12", command = lamda: self.goahead(self.title.get()))
    self.nickname.place(relx = 0.4, rely = 0.55)

    self.Window.mainloop()

nickname = input("Choose your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000

client.connect((ip_address, port))

def receive() :
  while True:
    try:
      message = client.recv(2048).decode('utf-8')
      if message == 'NICKNAME':
        client.send(nickname.encode('utf-8'))
      else:
        print(message)
    except:
      print("An error occured!")
      client.close()
      break

def write() :
  while True:
    message = input('')
    client.send(message.encode('utf-8'))

receive_thread = Thread(target=receive)
receive_thread.start()
write_thread = Thread(target=write)
write_thread.start()

def goahead (self, name) :
  self.loginscreen.destroy()
  self.name = name
  
  thread = Thread(target = self.receive)
  thread.start()