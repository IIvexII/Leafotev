import tkinter as tk
from tkinter import Canvas, Frame
from tkinter import filedialog
from PIL import Image, ImageTk
import requests

SERVER_URL = "http://127.0.0.1:8000"

class LeafotevApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Leafotev 🍃")
        self.root.geometry("600x600")
        self.root.iconbitmap("resources/_.ico")

        self.background_image = tk.PhotoImage(file="resources/background.png") 
        self.background_label = tk.Label(self.root, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # home widgets
        self.home_widgets()

        # footer
        self.footer = tk.Label(self.root, text="Computer Vision Term Project", bg="#83B333", fg="#ffffff", font=("Arial", 16))        
        self.footer.pack(side=tk.BOTTOM, fill=tk.X)

    def load_iamge(self):
        self.image_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])

        if self.image_path:
            # make back button < with #83B333 background
            self.back_image = tk.PhotoImage(file="resources/back_btn.png")
            self.back_button = tk.Button(self.root, image=self.back_image, command=self.back,borderwidth=0, bg="#83B333")
            self.back_button.place(relx=0.1, rely=0.2, anchor=tk.CENTER)

            # Display the selected image
            image = Image.open(self.image_path)
            image = image.resize((256, 256))
            photo = ImageTk.PhotoImage(image)

            # destroy upload button
            self.upload_button.destroy()

            # show image
            self.image_label = tk.Label(self.root, image=photo)
            self.image_label.image = photo
            self.image_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

            # predict disease
            self.predict_disease()
    
    def back(self):
        self.image_label and self.image_label.destroy()
        self.back_button and self.back_button.destroy()
        self.result_label and self.result_label.destroy()
        
        self.home_widgets()

    def home_widgets(self):
        # show custom button image
        self.upload_image = tk.PhotoImage(file="resources/upload_btn.png")    
        self.upload_button = tk.Button(self.root, image=self.upload_image, command=self.load_iamge,borderwidth=0, bg="#ffffff")
        self.upload_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def predict_disease(self):
        if self.image_path:
            files = {'file': open(self.image_path, 'rb')}

            try:
                r = requests.post(SERVER_URL, files=files)
                result_text = r.json()["prediction"]
                bg_color = "#83B333"                
            except:
                result_text = "Server Error"
                bg_color = "#FF0000"                

            self.result_label = tk.Label(self.root,text=result_text, bg=bg_color, fg="white", font=("Arial", 16))
            self.result_label.config(width=15, height=2)
            self.result_label.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

if __name__ == "__main__":
    root = tk.Tk()
    app = LeafotevApp(root)
    root.mainloop()
