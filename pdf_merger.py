import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfMerger, PdfReader, PdfWriter
import os

class PDFToolApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📚 PDF Merger & Splitter")
        self.root.geometry("400x320")
        self.root.resizable(False, False)
        self.root.configure(bg="#f5f5f5")

        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(self.root, text="📄 PDF Merger & Splitter", font=("Segoe UI", 16, "bold"), bg="#f5f5f5", fg="#333")
        title.pack(pady=20)

        self.create_button("📎 Merge PDFs", self.merge_pdfs_gui).pack(pady=10)
        self.create_button("✂️ Split PDF", self.split_pdf_gui).pack(pady=10)
        self.create_button("❌ Exit", self.root.quit).pack(pady=10)

    def create_button(self, text, command):
        btn = tk.Button(self.root, text=text, font=("Segoe UI", 12), width=25, height=2, bg="#4CAF50", fg="white", bd=0, activebackground="#45a049", command=command)
        return btn

    def merge_pdfs_gui(self):
        files = filedialog.askopenfilenames(title="Select PDFs to Merge", filetypes=[("PDF Files", "*.pdf")])
        if not files:
            return

        output_file = filedialog.asksaveasfilename(defaultextension=".pdf", title="Save Merged PDF As",
                                                   filetypes=[("PDF Files", "*.pdf")])
        if not output_file:
            return

        try:
            merger = PdfMerger()
            for pdf in files:
                merger.append(pdf)
            merger.write(output_file)
            merger.close()
            messagebox.showinfo("✅ Success", f"PDFs merged into:\n{output_file}")
        except Exception as e:
            messagebox.showerror("❌ Error", f"Something went wrong:\n{e}")

    def split_pdf_gui(self):
        file = filedialog.askopenfilename(title="Select a PDF to Split", filetypes=[("PDF Files", "*.pdf")])
        if not file:
            return

        output_folder = filedialog.askdirectory(title="Select Folder to Save Split Pages")
        if not output_folder:
            return

        try:
            reader = PdfReader(file)
            for i, page in enumerate(reader.pages):
                writer = PdfWriter()
                writer.add_page(page)
                output_path = os.path.join(output_folder, f"page_{i + 1}.pdf")
                with open(output_path, "wb") as f:
                    writer.write(f)
            messagebox.showinfo("✅ Success", f"Split into {len(reader.pages)} pages in:\n{output_folder}")
        except Exception as e:
            messagebox.showerror("❌ Error", f"Something went wrong:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFToolApp(root)
    root.mainloop()
