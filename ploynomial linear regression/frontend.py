import tkinter as tk
import joblib
from sklearn.preprocessing import PolynomialFeatures

model = joblib.load("predcterrr.joblib")

def precdictresilt():
    x = float(en1.get())

    xyz = PolynomialFeatures(degree = 2)
    chnage_inp = xyz.fit_transform([[x]])
    result = model.predict(chnage_inp)

    lblshow.config(text = f"Your Predicted output is : {result[0]}")

app = tk.Tk()

app.geometry("600x400")
app.title("predictor")
app.config(background = "lightgray")

fram1 = tk.Frame(app, relief = "groove", borderwidth = 15, background="#36383b")
fram1.pack(fill="x")

fram2 = tk.Frame(app, relief = "raised", borderwidth = 15, background="#36383b")
fram2.pack(fill="x")

lbl = tk.Label(fram1, text = "Predictor", font = ("robort", 30, "bold"), fg = "white", bg = "black")
lbl.pack(fill="x", ipady = 10)




lblx = tk.Label(fram2, font = ("robort", 20, "bold",), background = "#36383b")
lbl1 = tk.Label(fram2, text = "Input 1", font = ("robort", 20, "bold",), background = "#36383b")
lbl3 = tk.Label(fram2, text = ":", font = ("robort", 20, "bold"), background = "#36383b")

en1 = tk.Entry(fram2, font = ("robort", 20))

lblx.grid(row = 0, column = 0, padx  = 10)
lbl1.grid(row = 1, column = 1)
lbl3.grid(row = 1, column = 2, padx  = 10)
en1.grid(row = 1, column = 3)


btn = tk.Button(fram2, text = "Check", font = ("robort", 20, "bold"), fg = "white", bg = "black", command = precdictresilt)
btn.grid(row = 3, column = 3)





fram3 = tk.Frame(app, relief = "raised", borderwidth = 15, background="#36383b")
fram3.pack(fill="x", ipady = 5 )

lblshow = tk.Label(fram3, text=  "asdasdasd", background = "#36383b",fg = "white" , font = ("robort", 16))
lblshow.pack()
app.mainloop()