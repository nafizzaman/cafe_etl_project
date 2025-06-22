import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import pandas as pd
import os

from etl.extract import extract_orders
from etl.transform import transform_orders
from etl.load import load_to_sql

df_raw = None
df_clean = None
selected_file = "data/orders.csv"

def browse_file(label):
    global selected_file
    file_path = filedialog.askopenfilename(
        title="Select CSV File",
        filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
    )
    if file_path:
        selected_file = file_path
        label.config(text=f"Selected: {file_path}")

def extract_action():
    global df_raw, selected_file
    try:
        df_raw = extract_orders(selected_file)
        messagebox.showinfo("Extract", f"Extracted data from:\n{selected_file}")
    except FileNotFoundError:
        messagebox.showerror("Error", f"File not found:\n{selected_file}")

def transform_action():
    global df_raw, df_clean
    if df_raw is None:
        messagebox.showwarning("Warning", "Please extract data first.")
    else:
        df_clean = transform_orders(df_raw)
        messagebox.showinfo("Transform", "Data transformed and cleaned.")

def load_action():
    global df_clean
    if df_clean is None:
        messagebox.showwarning("Warning", "Please transform data first.")
    else:
        load_to_sql(df_clean)
        messagebox.showinfo("Load", "Data loaded into SQL Server.")
        
def full_etl_action():
    global df_raw, df_clean, selected_file
    try:
        df_raw = extract_orders(selected_file)
        df_clean = transform_orders(df_raw)
        load_to_sql(df_clean)
        messagebox.showinfo("Full ETL", "Extract, Transform, and Load completed successfully.")
    except FileNotFoundError:
        messagebox.showerror("Error", f"File not found:\n{selected_file}")
    except Exception as e:
        messagebox.showerror("ETL Error", str(e))


def export_action():
    global df_clean
    if df_clean is None:
        messagebox.showwarning("Warning", "No cleaned data to export.")
    else:
        df_clean.to_csv("output.csv", index=False)
        messagebox.showinfo("Export", "Cleaned data exported to output.csv.")

def view_cleaned_data():
    global df_clean
    if df_clean is None:
        messagebox.showwarning("Warning", "No cleaned data to display.")
        return

    win = tk.Toplevel()
    win.title("Cleaned Data Preview")
    win.geometry("800x400")

    text = scrolledtext.ScrolledText(win, wrap=tk.WORD, font=("Courier", 10))
    text.pack(expand=True, fill=tk.BOTH)

    preview = df_clean.to_string(index=False)
    text.insert(tk.END, preview)

def view_logs():
    log_path = "etl.log"
    if not os.path.exists(log_path):
        messagebox.showwarning("Warning", "No log file found.")
        return

    win = tk.Toplevel()
    win.title("ETL Log Viewer")
    win.geometry("800x400")

    text = scrolledtext.ScrolledText(win, wrap=tk.WORD, font=("Courier", 10))
    text.pack(expand=True, fill=tk.BOTH)

    with open(log_path, "r") as f:
        content = f.read()
        text.insert(tk.END, content)

def gui_menu():
    window = tk.Tk()
    window.title("Café ETL GUI")
    window.geometry("400x500")

    tk.Label(window, text="Café ETL Pipeline", font=("Arial", 16)).pack(pady=10)

    path_label = tk.Label(window, text=f"Selected: {selected_file}", wraplength=380)
    path_label.pack(pady=2)

    tk.Button(window, text="Browse File", width=25, command=lambda: browse_file(path_label)).pack(pady=5)
    tk.Button(window, text="Extract", width=25, command=extract_action).pack(pady=5)
    tk.Button(window, text="Transform", width=25, command=transform_action).pack(pady=5)
    tk.Button(window, text="Load", width=25, command=load_action).pack(pady=5)
    tk.Button(window, text="Run Full ETL", width=25, command=full_etl_action).pack(pady=5)
    tk.Button(window, text="Export Cleaned Data", width=25, command=export_action).pack(pady=5)
    tk.Button(window, text="View Cleaned Data", width=25, command=view_cleaned_data).pack(pady=5)
    tk.Button(window, text="View Logs", width=25, command=view_logs).pack(pady=5)
    tk.Button(window, text="Exit", width=25, command=window.quit).pack(pady=15)

    window.mainloop()
