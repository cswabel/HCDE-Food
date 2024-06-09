import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import pytesseract

class FoodManagementApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Food Management App")
        self.geometry("600x600")
        self.configure(bg="#cdd3df")
        self.home_screen()

    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()

    def home_screen(self):
        self.clear_screen()
        tk.Label(self, text="Welcome to the Food Management App", font=("Helvetica", 20, "bold"), bg="#cdd3df", fg="#000000").pack(pady=30)
        buttons = [
            ("Scan Barcode/Expiry Date", self.scan_barcode_expiry_date_screen),
            ("AI Meal Generator", self.ai_meal_generator_screen),
            ("Suggest Ingredients", self.suggest_ingredients_screen),
            ("Community Engagement", self.community_engagement_screen),
            ("Voice Commands", self.voice_commands_screen),
            ("Settings", self.settings_screen)
        ]
        for text, command in buttons:
            tk.Button(self, text=text, font=("Helvetica", 14), command=command, width=30, height=2, bg="#8e94f2", fg="#ffffff", activebackground="#5469b6", relief="flat").pack(pady=10)

    def scan_barcode_expiry_date_screen(self):
        self.clear_screen()
        tk.Label(self, text="Scan Barcode/Expiry Date", font=("Helvetica", 16, "bold"), bg="#cdd3df", fg="#000000").pack(pady=20)
        tk.Button(self, text="Choose Image", command=self.choose_image, width=20, height=2, bg="#8e94f2", fg="#ffffff", activebackground="#5469b6", relief="flat").pack(pady=10)
        self.image_label = tk.Label(self, bg="#cdd3df")
        self.image_label.pack(pady=10)
        self.result_label = tk.Label(self, text="", font=("Helvetica", 12), bg="#cdd3df", fg="#23395b")
        self.result_label.pack(pady=10)
        tk.Button(self, text="Back to Home", command=self.home_screen, width=20, height=2, bg="#8e94f2", fg="#ffffff", activebackground="#5469b6", relief="flat").pack(pady=20)

    def choose_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if file_path:
            image = Image.open(file_path)
            image.thumbnail((400, 400))
            photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo)
            self.image_label.image = photo
            self.process_image(image)

    def process_image(self, image):
        result = pytesseract.image_to_string(image)
        self.result_label.config(text=f"Decoded text: {result}")

    def ai_meal_generator_screen(self):
        self.clear_screen()
        tk.Label(self, text="AI Meal Generator", font=("Helvetica", 16, "bold"), bg="#cdd3df", fg="#000000").pack(pady=20)
        # Mockup content for AI meal generator
        items = ["Milk (Exp: 2024-05-25)", "Eggs (Exp: 2024-05-30)"]
        meals = ["French Toast", "Omelette"]
        tk.Label(self, text="Items sorted by expiry date:", font=("Helvetica", 14), bg="#cdd3df", fg="#23395b").pack(pady=10)
        for item in items:
            tk.Label(self, text=item, font=("Helvetica", 12), bg="#cdd3df", fg="#23395b").pack(pady=2)
        tk.Label(self, text="Suggested Meals:", font=("Helvetica", 14), bg="#cdd3df", fg="#23395b").pack(pady=10)
        for meal in meals:
            tk.Label(self, text=meal, font=("Helvetica", 12), bg="#cdd3df", fg="#23395b").pack(pady=2)
        tk.Button(self, text="Back to Home", command=self.home_screen, width=20, height=2, bg="#8e94f2", fg="#ffffff", activebackground="#5469b6", relief="flat").pack(pady=20)

    def suggest_ingredients_screen(self):
        self.clear_screen()
        tk.Label(self, text="Suggest Ingredients", font=("Helvetica", 16, "bold"), bg="#cdd3df", fg="#000000").pack(pady=20)
        # Mockup content for suggesting ingredients
        available_ingredients = ["Tomatoes", "Cheese"]
        suggested_ingredients = ["Olive Oil", "Basil"]
        tk.Label(self, text="Available Ingredients:", font=("Helvetica", 14), bg="#cdd3df", fg="#23395b").pack(pady=10)
        for ingredient in available_ingredients:
            tk.Label(self, text=ingredient, font=("Helvetica", 12), bg="#cdd3df", fg="#23395b").pack(pady=2)
        tk.Label(self, text="Suggested Ingredients to Buy:", font=("Helvetica", 14), bg="#cdd3df", fg="#23395b").pack(pady=10)
        for ingredient in suggested_ingredients:
            tk.Label(self, text=ingredient, font=("Helvetica", 12), bg="#cdd3df", fg="#23395b").pack(pady=2)
        tk.Button(self, text="Back to Home", command=self.home_screen, width=20, height=2, bg="#8e94f2", fg="#ffffff", activebackground="#5469b6", relief="flat").pack(pady=20)

    def community_engagement_screen(self):
        self.clear_screen()
        tk.Label(self, text="Community Engagement", font=("Helvetica", 16, "bold"), bg="#cdd3df", fg="#000000").pack(pady=20)
        # Mockup content for community engagement
        items_for_trade = ["Yogurt (Exp: 2024-05-22)", "Bread (Exp: 2024-05-20)"]
        tk.Label(self, text="Near-Date Items Available for Trade:", font=("Helvetica", 14), bg="#cdd3df", fg="#23395b").pack(pady=10)
        for item in items_for_trade:
            tk.Label(self, text=item, font=("Helvetica", 12), bg="#cdd3df", fg="#23395b").pack(pady=2)
        tk.Label(self, text="You have earned credits for sharing items.", font=("Helvetica", 12), bg="#cdd3df", fg="#23395b").pack(pady=10)
        tk.Label(self, text="Community Trades:", font=("Helvetica", 14), bg="#cdd3df", fg="#23395b").pack(pady=10)
        community_trades = ["User1 traded Yogurt for Bread"]
        for trade in community_trades:
            tk.Label(self, text=trade, font=("Helvetica", 12), bg="#cdd3df", fg="#23395b").pack(pady=2)
        tk.Button(self, text="Back to Home", command=self.home_screen, width=20, height=2, bg="#8e94f2", fg="#ffffff", activebackground="#5469b6", relief="flat").pack(pady=20)

    def voice_commands_screen(self):
        self.clear_screen()
        tk.Label(self, text="Voice Commands", font=("Helvetica", 16, "bold"), bg="#cdd3df", fg="#000000").pack(pady=20)
        tk.Label(self, text="Voice Commands Activated. Please speak your command.", font=("Helvetica", 12), bg="#cdd3df", fg="#23395b").pack(pady=10)
        command = tk.Entry(self, font=("Helvetica", 12), bg="#ffffff", fg="#23395b")
        command.pack(pady=10)
        tk.Button(self, text="Execute", command=lambda: self.execute_voice_command(command.get()), width=20, height=2, bg="#8e94f2", fg="#ffffff", activebackground="#5469b6", relief="flat").pack(pady=10)
        tk.Button(self, text="Back to Home", command=self.home_screen, width=20, height=2, bg="#8e94f2", fg="#ffffff", activebackground="#5469b6", relief="flat").pack(pady=20)

    def execute_voice_command(self, command):
        messagebox.showinfo("Voice Command", f"You said: {command}")

    def settings_screen(self):
        self.clear_screen()
        tk.Label(self, text="Settings", font=("Helvetica", 16, "bold"), bg="#cdd3df", fg="#000000").pack(pady=20)
        buttons = [
            ("Set Dietary Preferences and Allergies", self.dietary_preferences_screen),
            ("Manage Shopping List", self.manage_shopping_list_screen),
            ("Food Donation System", self.food_donation_screen),
            ("Other Preferences", self.other_preferences_screen)
        ]
        for text, command in buttons:
            tk.Button(self, text=text, font=("Helvetica", 14), command=command, width=30, height=2, bg="#8e94f2", fg="#ffffff", activebackground="#5469b6", relief="flat").pack(pady=10)
        tk.Button(self, text="Back to Home", command=self.home_screen, width=20, height=2, bg="#8e94f2", fg="#ffffff", activebackground="#5469b6", relief="flat").pack(pady=20)

    def dietary_preferences_screen(self):
        self.clear_screen()
        tk.Label(self, text="Dietary Preferences and Allergies", font=("Helvetica", 16, "bold"), bg="#cdd3df", fg="#000000").pack(pady=20)
        # Mockup content for dietary preferences
        tk.Label(self, text="Set your dietary preferences and allergies here.", font=("Helvetica", 12), bg="#cdd3df", fg="#23395b").pack(pady=10)
        tk.Button(self, text="Back to Home", command=self.home_screen, width=20, height=2, bg="#8e94f2", fg="#ffffff", activebackground="#5469b6", relief="flat").pack(pady=20)

    def manage_shopping_list_screen(self):
        self.clear_screen()
        tk.Label(self, text="Manage Shopping List", font=("Helvetica", 16, "bold"), bg="#cdd3df", fg="#000000").pack(pady=20)
        # Mockup content for shopping list
        tk.Label(self, text="Manage your shopping list here.", font=("Helvetica", 12), bg="#cdd3df", fg="#23395b").pack(pady=10)
        tk.Button(self, text="Back to Home", command=self.home_screen, width=20, height=2, bg="#8e94f2", fg="#ffffff", activebackground="#5469b6", relief="flat").pack(pady=20)

    def food_donation_screen(self):
        self.clear_screen()
        tk.Label(self, text="Food Donation System", font=("Helvetica", 16, "bold"), bg="#cdd3df", fg="#000000").pack(pady=20)
        # Mockup content for food donation
        tk.Label(self, text="Manage food donations here.", font=("Helvetica", 12), bg="#cdd3df", fg="#23395b").pack(pady=10)
        tk.Button(self, text="Back to Home", command=self.home_screen, width=20, height=2, bg="#8e94f2", fg="#ffffff", activebackground="#5469b6", relief="flat").pack(pady=20)

    def other_preferences_screen(self):
        self.clear_screen()
        tk.Label(self, text="Other Preferences", font=("Helvetica", 16, "bold"), bg="#cdd3df", fg="#000000").pack(pady=20)
        # Mockup content for other preferences
        tk.Label(self, text="Set other preferences here.", font=("Helvetica", 12), bg="#cdd3df", fg="#23395b").pack(pady=10)
        tk.Button(self, text="Back to Home", command=self.home_screen, width=20, height=2, bg="#8e94f2", fg="#ffffff", activebackground="#5469b6", relief="flat").pack(pady=20)

if __name__ == "__main__":
    app = FoodManagementApp()
    app.mainloop()
