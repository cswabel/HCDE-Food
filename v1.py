import tkinter as tk
from tkinter import messagebox, Scrollbar

class FoodManagementApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Food Management App")
        self.geometry("400x600")
        self.configure(bg="#cdd3df")
        self.home_screen()

    def home_screen(self):
        self.clear_screen()
        tk.Label(self, text="Home Screen", font=("Helvetica", 16, "bold"), bg="#cdd3df", fg="#000000").pack(pady=20)
        tk.Button(self, text="Scan Barcode", command=self.scan_barcode, bg="#8e94f2", fg="#ffffff", width=20, height=2).pack(pady=10)
        tk.Button(self, text="Generate Meal", command=self.generate_meal, bg="#8e94f2", fg="#ffffff", width=20, height=2).pack(pady=10)
        tk.Button(self, text="Community Trades", command=self.community_trades, bg="#8e94f2", fg="#ffffff", width=20, height=2).pack(pady=10)
        tk.Button(self, text="Dietary Preferences", command=self.dietary_preferences, bg="#8e94f2", fg="#ffffff", width=20, height=2).pack(pady=10)
        tk.Button(self, text="Food Donation", command=self.food_donation, bg="#8e94f2", fg="#ffffff", width=20, height=2).pack(pady=10)
        tk.Button(self, text="Onboarding", command=self.onboarding, bg="#8e94f2", fg="#ffffff", width=20, height=2).pack(pady=10)
        tk.Button(self, text="Profile Management", command=self.profile_management, bg="#8e94f2", fg="#ffffff", width=20, height=2).pack(pady=10)

    def scan_barcode(self):
        messagebox.showinfo("Scan Barcode", "Barcode scanning functionality")

    def generate_meal(self):
        self.clear_screen()
        tk.Label(self, text="Select Ingredients", font=("Helvetica", 16, "bold"), bg="#cdd3df", fg="#000000").pack(pady=20)
        ingredients_frame = tk.Frame(self, bg="#cdd3df")
        ingredients_frame.pack(pady=10, padx=10)
        ingredients = ["Tomato", "Cheese", "Bread", "Lettuce", "Chicken", "Beef", "Pasta", "Rice"]
        self.selected_ingredients = []
        scrollbar = Scrollbar(ingredients_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        ingredients_listbox = tk.Listbox(ingredients_frame, selectmode=tk.MULTIPLE, yscrollcommand=scrollbar.set, bg="#8e94f2", fg="#ffffff")
        for ingredient in ingredients:
            ingredients_listbox.insert(tk.END, ingredient)
        ingredients_listbox.pack()
        scrollbar.config(command=ingredients_listbox.yview)
        tk.Button(self, text="Generate Meal", command=lambda: self.create_meal(ingredients_listbox.curselection(), ingredients), bg="#5469b6", fg="#ffffff", width=20, height=2).pack(pady=10)
        tk.Button(self, text="Back", command=self.home_screen, bg="#5469b6", fg="#ffffff", width=20, height=2).pack(pady=10)

    def create_meal(self, selections, ingredients):
        selected_items = [ingredients[i] for i in selections]
        meal = f"Generated Meal with: {', '.join(selected_items)}"
        messagebox.showinfo("Generated Meal", meal)
        self.home_screen()

    def community_trades(self):
        messagebox.showinfo("Community Trades", "Community trading functionality")

    def dietary_preferences(self):
        messagebox.showinfo("Dietary Preferences", "Set dietary preferences")

    def food_donation(self):
        messagebox.showinfo("Food Donation", "Donate food")

    def onboarding(self):
        messagebox.showinfo("Onboarding", "Onboarding process")

    def profile_management(self):
        messagebox.showinfo("Profile Management", "Manage profile")

    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = FoodManagementApp()
    app.mainloop()
