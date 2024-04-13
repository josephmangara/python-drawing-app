import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Drawing App")
        
        self.drawing_area = tk.Canvas(self.root, width=600, height=400, bg="white")
        self.drawing_area.pack(pady=20)
        
        self.drawing_area.bind("<B1-Motion>", self.draw)
        
        self.clear_button = ttk.Button(self.root, text="Clear", command=self.clear_drawing)
        self.clear_button.pack(side=tk.LEFT, padx=10, pady=10)
        
        self.save_button = ttk.Button(self.root, text="Save", command=self.save_drawing)
        self.save_button.pack(side=tk.RIGHT, padx=10, pady=10)
        
    def draw(self, event):
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)
        self.drawing_area.create_oval(x1, y1, x2, y2, fill="black", width=5)
        
    def clear_drawing(self):
        self.drawing_area.delete("all")
        
    def save_drawing(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".ps", filetypes=[("PostScript files", "*.ps"), ("PNG files", "*.png")])
        
        if file_path:
            if file_path.endswith(".ps"):
                self.drawing_area.postscript(file=file_path, colormode="color")
            elif file_path.endswith(".png"):
                self.drawing_area.postscript(file="temp.ps", colormode="color")
                img = Image.open("temp.ps")
                img.save(file_path, "png")

if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()
