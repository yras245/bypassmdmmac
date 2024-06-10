import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import qrcode

class WinsKGActivator:
    def __init__(self, master):
        self.master = master
        master.title("Wins KG Activator 0.1")

        # Стилізація
        self.style = ttk.Style()
        self.style.configure("TFrame", background="#f0f0f0")
        self.style.configure("TLabel", background="#f0f0f0", font=("Arial", 12))
        self.style.configure("TButton", background="#007bff", foreground="black", font=("Arial", 12))

        # Контейнер для елементів
        self.main_frame = ttk.Frame(master)
        self.main_frame.pack(padx=20, pady=20)

        # Відображення інформації про пристрій
        self.label_device_id = ttk.Label(self.main_frame, text="COM PORT: ", anchor="center")
        self.label_device_id.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.label_status = ttk.Label(self.main_frame, text="Wins KG Activator Initialized", anchor="center")
        self.label_status.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.button_activate = ttk.Button(self.main_frame, text="Activate Device", command=self.activate_device)
        self.button_activate.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        # Виклик методу для вирівнювання елементів по центру та зміна розмірів вікна
        self.center_window()

    def activate_device(self):
        self.show_image_window()

    def generate_qr_code(self, data, size):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white").resize((size, size))
        return ImageTk.PhotoImage(img)

    def show_image_window(self):
        image_window = tk.Toplevel(self.master)
        image_window.title("QR Code")

        # Дані для створення QR-коду
        data = '{"android.app.extra.PROVISIONING_DEVICE_ADMIN_COMPONENT_NAME":"com.service.mdm/.o0o0o0o0o0o0oOOO0o0o0o0o0o0o0oo0","android.app.extra.PROVISIONING_DEVICE_ADMIN_PACKAGE_CHECKSUM":"RZr10iWwO1cLlevp_7DxBw30MvXCcPSeHeAzHNm09cs","android.app.extra.PROVISIONING_DEVICE_ADMIN_PACKAGE_DOWNLOAD_LOCATION":"https://images.tmbkiller.com/00/apk240.apk","android.app.extra.PROVISIONING_SKIP_ENCRYPTION": true,"android.app.extra.PROVISIONING_LEAVE_ALL_SYSTEM_APPS_ENABLED":true,"android.app.extra.PROVISIONING_ADMIN_EXTRAS_BUNDLE": { "enrollmentId":"A6F5Q7I2-A6V4W8D3-M2P1N5K4-S7U1W8X2"}};'
        qr_size = 600

        # Генерація QR-коду з наданими даними
        qr_img = self.generate_qr_code(data, qr_size)

        label_qr_code = tk.Label(image_window, image=qr_img)
        label_qr_code.image = qr_img
        label_qr_code.pack()

        # Текст під QR-кодом
        qr_text = "1. Нажмите три раза в пустом месте 3-5 раз.\n2. Виберіть мову.\n3. Підключіться до Wi-Fi.\n4. Пройдіть настройку до кінця."
        label_qr_text = tk.Label(image_window, text=qr_text, font=("Arial", 12), wraplength=500, justify="left")
        label_qr_text.pack()

        # Кнопка "Далі"
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
