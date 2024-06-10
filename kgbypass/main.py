import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
import serial.tools.list_ports
import re

class WinsKGActivator:
    def __init__(self, master):
        self.master = master
        master.title("Wins KG Activator 0.1")

        self.device_id = self.get_samsung_usb_modem_port()
        self.device_connected = bool(self.device_id)

        # Стилізація
        self.style = ttk.Style()
        self.style.configure("TFrame", background="#f0f0f0")
        self.style.configure("TLabel", background="#f0f0f0", font=("Arial", 12))
        self.style.configure("TButton", background="#007bff", foreground="black", font=("Arial", 12))

        # Контейнер для елементів
        self.main_frame = ttk.Frame(master)
        self.main_frame.pack(padx=20, pady=20)

        self.label_device_id = ttk.Label(self.main_frame, text=f"COM PORT: {self.device_id}", anchor="center")
        self.label_device_id.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.label_status = ttk.Label(self.main_frame, text=self.get_status_message(), anchor="center")
        self.label_status.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.button_activate = ttk.Button(self.main_frame, text="Activate Device", command=self.activate_device)
        self.button_activate.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        # Виклик методу для вирівнювання елементів по центру та зміна розмірів вікна
        self.center_window()

    def get_samsung_usb_modem_port(self):
        # Пошук доступних COM портів
        ports = serial.tools.list_ports.comports()
        for port, desc, hwid in sorted(ports):
            if "Samsung USB Modem" in desc:
                # Знаходження номеру COM порту
                match = re.search(r'COM(\d+)', port)
                if match:
                    return match.group(0)
        return None

    def get_status_message(self):
        if self.device_connected:
            return "Device Connected Successfully!"
        else:
            return "No Samsung USB Modem found."

    def activate_device(self):
        if self.device_connected:
            self.show_image_window()
        else:
            self.label_status.config(text="Please connect a device first.")

    def show_image_window(self):
        image_window = tk.Toplevel(self.master)
        image_window.title("Main Image")
        
        img = PhotoImage(file="main.png")
        label_image = tk.Label(image_window, image=img)
        label_image.image = img
        label_image.pack()

        button_next = ttk.Button(image_window, text="Next")
        button_next.pack()

    def center_window(self):
        # Отримання розмірів екрану
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        # Розміри вікна
        window_width = 500  # Збільшення ширини вікна
        window_height = 200

        # Обчислення положення вікна
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2

        # Встановлення положення та розмірів вікна
        self.master.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

root = tk.Tk()
app = WinsKGActivator(root)
root.mainloop()
