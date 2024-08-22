import tkinter as tk
from tkinter import ttk, messagebox
import random
import importlib

root = tk.Tk()
root.title("CV Maker")

# Define user data storage
user_data = {}

# Show the given frame
def show_frame(frame):
    frame.tkraise()

# Section 1: Greeting Window
def section_1():
    global frame1
    frame1 = tk.Frame(root, width=900, height=600, bg="white")
    frame1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    
    title = tk.Label(frame1, text="CV MAKER", font=("Arial", 24, "bold"), bg="white")
    title.pack(pady=20)
    
    motive = tk.Label(frame1, text="Create Your CV Instantly.", font=("Arial", 16), bg="white")
    motive.pack(pady=10)
    
    message = tk.Label(frame1, text="In the modern world, create your CV by clicking the button below to get started.", 
                       font=("Arial", 14), bg="white", wraplength=800, justify="center")
    message.pack(pady=50)
    
    start_button = tk.Button(frame1, text="Get Started", font=("Arial", 14), command=lambda: show_frame(frame2))
    start_button.pack(pady=30)
    
    frame1.grid(row=0, column=0, sticky="nsew")

# Section 2: Template Selection
def section_2():
    global frame2
    frame2 = tk.Frame(root, width=900, height=600, bg="white")
    frame2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    
    title = tk.Label(frame2, text="CV MAKER", font=("Arial", 24, "bold"), bg="white")
    title.pack(pady=20)
    
    motive = tk.Label(frame2, text="Create Your CV Instantly.", font=("Arial", 16), bg="white")
    motive.pack(pady=10)
    
    template_label = tk.Label(frame2, text="Choose Your Template", font=("Arial", 14), bg="white")
    template_label.pack(pady=20)
    
    template_frame = tk.Frame(frame2, bg="white")
    template_frame.pack(pady=20)
    
    template1 = tk.Button(template_frame, text="Template 1", font=("Arial", 14), width=20, height=10, command=lambda: select_template(1))
    template2 = tk.Button(template_frame, text="Template 2", font=("Arial", 14), width=20, height=10, command=lambda: select_template(2))
    template3 = tk.Button(template_frame, text="Template 3", font=("Arial", 14), width=20, height=10, command=lambda: select_template(3))
    
    template1.pack(side="left", padx=10)
    template2.pack(side="left", padx=10)
    template3.pack(side="left", padx=10)
    
    frame2.grid(row=0, column=0, sticky="nsew")

# Template selection handler
def select_template(template_number):
    user_data["template"] = template_number
    show_frame(frame3)

# Section 3: Personal Information
def section_3():
    global frame3, entry_name, entry_email, entry_phone, entry_website, entry_job_title
    frame3 = tk.Frame(root, width=900, height=600, bg="white")
    frame3.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    
    title = tk.Label(frame3, text="CV MAKER", font=("Arial", 24, "bold"), bg="white")
    title.pack(pady=20)
    
    motive = tk.Label(frame3, text="Create Your CV Instantly.", font=("Arial", 16), bg="white")
    motive.pack(pady=10)
    
    label_name = tk.Label(frame3, text="Full Name:", font=("Arial", 14), bg="white")
    label_name.pack(pady=5)
    entry_name = tk.Entry(frame3, width=40, font=("Arial", 14))
    entry_name.pack(pady=5)
    
    label_email = tk.Label(frame3, text="Email:", font=("Arial", 14), bg="white")
    label_email.pack(pady=5)
    entry_email = tk.Entry(frame3, width=40, font=("Arial", 14))
    entry_email.pack(pady=5)
    
    label_phone = tk.Label(frame3, text="Phone Number:", font=("Arial", 14), bg="white")
    label_phone.pack(pady=5)
    entry_phone = tk.Entry(frame3, width=40, font=("Arial", 14))
    entry_phone.pack(pady=5)
    
    label_website = tk.Label(frame3, text="Website / LinkedIn URL:", font=("Arial", 14), bg="white")
    label_website.pack(pady=5)
    entry_website = tk.Entry(frame3, width=40, font=("Arial", 14))
    entry_website.pack(pady=5)
    
    label_job_title = tk.Label(frame3, text="Current Job Title:", font=("Arial", 14), bg="white")
    label_job_title.pack(pady=5)
    entry_job_title = tk.Entry(frame3, width=40, font=("Arial", 14))
    entry_job_title.pack(pady=5)
    
    next_button = tk.Button(frame3, text="Next", font=("Arial", 14), command=collect_personal_info)
    next_button.pack(pady=30)
    
    frame3.grid(row=0, column=0, sticky="nsew")

def collect_personal_info():
    user_data["personal_info"] = {
        "name": entry_name.get(),
        "email": entry_email.get(),
        "phone": entry_phone.get(),
        "website": entry_website.get(),
        "job_title": entry_job_title.get()
    }
    show_frame(frame4)

# Section 4: Education
def section_4():
    global frame4, entry_education, entry_school, entry_dates
    frame4 = tk.Frame(root, width=900, height=600, bg="white")
    frame4.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    
    title = tk.Label(frame4, text="CV MAKER", font=("Arial", 24, "bold"), bg="white")
    title.pack(pady=20)
    
    motive = tk.Label(frame4, text="Create Your CV Instantly.", font=("Arial", 16), bg="white")
    motive.pack(pady=10)
    
    label_education = tk.Label(frame4, text="Education:", font=("Arial", 14), bg="white")
    label_education.pack(pady=5)
    entry_education = tk.Entry(frame4, width=40, font=("Arial", 14))
    entry_education.pack(pady=5)
    
    label_school = tk.Label(frame4, text="School/University:", font=("Arial", 14), bg="white")
    label_school.pack(pady=5)
    entry_school = tk.Entry(frame4, width=40, font=("Arial", 14))
    entry_school.pack(pady=5)
    
    label_dates = tk.Label(frame4, text="Date (format: StartMonth Year - EndMonth Year):", font=("Arial", 14), bg="white")
    label_dates.pack(pady=5)
    entry_dates = tk.Entry(frame4, width=40, font=("Arial", 14))
    entry_dates.pack(pady=5)
    
    next_button = tk.Button(frame4, text="Next", font=("Arial", 14), command=collect_education_info)
    next_button.pack(pady=30)
    
    frame4.grid(row=0, column=0, sticky="nsew")

def collect_education_info():
    user_data["education"] = {
        "education": entry_education.get(),
        "school": entry_school.get(),
        "dates": entry_dates.get()
    }
    show_frame(frame5)

# Section 5: Skills
def section_5():
    global frame5, skill_entries
    frame5 = tk.Frame(root, width=900, height=600, bg="white")
    frame5.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    
    title = tk.Label(frame5, text="CV MAKER", font=("Arial", 24, "bold"), bg="white")
    title.pack(pady=20)
    
    motive = tk.Label(frame5, text="Create Your CV Instantly.", font=("Arial", 16), bg="white")
    motive.pack(pady=10)
    
    skill_entries = []
    for i in range(5):
        label_skill = tk.Label(frame5, text=f"Skill {i+1}:", font=("Arial", 14), bg="white")
        label_skill.pack(pady=5)
        entry_skill = tk.Entry(frame5, width=40, font=("Arial", 14))
        entry_skill.pack(pady=5)
        skill_entries.append(entry_skill)
    
    next_button = tk.Button(frame5, text="Next", font=("Arial", 14), command=collect_skills_info)
    next_button.pack(pady=30)
    
    frame5.grid(row=0, column=0, sticky="nsew")

def collect_skills_info():
    user_data["skills"] = [entry.get() for entry in skill_entries]
    if user_data["template"] in [1, 3]:
        show_frame(frame6)  # Move to Section 6 (Languages) if template 1 or 3 is selected
    else:
        process_cv()  # Otherwise, directly process the CV

# Section 6: Languages
def section_6():
    global frame6, language_entries
    frame6 = tk.Frame(root, width=900, height=600, bg="white")
    frame6.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    
    title = tk.Label(frame6, text="CV MAKER", font=("Arial", 24, "bold"), bg="white")
    title.pack(pady=20)
    
    motive = tk.Label(frame6, text="Create Your CV Instantly.", font=("Arial", 16), bg="white")
    motive.pack(pady=10)
    
    language_entries = []
    for i in range(3):
        label_language = tk.Label(frame6, text=f"Language {i+1}:", font=("Arial", 14), bg="white")
        label_language.pack(pady=5)
        entry_language = tk.Entry(frame6, width=40, font=("Arial", 14))
        entry_language.pack(pady=5)
        language_entries.append(entry_language)
    
    proceed_button = tk.Button(frame6, text="Proceed", font=("Arial", 14), command=process_cv)
    proceed_button.pack(pady=30)
    
    frame6.grid(row=0, column=0, sticky="nsew")

def create_loader_frame():
    global frame_loader, progress, message_label
    frame_loader = tk.Frame(root, width=900, height=600, bg="white")
    frame_loader.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    
    title = tk.Label(frame_loader, text="CV MAKER", font=("Arial", 24, "bold"), bg="white")
    title.pack(pady=20)
    
    motive = tk.Label(frame_loader, text="Processing Your Information...", font=("Arial", 16), bg="white")
    motive.pack(pady=10)
    
    message_label = tk.Label(frame_loader, text="", font=("Arial", 14), bg="white")
    message_label.pack(pady=10)
    
    progress = ttk.Progressbar(frame_loader, orient="horizontal", length=800, mode="determinate")
    progress.pack(pady=20)
    
    frame_loader.grid(row=0, column=0, sticky="nsew")

# Update the loader message and progress bar
def update_loader_message(messages, index=0):
    if index < len(messages):
        message_label.config(text=messages[index])
        root.update()
        
        # Determine the delay based on the message
        delay = 5000 if messages[index] == "Creating your CV" else random.randint(2000, 4000)
        
        progress_step = 100 / len(messages)
        progress['value'] = progress_step * (index + 1)
        root.update()
        
        root.after(delay, update_loader_message, messages, index + 1)
    else:
        root.after(1000, move_to_next_section)

# Move to the next section after processing
def move_to_next_section():
    frame_loader.destroy()
    if user_data["template"] in [1, 3]:
        show_frame(frame6)  # Show Section 6 if template 1 or 3 is selected
    else:
        process_cv_final()  # Replace with the function to handle the finalization

def process_cv():
    create_loader_frame()
    
    messages = ["Processing Inputs", "Analyzing Data", "Creating your CV", "Almost There"]
    
    # Calculate the remaining time to ensure total time is between 10 to 15 seconds
    total_processing_time = random.randint(10000, 15000)  # Total time between 10 and 15 seconds
    remaining_time = total_processing_time - 5000  # Subtract 5 seconds for the "Creating your CV" message
    
    # Update the loader messages
    update_loader_message(messages)
    
    # Ensure the total time is respected by setting a final delay
    root.after(remaining_time, move_to_next_section)

def process_cv_final():
    # Finalize the CV processing or show completion
    print(f"Finalized CV with user data: {user_data}")
    # Open the corresponding template file
    template_file = f"template_{user_data['template']}.py"
    try:
        module = importlib.import_module(template_file.replace('.py', ''))
        # Call a function in the module if needed, e.g., module.generate_cv(user_data)
        # For now, just print a message
        print(f"Loaded and processed template: {template_file}")
    except ModuleNotFoundError:
        print(f"Template file {template_file} not found.")
    
    # Show completion message
    messagebox.showinfo("CV Maker", "Your CV has been created successfully!")
    root.quit()  # Close the application

if __name__ == "__main__":
    # Initialize frames
    section_1()
    section_2()
    section_3()
    section_4()
    section_5()
    section_6()
    
    # Set the initial frame
    show_frame(frame1)
    
    # Start the Tkinter main loop
    root.mainloop()
