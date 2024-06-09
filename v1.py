import tkinter as tk
from tkinter import messagebox

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
        tk.Button(self, text="Scan Barcode", command=self.scan_barcode, bg="#8e94f2", fg="#ffffff").pack(pady=10)
        tk.Button(self, text="Generate Meal", command=self.generate_meal, bg="#8e94f2", fg="#ffffff").pack(pady=10)
        tk.Button(self, text="Community Trades", command=self.community_trades, bg="#8e94f2", fg="#ffffff").pack(pady=10)
        tk.Button(self, text="Dietary Preferences", command=self.dietary_preferences, bg="#8e94f2", fg="#ffffff").pack(pady=10)
        tk.Button(self, text="Food Donation", command=self.food_donation, bg="#8e94f2", fg="#ffffff").pack(pady=10)

    def scan_barcode(self):
        messagebox.showinfo("Scan Barcode", "Barcode scanning functionality")

    def generate_meal(self):
        messagebox.showinfo("Generate Meal", "AI Meal Generation functionality")

    def community_trades(self):
        messagebox.showinfo("Community Trades", "Community trading functionality")

    def dietary_preferences(self):
        messagebox.showinfo("Dietary Preferences", "Set dietary preferences")

    def food_donation(self):
        messagebox.showinfo("Food Donation", "Donate food")

    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = FoodManagementApp()
    app.mainloop()
