import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageDraw, ImageFont

# Function to generate resume image
def generate_resume(template_choice, user_data):
    # Load the appropriate template
    if template_choice == 1:
        template = Image.open("template-1.png")  # Placeholder image path
    elif template_choice == 2:
        template = Image.open("template-2.png")  # Placeholder image path
    else:
        template = Image.open("template-3.png")  # Placeholder image path

    draw = ImageDraw.Draw(template)
    font = ImageFont.truetype("arial.ttf", 20)  # Placeholder font path

    # Draw the user data on the template
    draw.text((50, 50), f"Name: {user_data['name']}", font=font, fill="black")
    draw.text((50, 100), f"Email: {user_data['email']}", font=font, fill="black")
    draw.text((50, 150), f"Phone: {user_data['phone']}", font=font, fill="black")
    draw.text((50, 200), f"Address: {user_data['address']}", font=font, fill="black")
    draw.text((50, 250), f"Education 1: {user_data['education1']}", font=font, fill="black")
    draw.text((50, 300), f"Education 2: {user_data['education2']}", font=font, fill="black")
    draw.text((50, 350), f"Experience: {user_data['experience']}", font=font, fill="black")
    draw.text((50, 400), f"Skills: {user_data['skills']}", font=font, fill="black")

    return template

# Function to save resume
def save_resume(image, file_type):
    file_path = tk.filedialog.asksaveasfilename(defaultextension=file_type, filetypes=[(f"{file_type.upper()} file", f"*.{file_type}")])
    if file_path:
        image.save(file_path)

# Function to preview the resume
def preview_resume():
    user_data = {
        "name": name_entry.get(),
        "email": email_entry.get(),
        "phone": phone_entry.get(),
        "address": address_entry.get(),
        "education1": edu1_entry.get(),
        "education2": edu2_entry.get(),
        "experience": exp_entry.get(),
        "skills": skills_entry.get(),
    }
    
    resume_image = generate_resume(template_var.get(), user_data)
    resume_image.show()

    # Save button
    save_button = ttk.Button(root, text="Save as JPG", command=lambda: save_resume(resume_image, "jpg"))
    save_button.pack(pady=10)
    save_button = ttk.Button(root, text="Save as PNG", command=lambda: save_resume(resume_image, "png"))
    save_button.pack(pady=10)
    save_button = ttk.Button(root, text="Save as PDF", command=lambda: save_resume(resume_image, "pdf"))
    save_button.pack(pady=10)

# GUI setup
root = tk.Tk()
root.title("Resume Maker")
root.geometry("500x600")

# Template selection
template_label = ttk.Label(root, text="Select Template:")
template_label.pack(pady=10)
template_var = tk.IntVar()
template1_radio = ttk.Radiobutton(root, text="Template 1", variable=template_var, value=1)
template1_radio.pack()
template2_radio = ttk.Radiobutton(root, text="Template 2", variable=template_var, value=2)
template2_radio.pack()
template3_radio = ttk.Radiobutton(root, text="Template 3", variable=template_var, value=3)
template3_radio.pack()

# Personal Information
name_label = ttk.Label(root, text="First Name:")
name_label.pack(pady=5)
name_entry = ttk.Entry(root)
name_entry.pack()

last_name_label = ttk.Label(root, text="Last Name (Optional):")
last_name_label.pack(pady=5)
last_name_entry = ttk.Entry(root)
last_name_entry.pack()

email_label = ttk.Label(root, text="Email:")
email_label.pack(pady=5)
email_entry = ttk.Entry(root)
email_entry.pack()

phone_label = ttk.Label(root, text="Phone Number:")
phone_label.pack(pady=5)
phone_entry = ttk.Entry(root)
phone_entry.pack()

address_label = ttk.Label(root, text="Address:")
address_label.pack(pady=5)
address_entry = ttk.Entry(root)
address_entry.pack()

# Educational Information
edu1_label = ttk.Label(root, text="Last Education (Institution - Duration):")
edu1_label.pack(pady=5)
edu1_entry = ttk.Entry(root)
edu1_entry.pack()

edu2_label = ttk.Label(root, text="Second Last Education (Institution - Duration):")
edu2_label.pack(pady=5)
edu2_entry = ttk.Entry(root)
edu2_entry.pack()

# Professional Experience
exp_label = ttk.Label(root, text="Experience (Title - Period - Description):")
exp_label.pack(pady=5)
exp_entry = ttk.Entry(root)
exp_entry.pack()

# Skills
skills_label = ttk.Label(root, text="Skills (Comma separated, max 5):")
skills_label.pack(pady=5)
skills_entry = ttk.Entry(root)
skills_entry.pack()

# Preview and Download
preview_button = ttk.Button(root, text="Preview Resume", command=preview_resume)
preview_button.pack(pady=20)

root.mainloop()
