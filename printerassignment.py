import tkinter as tk
from tkinter import filedialog
import win32print

class PrinterApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Printer App")

        self.printers = self.get_connected_printers()

        self.printer_var = tk.StringVar(value=self.printers[0] if self.printers else "")
        self.file_var = tk.StringVar(value="No file selected")

        self.printer_label = tk.Label(master, text="Select Printer:")
        self.printer_label.grid(row=0, column=0, sticky="w")

        self.printer_option = tk.OptionMenu(master, self.printer_var, *self.printers)
        self.printer_option.grid(row=0, column=1, sticky="w")

        self.browse_button = tk.Button(master, text="Browse File", command=self.browse_file)
        self.browse_button.grid(row=1, column=0, columnspan=2, pady=10)

        self.file_label = tk.Label(master, text="Selected File:")
        self.file_label.grid(row=2, column=0, sticky="w")

        self.file_entry = tk.Entry(master, textvariable=self.file_var, state="readonly", width=40)
        self.file_entry.grid(row=2, column=1, sticky="w")

        self.print_button = tk.Button(master, text="Print", command=self.print_file)
        self.print_button.grid(row=3, column=0, columnspan=2, pady=10)

    def get_connected_printers(self):
        printers = []
        printer_info = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL, None, 1)
        for printer in printer_info:
            printers.append(printer[2])
        return printers

    def browse_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.file_var.set(file_path)

    def print_file(self):
        printer_name = self.printer_var.get()
        file_path = self.file_var.get()
        if not printer_name:
            tk.messagebox.showerror("Error", "Please select a printer.")
            return
        if file_path == "No file selected":
            tk.messagebox.showerror("Error", "Please select a file.")
            return
        # Here you can add code to send the file to the selected printer
        tk.messagebox.showinfo("Print", f"File '{file_path}' printed successfully to '{printer_name}'.")

def main():
    root = tk.Tk()
    app = PrinterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
