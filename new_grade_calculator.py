import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Grade Calculator")
root.geometry("420x500")
root.configure(bg="#f0f8ff")  # Alice Blue background

# Scrollable Frame Setup
main_frame = tk.Frame(root, bg="#f0f8ff")
main_frame.pack(fill=tk.BOTH, expand=1)

canvas = tk.Canvas(main_frame, bg="#f0f8ff", highlightthickness=0)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

scrollbar = tk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas.configure(yscrollcommand=scrollbar.set)

# Frame inside the Canvas
scrollable_frame = tk.Frame(canvas, bg="#f0f8ff")
window = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

# --- Update scrollregion when content changes ---
def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

scrollable_frame.bind("<Configure>", on_frame_configure)

# --- Expand scrollable_frame to fill canvas width ---
def on_canvas_configure(event):
    canvas.itemconfig(window, width=event.width)

canvas.bind('<Configure>', on_canvas_configure)

# Use scrollable_frame as your main parent for content
content_frame = tk.Frame(scrollable_frame, bg="#f0f8ff")
content_frame.pack(fill="x", anchor="n", expand=True)

# LEFT & RIGHT LABELS
header_frame = tk.Frame(content_frame, bg="#f0f8ff")
header_frame.pack(fill="x", pady=(20, 0))

college_label = tk.Label(header_frame,
              text="Cadet College Kohat",
              font=("Arial",16,"bold"),
              bg="#f0f8ff",fg="#4169e1")  # Royal Blue
college_label.grid(row=0, column=0, sticky="w", padx=(30, 10))

class_label = tk.Label(header_frame,
              text="Class 9 & 10",
              font=("Arial",16,"bold"),
              bg="#f0f8ff",fg="#4169e1")  # Royal Blue
class_label.grid(row=0, column=1, sticky="e", padx=(10, 30))

# Make columns expand to fill available space
header_frame.grid_columnconfigure(0, weight=1)
header_frame.grid_columnconfigure(1, weight=1)


# Creating Grade Calculator label
title_label = tk.Label(content_frame,
              text="Grade Calculator",
              font=("Arial",16,"bold"),
              bg="#f0f8ff",fg="#ff6347")  # Tomato
title_label.pack(pady=20)

# Student name label
name_label = tk.Label(content_frame,
                 text="Student Name",
                 font=("Arial",12,"bold"),
                 bg="#f0f8ff",fg="#2e8b57")  # Sea Green
name_label.pack(pady=2)

# Creating entry
name_entry = tk.Entry(content_frame, width=30, bg="#ffffff", fg="#000000", 
                     highlightbackground="#4169e1", highlightthickness=1)
name_entry.pack(pady=10)

# Total Marks
label_2 = tk.Label(content_frame,
                 text="Enter Marks According To Your Paper's Maximum Marks",
                 font=("Arial",12,"bold"),
                 bg="#f0f8ff",fg="#2e8b57")  # Sea Green
label_2.pack(pady=10)

# 1. Maths
maths = tk.Label(content_frame,
                 text="1. Maths",
                 font=("Arial",12,"bold"),
                 bg="#f0f8ff",fg="#4682b4")  # Steel Blue
maths.pack(pady=2)

maths_entry = tk.Entry(content_frame, width=30, bg="#ffffff", fg="#000000",
                      highlightbackground="#4682b4", highlightthickness=1)
maths_entry.pack(pady=5)

# 2. English
english = tk.Label(content_frame,
                   text="2. English",
                   font=("Arial",12,"bold"),
                   bg="#f0f8ff",fg="#4682b4")  # Steel Blue
english.pack(pady=2)

english_entry = tk.Entry(content_frame, width=30, bg="#ffffff", fg="#000000",
                        highlightbackground="#4682b4", highlightthickness=1)
english_entry.pack(pady=5)

# 3. Biology
bio = tk.Label(content_frame,
               text="3. Biology",
               font=("Arial",12,"bold"),
               bg="#f0f8ff",fg="#4682b4")  # Steel Blue
bio.pack(pady=2)

bio_entry = tk.Entry(content_frame, width=30, bg="#ffffff", fg="#000000",
                    highlightbackground="#4682b4", highlightthickness=1)
bio_entry.pack(pady=5)

# 4. Chemistry
chem = tk.Label(content_frame,
                text="4. Chemistry",
                font=("Arial",12,"bold"),
                bg="#f0f8ff",fg="#4682b4")  # Steel Blue
chem.pack(pady=2)

chem_entry = tk.Entry(content_frame, width=30, bg="#ffffff", fg="#000000",
                     highlightbackground="#4682b4", highlightthickness=1)
chem_entry.pack(pady=5)

# 5. Physics
phy = tk.Label(content_frame,
               text="5. Physics",
               font=("Arial",12,"bold"),
               bg="#f0f8ff",fg="#4682b4")  # Steel Blue
phy.pack(pady=2)

phy_entry = tk.Entry(content_frame, width=30, bg="#ffffff", fg="#000000",
                    highlightbackground="#4682b4", highlightthickness=1)
phy_entry.pack(pady=5)

# 6. Urdu
urdu = tk.Label(content_frame,
                text="6. Urdu",
                font=("Arial",12,"bold"),
                bg="#f0f8ff",fg="#4682b4")  # Steel Blue
urdu.pack(pady=2)

urdu_entry = tk.Entry(content_frame, width=30, bg="#ffffff", fg="#000000",
                     highlightbackground="#4682b4", highlightthickness=1)
urdu_entry.pack(pady=5)

# 7. Pak Studies
pakst = tk.Label(content_frame,
                 text="7. Pakistan Studies",
                 font=("Arial",12,"bold"),
                 bg="#f0f8ff",fg="#4682b4")  # Steel Blue
pakst.pack(pady=2)

pakst_entry = tk.Entry(content_frame, width=30, bg="#ffffff", fg="#000000",
                      highlightbackground="#4682b4", highlightthickness=1)
pakst_entry.pack(pady=5)

# 8. Mutal e Quran
mquran = tk.Label(content_frame,
                  text="8. Mutal-e-Quran",
                  font=("Arial",12,"bold"),
                  bg="#f0f8ff",fg="#4682b4")  # Steel Blue
mquran.pack(pady=2)

mquran_entry = tk.Entry(content_frame, width=30, bg="#ffffff", fg="#000000",
                       highlightbackground="#4682b4", highlightthickness=1)
mquran_entry.pack(pady=5)

# 9. Islamiyat
isl = tk.Label(content_frame,
               text="9. Islamiyat",
               font=("Arial",12,"bold"),
               bg="#f0f8ff",fg="#4682b4")  # Steel Blue
isl.pack(pady=2)

isl_entry = tk.Entry(content_frame, width=30, bg="#ffffff", fg="#000000",
                    highlightbackground="#4682b4", highlightthickness=1)
isl_entry.pack(pady=5)

# Creating label for remarks
displayed = tk.Label(content_frame,
                     text="Your Grades And Marks Are Displayed Below",
                     font=("Arial",12,"bold"),
                     bg="#f0f8ff",fg="#ff6347")  # Tomato
displayed.pack(pady=2)

def calculate_marks():
    try:
        name = name_entry.get()
        math_marks = float(maths_entry.get())
        english_marks = float(english_entry.get())
        urdu_marks = float(urdu_entry.get())
        bio_marks = float(bio_entry.get())
        chem_marks = float(chem_entry.get())
        phy_marks = float(phy_entry.get())
        pakst_marks = float(pakst_entry.get())
        isl_marks = float(isl_entry.get())
        mquran_marks = float(mquran_entry.get())

        if not name.strip():
            messagebox.showerror("Error", "Please enter student name")
            return

        if (
            math_marks < 0 or math_marks > 75 or
            english_marks < 0 or english_marks > 75 or
            urdu_marks < 0 or urdu_marks > 75 or
            bio_marks < 0 or bio_marks > 75 or
            chem_marks < 0 or chem_marks > 75 or
            phy_marks < 0 or phy_marks > 75 or
            pakst_marks < 0 or pakst_marks > 50 or
            isl_marks < 0 or isl_marks > 50 or
            mquran_marks < 0 or mquran_marks > 50
        ):
            messagebox.showerror("Error", "Enter marks according to your papers maximum marks")
            return

        obtained = (
            math_marks + english_marks + urdu_marks + bio_marks +
            chem_marks + phy_marks + pakst_marks + isl_marks + mquran_marks
        )
        # Calculate total marks and percentage correctly
        total_marks = 75*6 + 50*3  # 6 subjects x 75, 3 subjects x 50 = 600
        percentage = (obtained / total_marks) * 100

        # Grade based on percentage
        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 50:
            grade = "D"
        else:
            grade = "FAIL"

        result = (
            f"Student Name: {name}\n"
            f"Obtained Marks: {obtained}\n"
            f"Total Marks: {total_marks}\n"
            f"Percentage: {percentage:.2f}\n"
            f"Grade: {grade}"
        )
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, result)

    except ValueError:
        messagebox.showerror("ERROR", "Enter valid numeric marks and name")

# Creating text area for any remarks or note
text_area = tk.Text(content_frame, height=8, width=40, bg="#ffffff", fg="#000000",
                   highlightbackground="#4169e1", highlightthickness=1)
text_area.pack(pady=10)

def clearall():
    name_entry.delete(0, tk.END)
    bio_entry.delete(0, tk.END)
    maths_entry.delete(0, tk.END)
    english_entry.delete(0, tk.END)
    chem_entry.delete(0, tk.END)
    text_area.delete("1.0", tk.END)
    phy_entry.delete(0, tk.END)
    urdu_entry.delete(0, tk.END)
    pakst_entry.delete(0, tk.END)
    isl_entry.delete(0, tk.END)
    mquran_entry.delete(0, tk.END)

calculate_grade = tk.Button(content_frame,
                            text="Calculate",
                            bg="#4CAF50", fg="white",  # Green
                            font=("Arial", 10, "bold"),
                            activebackground="#45a049",
                            command=calculate_marks)
calculate_grade.pack(pady=10)

clear = tk.Button(content_frame,
                  text="Clear All",
                  bg="#f44336", fg="white",  # Red
                  font=("Arial", 10, "bold"),
                  activebackground="#d32f2f",
                  command=clearall)
clear.pack(pady=10)

root.mainloop()
