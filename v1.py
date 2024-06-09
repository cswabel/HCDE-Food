import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import pytesseract
from pyzbar.pyzbar import decode
from datetime import datetime
import re
from tkinter import ttk

class FoodManagementApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Food Management App")
        self.geometry("800x600")
        self.create_widgets()

    def create_widgets(self):
        self.home_screen()

    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()

    def home_screen(self):
        self.clear_screen()
        tk.Label(self, text="Welcome to the Food Management App", font=("Helvetica", 16)).pack(pady=20)

        tk.Button(self, text="Scan Barcode/Expiry Date", command=self.scan_barcode_expiry_date_screen, width=30).pack(pady=10)
        tk.Button(self, text="AI Meal Generator", command=self.ai_meal_generator_screen, width=30).pack(pady=10)
        tk.Button(self, text="Suggest Ingredients", command=self.suggest_ingredients_screen, width=30).pack(pady=10)
        tk.Button(self, text="Community Engagement", command=self.community_engagement_screen, width=30).pack(pady=10)
        tk.Button(self, text="Voice Commands", command=self.voice_commands_screen, width=30).pack(pady=10)
        tk.Button(self, text="Settings", command=self.settings_screen, width=30).pack(pady=10)

    def scan_barcode_expiry_date_screen(self):
        self.clear_screen()
        tk.Label(self, text="Scan Barcode/Expiry Date", font=("Helvetica", 16)).pack(pady=20)
        tk.Button(self, text="Choose Image", command=self.load_image).pack(pady=10)
        self.image_label = tk.Label(self)
        self.image_label.pack(pady=10)
        self.result_label = tk.Label(self, text="")
        self.result_label.pack(pady=10)
        tk.Button(self, text="Back to Home", command=self.home_screen).pack(pady=20)

    def load_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            image = Image.open(file_path)
            image.thumbnail((400, 400))
            self.photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=self.photo)

            self.decode_barcode(file_path)
            self.extract_expiry_date(file_path)

    def decode_barcode(self, image_path):
        image = Image.open(image_path)
        decoded_objects = decode(image)
        for obj in decoded_objects:
            barcode_info = f"Type: {obj.type}, Data: {obj.data.decode('utf-8')}"
            self.result_label.config(text=barcode_info)

    def extract_expiry_date(self, image_path):
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        expiry_date = self.find_expiry_date(text)
        if expiry_date:
            expiry_info = f"Expiry Date: {expiry_date.strftime('%d/%m/%Y')}"
            self.result_label.config(text=expiry_info)

    def find_expiry_date(self, text):
        date_patterns = [
            r'\b(\d{2}/\d{2}/\d{4})\b',  # Format: DD/MM/YYYY
            r'\b(\d{2}-\d{2}-\d{4})\b',  # Format: DD-MM-YYYY
            r'\b(\d{4}/\d{2}/\d{2})\b',  # Format: YYYY/MM/DD
        ]

        for pattern in date_patterns:
            match = re.search(pattern, text)
            if match:
                date_str = match.group(1)
                try:
                    expiry_date = datetime.strptime(date_str, "%d/%m/%Y")
                    return expiry_date
                except ValueError:
                    try:
                        expiry_date = datetime.strptime(date_str, "%d-%m-%Y")
                        return expiry_date
                    except ValueError:
                        try:
                            expiry_date = datetime.strptime(date_str, "%Y/%m/%d")
                            return expiry_date
                        except ValueError:
                            continue

        return None

    def ai_meal_generator_screen(self):
        self.clear_screen()
        tk.Label(self, text="AI Meal Generator", font=("Helvetica", 16)).pack(pady=20)
        items = self.get_items_sorted_by_expiry_date()
        tk.Label(self, text="Items sorted by expiry date:").pack(pady=10)
        for item in items:
            tk.Label(self, text=item).pack()
        meals = self.generate_meals(items)
        tk.Label(self, text="Suggested Meals:").pack(pady=10)
        for meal in meals:
            tk.Label(self, text=meal).pack()
        tk.Button(self, text="Back to Home", command=self.home_screen).pack(pady=20)

    def get_items_sorted_by_expiry_date(self):
        return ["Milk (Exp: 2024-05-25)", "Eggs (Exp: 2024-05-24)", "Bread (Exp: 2024-05-23)"]

    def generate_meals(self, items):
        return ["French Toast", "Omelette", "Bread Pudding"]

    def suggest_ingredients_screen(self):
        self.clear_screen()
        tk.Label(self, text="Suggest Ingredients", font=("Helvetica", 16)).pack(pady=20)
        available_ingredients = self.get_available_ingredients()
        tk.Label(self, text="Available Ingredients:").pack(pady=10)
        for ingredient in available_ingredients:
            tk.Label(self, text=ingredient).pack()
        missing_ingredients = self.check_nearby_reduced_aisle_items(available_ingredients)
        tk.Label(self, text="Suggested Ingredients to Buy:").pack(pady=10)
        for ingredient in missing_ingredients:
            tk.Label(self, text=ingredient).pack()
        tk.Button(self, text="Back to Home", command=self.home_screen).pack(pady=20)

    def get_available_ingredients(self):
        return ["Tomatoes", "Cheese", "Pasta"]

    def check_nearby_reduced_aisle_items(self, available_ingredients):
        return ["Olive Oil", "Garlic", "Basil"]

    def community_engagement_screen(self):
        self.clear_screen()
        tk.Label(self, text="Community Engagement", font=("Helvetica", 16)).pack(pady=20)
        near_date_items = self.get_near_date_items()
        tk.Label(self, text="Near-Date Items Available for Trade:").pack(pady=10)
        for item in near_date_items:
            tk.Label(self, text=item).pack()
        self.earn_credits_for_sharing()
        self.view_community_trades()
        tk.Button(self, text="Back to Home", command=self.home_screen).pack(pady=20)

    def get_near_date_items(self):
        return ["Yogurt (Exp: 2024-05-22)", "Butter (Exp: 2024-05-21)"]

    def earn_credits_for_sharing(self):
        tk.Label(self, text="You have earned credits for sharing items.").pack(pady=10)

    def view_community_trades(self):
        tk.Label(self, text="Community Trades:").pack(pady=10)
        tk.Label(self, text="User1 traded Yogurt for Bread").pack()

    def voice_commands_screen(self):
        self.clear_screen()
        tk.Label(self, text="Voice Commands", font=("Helvetica", 16)).pack(pady=20)
        tk.Label(self, text="Voice Commands Activated. Please speak your command.").pack(pady=10)
        command = tk.Entry(self)
        command.pack(pady=10)
        tk.Button(self, text="Execute", command=lambda: self.execute_voice_command(command.get())).pack(pady=10)
        tk.Button(self, text="Back to Home", command=self.home_screen).pack(pady=20)

    def execute_voice_command(self, command):
        if "scan" in command.lower():
            self.scan_barcode_expiry_date_screen()
        elif "meal" in command.lower():
            self.ai_meal_generator_screen()
        elif "suggest" in command.lower():
            self.suggest_ingredients_screen()
        elif "community" in command.lower():
            self.community_engagement_screen()
        elif "settings" in command.lower():
            self.settings_screen()
        else:
            messagebox.showerror("Error", "Command not recognized.")

    def settings_screen(self):
        self.clear_screen()
        tk.Label(self, text="Settings", font=("Helvetica", 16)).pack(pady=20)
        tk.Button(self, text="Set Dietary Preferences and Allergies", command=self.set_dietary_preferences_and_allergies, width=30).pack(pady=10)
        tk.Button(self, text="Manage Shopping List", command=self.manage_shopping_list, width=30).pack(pady=10)
        tk.Button(self, text="Food Donation System", command=self.food_donation_system, width=30).pack(pady=10)
        tk.Button(self, text="Other Preferences", command=self.other_preferences, width=30).pack(pady=10)
        tk.Button(self, text="Back to Home", command=self.home_screen).pack(pady=20)

    def set_dietary_preferences_and_allergies(self):
        messagebox.showinfo("Settings", "Set your dietary preferences and allergies here.")

    def manage_shopping_list(self):
        messagebox.showinfo("Settings", "Manage your shopping list here.")

    def food_donation_system(self):
        messagebox.showinfo("Settings", "Donate food to those in need here.")

    def other_preferences(self):
        messagebox.showinfo("Settings", "Set other preferences here.")

if __name__ == "__main__":
    app = FoodManagementApp()
    app.mainloop()

    class FoodManagementApp(tk.Tk):
        def __init__(self):
            super().__init__()
            self.title("Food Management App")
            self.geometry("800x600")
            self.configure(bg="white")  # Set background color to white
            self.create_widgets()

        def create_widgets(self):
            self.home_screen()

        def clear_screen(self):
            for widget in self.winfo_children():
                widget.destroy()

        def home_screen(self):
            self.clear_screen()
            tk.Label(self, text="Welcome to the Food Management App", font=("Helvetica", 16), bg="white").pack(pady=20)

            tk.Button(self, text="Scan Barcode/Expiry Date", command=self.scan_barcode_expiry_date_screen, width=30, bg="lightblue").pack(pady=10)
            tk.Button(self, text="AI Meal Generator", command=self.ai_meal_generator_screen, width=30, bg="lightgreen").pack(pady=10)
            tk.Button(self, text="Suggest Ingredients", command=self.suggest_ingredients_screen, width=30, bg="lightyellow").pack(pady=10)
            tk.Button(self, text="Community Engagement", command=self.community_engagement_screen, width=30, bg="lightpink").pack(pady=10)
            tk.Button(self, text="Voice Commands", command=self.voice_commands_screen, width=30, bg="lightpurple").pack(pady=10)
            tk.Button(self, text="Settings", command=self.settings_screen, width=30, bg="lightorange").pack(pady=10)

        def scan_barcode_expiry_date_screen(self):
            self.clear_screen()
            tk.Label(self, text="Scan Barcode/Expiry Date", font=("Helvetica", 16), bg="white").pack(pady=20)
            tk.Button(self, text="Choose Image", command=self.load_image, bg="lightblue").pack(pady=10)
            self.image_label = tk.Label(self)
            self.image_label.pack(pady=10)
            self.result_label = tk.Label(self, text="", bg="white")
            self.result_label.pack(pady=10)
            tk.Button(self, text="Back to Home", command=self.home_screen, bg="lightgray").pack(pady=20)

        # Rest of the code...
        self.mainloop()

    if __name__ == "__main__":
        app = FoodManagementApp()
        app.mainloop()