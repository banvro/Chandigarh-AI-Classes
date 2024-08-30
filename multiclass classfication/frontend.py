import tkinter as tk 
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
import joblib
import pandas as pd
from PIL import ImageOps


model = joblib.load("image_predictorr.joblib")

def predictimage(filepath):
    img = Image.open(filepath)
    img = ImageOps.grayscale(img)
    chnage_size = img.resize((28, 28))
    # chnage_type
    new_image = np.array(chnage_size)
    # print(new_image)
    image_row = new_image.flatten()
    print(image_row.shape)
    # print(image_row)
    reshaped_image = image_row.reshape(1, -1)
     

    output = model.predict(reshaped_image)

    return output

def uploadimage():
    file = filedialog.askopenfilename()
    img = Image.open(file)
    show = ImageTk.PhotoImage(img)

    lbl2.config(image = show)
    lbl2.image = show

    result = predictimage(file)
    # btn.config(text = "Predict", command = predictimage)
    print(result, "oooutttput")
    


app = tk.Tk()
app.geometry("700x600")
app.config(background = "#a6f763")
app.title("Image Predictor")


lbl = tk.Label(app, text = "Image Predictor", font = ("robort", 30, "bold"), background = "#1f4201", fg = "white")
lbl.pack(fill = "x", ipady = 10)

lbl2 = tk.Label(app)
lbl2.pack(pady = 20)

btn = tk.Button(app, text = "Upload Image", font = ("robort", 20, "bold"), background = "#1f4201", fg = "white", command = uploadimage)
btn.pack()


app.mainloop()