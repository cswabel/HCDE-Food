import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import pytesseract
import random
from datetime import datetime

class FoodManagementApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Food Management App")
        self.geometry("600x800")
        self.configure(bg="#cdd3df")
        self.meal_pool = {
            "Spaghetti Bolognese": ["Spaghetti", "Minced Meat", "Tomato Sauce", "Onions"],
            "Chicken Salad": ["Chicken", "Lettuce", "Tomatoes", "Cucumber", "Olive Oil"],
            "Vegetable Stir Fry": ["Broccoli", "Carrots", "Bell Peppers", "Soy Sauce", "Garlic"],
            "Pancakes": ["Flour", "Milk", "Eggs", "Butter", "Maple Syrup"],
            "Omelette": ["Eggs", "Cheese", "Ham", "Bell Peppers"],
            "Grilled Cheese Sandwich": ["Bread", "Cheese", "Butter"],
            "French Toast": ["Bread", "Eggs", "Milk", "Cinnamon", "Maple Syrup"],
            "Caesar Salad": ["Lettuce", "Croutons", "Chicken", "Caesar Dressing", "Parmesan Cheese"]
        }
        self.ingredients = {
            "Spaghetti": "2024-06-10",
            "Minced Meat": "2024-06-05",
            "Tomato Sauce": "2024-06-20",
            "Onions": "2024-06-15",
            "Chicken": "2024-06-08",
            "Lettuce": "2024-06-07",
            "Tomatoes": "2024-06-10",
            "Cucumber": "2024-06-12",
            "Olive Oil": "2024-07-01",
            "Broccoli": "2024-06-11",
            "Carrots": "2024-06-14",
            "Bell Peppers": "2024-06-13",
            "Soy Sauce": "2024-07-20",
            "Garlic": "2024-06-25",
            "Flour": "2024-12-01",
            "Milk": "2024-06-05",
            "Eggs": "2024-06-04",
            "Butter": "2024-08-01",
            "Maple Syrup": "2024-12-10",
            "Cheese": "2024-06-18",
            "Ham": "2024-06-06",
            "Bread": "2024-06-03",
            "Cinnamon": "2024-12-25",
            "Croutons": "2024-07-15",
            "Caesar Dressing": "2024-07-10",
            "Parmesan Cheese": "2024-07-05"
        }
        self.selected_ingredients = []
        self.user_profile = {"name": "", "email": ""}
        self.logged_in = False
        self.current_step = 0
        self.onboarding_steps = [
            "Welcome to the Food Management App",
            "Scan barcodes and expiry dates",
            "Generate meals with AI",
            "Engage with the community",
            "Manage your profile and settings"
        ]
        self.onboarding_screen()

    def clear_screen(self):
        """Clear all widgets from the screen."""
        for widget in self.winfo_children():
            widget.destroy()

    def onboarding_screen(self):
        """Display the onboarding screen with navigation buttons."""
        self.clear_screen()
        if self.current_step < len(self.onboarding_steps):
            tk.Label(self, text=self.onboarding_steps[self.current_step], font=("Helvetica", 20, "bold"), bg="#cdd3df", fg="#000000").pack(pady=30)
            tk.Button(self, text="Next", font=("Helvetica", 14), command=self.next_onboarding_step, width=20, height=2, bg="#8e94f2", fg="#ffffff", activebackground="#5469b6", relief="flat").pack(pady=20)
        else:
            self.home_screen()

    def next_onboarding_step(self):
        """Move to the next step in the onboarding process."""
        self.current_step += 1
        self.onboarding_screen()

    def home_screen(self):
        """Display the home screen with main options."""
        self.clear_screen()
        tk.Label(self, text="Welcome to the Food Management App", font=("Helvetica", 20, "bold"), bg="#cdd3df", fg="#000000").pack(pady=30)
        buttons = [
            ("Scan Barcode/Expiry Date", self.scan_barcode_expiry_date_screen),
            ("AI Meal Generator", self.ai_meal_generator_screen),
            ("Suggest Ingredients", self.suggest_ingredients_screen),
            ("Community Engagement", self.community_engagement_screen),
            ("Voice Commands", self.voice_commands_screen),
            ("Profile", self.profile_screen),
            ("Settings", self.settings_screen)
        ]
        for text, command in buttons:
            tk.Button(self, text=text, font=("Helvetica", 14), command=command, width=30, height=2, bg="#8e94f2", fg="#ffffff", activebackground="#5469b6", relief="flat").pack(pady=10)

    def scan_barcode_expiry_date_screen(self):
        """Screen for scanning barcodes or expiry dates."""
        self.clear_screen()
        tk.Label(self, text="Scan Barcode/Expiry Date", font=("Helvetica", 16, "bold"), bg="#cdd3df", fg="#000000").pack(pady=20)
        tk.Button(self, text="Choose Image", command=self.choose_image, width=20, height=2, bg="#8e94f2", fg="#ffffff", activebackground="#5469b6", relief="flat").pack(pady=10)
        self.image_label = tk.Label(self, bg="#cdd3df")
        self.image_label.pack(pady=10)
        self.result_label = tk.Label(self, text="", font=("Helvetica", 12), bg="#cdd3df", fg="#23395b")
        self.result_label.pack(pady=10)
        tk.Button(self, text="Back to Home", command=self.home_screen, width=20, height=2, bg="#8e94f2", fg="#ffffff", activebackground="#5469b6", relief="flat").pack(pady=20)

    def choose_image(self):
        """Open file dialog to choose an image for barcode/expiry date scanning."""
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if file_path:
            image = Image.open(file_path)
            image.thumbnail((400, 400))
            photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo)
            self.image_label.image = photo
            self.process_image(image)

    def process_image(self, image):
        """Process the image to extract text using OCR."""
        result = pytesseract.image_to_string(image)
        self.result_label.config(text=f"Decoded text: {result}")

    def ai_meal_generator_screen(self):
        """Screen for AI meal generation based on selected ingredients."""
        self.clear_screen()
        tk.Label(self, text="AI Meal Generator", font=("Helvetica", 16, "bold"), bg="#cdd3df", fg="#000000").pack(pady=20)

        # Create a canvas and scrollbar for scrolling functionality
        canvas = tk.Canvas(self, bg="#cdd3df")
        scrollbar = tk.Scrollbar(self, orient="vertical", command=canvas.yview)
        scroll_frame = tk.Frame(canvas, bg="#cdd3df")

        scroll_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Generate a meal based on the ingredients and expiry dates
        tk.Label(scroll_frame, text="Select Ingredients:", font=("Helvetica", 14), bg="#cdd3df", fg="#23395b").pack(pady=10)
        self.selected_ingredients = []
        for ingredient, expiry in sorted(self.ingredients.items(), key=lambda x: x[1]):
            var = tk.BooleanVar()
            chk = tk.Checkbutton(scroll_frame, text=f"{ingredient} (Exp: {expiry})", variable=var, font=("Helvetica", 12), bg="#cdd3df", fg="#23395b", onvalue=True, offvalue=False)
            chk.var = var
            chk.pack(pady=2)
            self.selected_ingredients.append((ingredient, var))
        tk.Button(scroll_frame, text="Generate Meal", command=self.generate_meal_based_on_selection, width=20, height=2, bg="#8e94f2", fg="#ffffff", activebackground="#5469b6", relief="flat").pack(pady=20)

        self.generated_meal_label = tk.Label(scroll_frame, text="", font=("Helvetica", 12), bg="#cdd3df", fg="#23395b")
        self.generated_meal_label.pack(pady=10)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        tk.Button(self, text="Back to Home", command=self.home_screen, width=20, height=2, bg="#8e94f2", fg="#ffffff", activebackground="#5469b6", relief="flat").pack(pady=20)

    def generate_meal_based_on_selection(self):
        """Generate a meal based on the selected ingredients."""
        selected = [ingredient for ingredient, var in self.selected_ingredients if var.get()]
        possible_meals = [meal for meal, ingredients in self.meal_pool.items() if all(item in selected for item in ingredients)]
        if possible_meals:
            meal = random.choice(possible_meals)
            self.generated_meal_label.config(text=f"Suggested Meal: {meal}\nIngredients: {', '.join(self.meal_pool[meal])}")
        else:
            self.generated_meal_label.config(text="No meals can be generated with the selected ingredients.")

    def suggest_ingredients_screen(self):
        """Screen to suggest additional ingredients for meals."""
        self.clear_screen()
        tk.Label(self, text="Suggested Ingredients", font=("Helvetica", 16, "bold"), bg="#cdd3df", fg="#000000").pack(pady=20)

        # Create a canvas and scrollbar for scrolling functionality
        canvas = tk.Canvas(self, bg="#cdd3df")
        scrollbar = tk.Scrollbar(self, orient="vertical", command=canvas.yview)
        scroll_frame = tk.Frame(canvas, bg="#cdd3df")

        scroll_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        suggested_ingredients = ["Bread", "Butter", "Milk", "Eggs"]  # Mock data
        tk.Label(scroll_frame, text="Suggested Ingredients:", font=("Helvetica", 14), bg="#cdd3df", fg="#23395b").pack(pady=10)
        for ingredient in suggested_ingredients:
            tk.Label(scroll_frame, text=ingredient, font=("Helvetica", 12), bg="#cdd3df", fg="#23395b").pack(pady=2)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        tk.Button(self, text="Back to Home", command=self.home_screen, width=20, height=2, bg="#8e94f2", fg="#ffffff", activebackground="#5469b6", relief="flat").pack(pady=20)

    def community_engagement_screen(self):
        """Screen for community engagement features."""
        self.clear_screen()
        tk.Label(self, text="Community Engagement", font=("Helvetica", 16, "bold"), bg="#cdd3df", fg="#000000").pack(pady=20)

        # Create a canvas and scrollbar for scrolling functionality
        canvas = tk.Canvas(self, bg="#cdd3df")
        scrollbar = tk.Scrollbar(self, orient="vertical", command=canvas.yview)
        scroll_frame = tk.Frame(canvas, bg="#cdd3df")

        scroll_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        items_for_trade = ["Milk", "Eggs"]  # Mock data
        tk.Label(scroll_frame, text="Near-Date Items Available for Trade:", font=("Helvetica", 14), bg="#cdd3df", fg="#23395b").pack(pady=10)
        for item in items_for_trade:
            tk.Label(scroll_frame, text=item, font=("Helvetica", 12), bg="#cdd3df", fg="#23395b").pack(pady=2)
        tk.Label(scroll_frame, text="You have earned credits for sharing items.", font=("Helvetica", 12), bg="#cdd3df", fg="#23395b").pack(pady=10)
        tk.Label(scroll_frame, text="Community Trades:", font=("Helvetica", 14), bg="#cdd3df", fg="#23395b").pack(pady=10)
        community_trades = ["User1 traded Yogurt for Bread"]  # Mock data
        for trade in community_trades:
            tk.Label(scroll_frame, text=trade, font=("Helvetica", 12), bg="#cdd3df", fg="#23395b").pack(pady=2)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        tk.Button(self, text="Back to Home", command=self.home_screen, width=20, height=2, bg="#8e94f2", fg="#ffffff", activebackground="#5469b6", relief="flat").pack(pady=20)

    def voice_commands_screen(self):
        """Screen for voice commands."""
        self.clear_screen()
        tk.Label(self, text="Voice Commands", font=("Helvetica", 16, "bold"), bg="#cdd3df", fg="#000000").pack(pady=20)
        tk.Label(self, text="Voice Commands Activated. Please speak your command.", font=("Helvetica", 12), bg="#cdd3df", fg="#23395b").pack(pady=10)
        command = tk.Entry(self, font=("Helvetica", 12), bg="#ffffff", fg="#23395b")
        command.pack(pady=10)
        tk.Button(self, text="Execute", command=lambda: self.execute_voice_command(command.get()), width=20, height=2, bg="#8e94f2", fg="#ffffff", activebackground="#5469b6", relief="flat").pack(pady=10)
        tk.Button(self, text="Back to Home", command=self.home_screen, width=20, height=2, bg="#8e94f2", fg="#ffffff", activebackground="#5469b6", relief="flat").pack(pady=20)

    def execute_voice_command(self, command):
        """Execute the given voice command."""
        messagebox.showinfo("Voice Command", f"You said: {command}")

    def profile_screen(self):
        """Screen for user profile management."""
        self.clear_screen()
        tk.Label(self, text="Profile", font=("Helvetica", 16, "bold"), bg="#cdd3df", fg="#000000").pack(pady=20)
        tk.Label(self, text="Name:", font=("Helvetica", 12), bg="#cdd3df", fg="#23395b").pack(pady=10)
        self.name_entry = tk.Entry(self, font=("Helvetica", 12), bg="#ffffff", fg="#23395b")
        self.name_entry.pack(pady=10)
        tk.Label(self, text="Email:", font=("Helvetica", 12), bg="#cdd3df", fg="#23395b").pack(pady=10)
        self.email_entry = tk.Entry(self, font=("Helvetica", 12), bg="#ffffff", fg="#23395b")
        self.email_entry.pack(pady=10)
        tk.Button(self, text="Save", command=self.save_profile, width=20, height=2, bg="#8e94f2", fg="#ffffff", activebackground="#5469b6", relief="flat").pack(pady=20)
        tk.Button(self, text="Back to Home", command=self.home_screen, width=20, height=2, bg="#8e94f2", fg="#ffffff", activebackground="#5469b6", relief="flat").pack(pady=20)

    def save_profile(self):
        """Save the user's profile information."""
        self.user_profile["name"] = self.name_entry.get()
        self.user_profile["email"] = self.email_entry.get()
        messagebox.showinfo("Profile Saved", "Your profile has been updated.")

    def settings_screen(self):
        """Screen for settings and preferences."""
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
        """Screen to set dietary preferences and allergies."""
        self.clear_screen()
        tk.Label(self, text="Dietary Preferences and Allergies", font=("Helvetica", 16, "bold"), bg="#cdd3df", fg="#000000").pack(pady=20)
        tk.Label(self, text="Select your dietary preferences and allergies.", font=("Helvetica", 12), bg="#cdd3df", fg="#23395b").pack(pady=10)
        tk.Checkbutton(self, text="Vegetarian", font=("Helvetica", 12), bg="#cdd3df", fg="#23395b").pack(pady=2)
        tk.Checkbutton(self, text="Vegan", font=("Helvetica", 12), bg="#cdd3df", fg="#23395b").pack(pady=2)
        tk.Checkbutton(self, text="Gluten-Free", font=("Helvetica", 12), bg="#cdd3df", fg="#23395b").pack(pady=2)
        tk.Checkbutton(self, text="Nut Allergy", font=("Helvetica", 12), bg="#cdd3df", fg="#23395b").pack(pady=2)
        tk.Button(self, text="Save", command=self.home_screen, width=20, height=2, bg="#8e94f2", fg="#ffffff", activebackground="#5469b6", relief="flat").pack(pady=20)

    def manage_shopping_list_screen(self):
        """Screen to manage the shopping list."""
        self.clear_screen()
        tk.Label(self, text="Manage Shopping List", font=("Helvetica", 16, "bold"), bg="#cdd3df", fg="#000000").pack(pady=20)
        tk.Label(self, text="Your shopping list is currently empty.", font=("Helvetica", 12), bg="#cdd3df", fg="#23395b").pack(pady=10)
        tk.Button(self, text="Back to Home", command=self.home_screen, width=20, height=2, bg="#8e94f2", fg="#ffffff", activebackground="#5469b6", relief="flat").pack(pady=20)

    def food_donation_screen(self):
        """Screen for the food donation system."""
        self.clear_screen()
        tk.Label(self, text="Food Donation System", font=("Helvetica", 16, "bold"), bg="#cdd3df", fg="#000000").pack(pady=20)
        tk.Label(self, text="Donate food to those in need.", font=("Helvetica", 12), bg="#cdd3df", fg="#23395b").pack(pady=10)
        tk.Button(self, text="Donate Now", command=lambda: messagebox.showinfo("Thank You", "Your donation has been accepted."), width=20, height=2, bg="#8e94f2", fg="#ffffff", activebackground="#5469b6", relief="flat").pack(pady=20)
        tk.Button(self, text="Back to Home", command=self.home_screen, width=20, height=2, bg="#8e94f2", fg="#ffffff", activebackground="#5469b6", relief="flat").pack(pady=20)

    def other_preferences_screen(self):
        """Screen for other preferences and settings."""
        self.clear_screen()
        tk.Label(self, text="Other Preferences", font=("Helvetica", 16, "bold"), bg="#cdd3df", fg="#000000").pack(pady=20)
        tk.Label(self, text="Set other preferences here.", font=("Helvetica", 12), bg="#cdd3df", fg="#23395b").pack(pady=10)
        tk.Button(self, text="Back to Home", command=self.home_screen, width=20, height=2, bg="#8e94f2", fg="#ffffff", activebackground="#5469b6", relief="flat").pack(pady=20)

if __name__ == "__main__":
    app = FoodManagementApp()
    app.mainloop()
