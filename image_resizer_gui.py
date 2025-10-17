import os
from tkinter import Tk, Label, Button, Entry, filedialog, messagebox
from PIL import Image

class ImageResizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📸 Image Resizer Tool")
        self.root.geometry("450x350")
        self.root.config(bg="#f0f0f0")

        Label(root, text="Image Resizer", font=("Segoe UI", 18, "bold"), bg="#f0f0f0", fg="#333").pack(pady=10)

        Button(root, text="Select Folder", command=self.select_folder, bg="#0078D7", fg="white", font=("Segoe UI", 10, "bold")).pack(pady=10)
        self.folder_path_label = Label(root, text="No folder selected", bg="#f0f0f0", fg="#555")
        self.folder_path_label.pack()

        Label(root, text="Width:", bg="#f0f0f0").pack(pady=(15, 0))
        self.width_entry = Entry(root, width=10)
        self.width_entry.pack()

        Label(root, text="Height:", bg="#f0f0f0").pack(pady=(10, 0))
        self.height_entry = Entry(root, width=10)
        self.height_entry.pack()

        Button(root, text="Resize Images", command=self.resize_images, bg="#28a745", fg="white", font=("Segoe UI", 10, "bold")).pack(pady=20)

        self.status_label = Label(root, text="", bg="#f0f0f0", fg="#333")
        self.status_label.pack()

        self.selected_folder = ""

    def select_folder(self):
        """Select the folder containing images"""
        folder = filedialog.askdirectory(title="Select Folder with Images")
        if folder:
            self.selected_folder = folder
            self.folder_path_label.config(text=folder)
            self.status_label.config(text="")

    def resize_images(self):
        """Resize all images in the selected folder"""
        if not self.selected_folder:
            messagebox.showwarning("Warning", "Please select a folder first!")
            return

        try:
            width = int(self.width_entry.get())
            height = int(self.height_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Width and Height must be integers!")
            return

        output_folder = os.path.join(self.selected_folder, "Resized_Images")
        os.makedirs(output_folder, exist_ok=True)

        count = 0
        for file in os.listdir(self.selected_folder):
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                img_path = os.path.join(self.selected_folder, file)
                img = Image.open(img_path)
                img = img.resize((width, height))
                img.save(os.path.join(output_folder, file))
                count += 1

        self.status_label.config(text=f"✅ Resized {count} images saved in '{output_folder}'")
        messagebox.showinfo("Success", f"{count} images resized and saved in:\n{output_folder}")

if __name__ == "__main__":
    root = Tk()
    app = ImageResizerApp(root)
    root.mainloop()
