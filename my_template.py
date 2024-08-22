import tkinter as tk
from tkinter.font import Font

# Create the main window
window = tk.Tk()

# Set the window size to A4 dimensions in (794 x 1123) pixels at 96 dpi
window.geometry("794x1123") # A4 dimensions in pixels at 96 dpi
window.resizable(False, True)

window.title("Template 1")

# Define fonts
header_font = Font(family="Helvetica", size=20, weight="bold")
subheader_font = Font(family="Helvetica", size=12, weight="bold")
normal_font = Font(family="Helvetica", size=12)
small_font = Font(family="Helvetica", size=10)

# Create a canvas
canvas = tk.Canvas(window, width=794, height=1123)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Add a scrollbar
scrollbar = tk.Scrollbar(window, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
canvas.configure(yscrollcommand=scrollbar.set)

# Create a frame inside the canvas
frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor="nw")

# Update the scroll region when the frame changes size
def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

frame.bind("<Configure>", on_frame_configure)

# Draw a rectangle for the header background
header_bg = tk.Label(frame, bg="#000000", width=794, height=150)
header_bg.place(x=0, y=0, width=794, height=150)

# Add header text
header_name = tk.Label(frame, text="DENVER DAHL", font=header_font, fg="white", bg="#000000", anchor="nw")
header_name.place(x=100, y=40)
header_title = tk.Label(frame, text="Account Manager", font=subheader_font, fg="white", bg="#000000", anchor="nw")
header_title.place(x=100, y=80)
header_contact = tk.Label(frame, text="☎ +1 555 555 5555    📧 denver.dahl@example.com    🔗 linkedin.com/denver-dahl",
                          font=small_font, fg="white", bg="#000000", anchor="nw")
header_contact.place(x=100, y=110)

# Add section titles with underline
experience_title = tk.Label(frame, text="EXPERIENCE", font=subheader_font, fg="black", anchor="nw")
experience_title.place(x=50, y=180)
experience_underline = tk.Frame(frame, bg="black", width=650, height=3)
experience_underline.place(x=50, y=200)

education_title = tk.Label(frame, text="EDUCATION", font=subheader_font, fg="black", anchor="nw")
education_title.place(x=50, y=540)
education_underline = tk.Frame(frame, bg="black", width=650, height=3)
education_underline.place(x=50, y=560)

skills_title = tk.Label(frame, text="SKILLS", font=subheader_font, fg="black", anchor="nw")
skills_title.place(x=50, y=650)
skills_underline = tk.Frame(frame, bg="black", width=650, height=3)
skills_underline.place(x=50, y=670)

languages_title = tk.Label(frame, text="LANGUAGES", font=subheader_font, fg="black", anchor="nw")
languages_title.place(x=50, y=770)
languages_underline = tk.Frame(frame, bg="black", width=650, height=3)
languages_underline.place(x=50, y=790)

# Add experience content
experience_text = """Key Account Manager
Lauzon
🗓2016 - Ongoing    📍 San Francisco, CA
Lauzon is a leading worldwide manufacturer, designer, and supplier of bearings, linear motion products, precision bearings, spindles, seals, and services. Responsible for business development with Key Accounts with main focus in ENERGY, POWER UTILITIES and HEAVY industries.
• Achieved 12% growth in the account's revenue and 7% profitability improvement.
• Generated $2,000,000+ new revenue by signing 10 new accounts.
• Presented to over 600 delegates in Europe for facilitating new insurance tracking process.
• Established a Cloud Team and increased Cloud Business profit 8X.

Senior Account Manager
Koep Inc
🗓 2014 - 2016    📍 San Francisco, CA
Koep Inc is Google Street View certified agency.
• Managed Search, Shopping & Display ads for major brands with total monthly ad spend of around $150,000/month.
• Managed the largest key account generating $17,500,000 annually.
• Worked with the BSO team for 6 months as being the sole responsible for their online marketing campaigns.
"""

experience_content = tk.Label(frame, text=experience_text, font=small_font, fg="black", anchor="nw", justify=tk.LEFT)
experience_content.place(x=50, y=210, width=650)

# Add education content
education_text = """Master of Marketing Management [MMM]
La Trobe University
2007 - 2008    San Francisco, CA"""
education_content = tk.Label(frame, text=education_text, font=small_font, fg="black", anchor="nw", justify=tk.LEFT)
education_content.place(x=50, y=580)

# Add skills content
skills_text = """MS Office Programs     Windows & Mac OSX     Asana     Salesforce     Agile     CRM Systems     Hubspot
LinkedIn Sales Navigator     Dun & Bradstreet"""
skills_content = tk.Label(frame, text=skills_text, font=small_font, fg="black", anchor="nw", justify=tk.LEFT)
skills_content.place(x=50, y=680)

# Add languages content
languages_text = """English - Native
German - Proficient
Greek - Advanced"""
languages_content = tk.Label(frame, text=languages_text, font=small_font, fg="black", anchor="nw", justify=tk.LEFT)
languages_content.place(x=50, y=800)

window.mainloop()

