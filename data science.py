from sklearn import linear_model
from sklearn.model_selection import train_test_split
import pandas as pd

df = pd.read_csv("USA_Housing.csv")

X = df [["Avg. Area Income", "Avg. Area House Age", "Avg. Area Number of Rooms", "Avg. Area Number of Bedrooms", "Area Population"]]
y = df["Price"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=101)

reg = linear_model.LinearRegression()

reg.fit(X_train, y_train)



def Pridect():
    income = float(Area_Income_Entry.get())
    age = float(House_Age_Entry.get())
    rooms = float(Number_of_Rooms_Entry.get())
    bedrooms = float(Number_of_Bedrooms_Entry.get())
    population = float(Area_Population__Entry.get())

    input_data = pd.DataFrame([[income, age, rooms, bedrooms, population]], columns=["Avg. Area Income", "Avg. Area House Age", "Avg. Area Number of Rooms", "Avg. Area Number of Bedrooms", "Area Population"])

    price = reg.predict(input_data)

    result = f"The predicted price is: ${price[0]:,.2f}"
    messagebox.showinfo("Prediction Result", result)


import tkinter as tk
from tkinter import messagebox

window=tk.Tk()
window.geometry("500x200")

frame = tk.Frame(window)
frame.pack()

info_frame=tk.LabelFrame(frame,text="House information", padx=10, pady=10)
info_frame.pack()

Area_Income_label=tk.Label(info_frame,text="Area Income").grid(row=0,column=0)
Area_Income_Entry=tk.Entry(info_frame)

Area_Income_Entry.grid(row=1,column=0)

House_Age_label=tk.Label(info_frame,text="House Age").grid(row=0,column=1)
House_Age_Entry=tk.Entry(info_frame)
House_Age_Entry.grid(row=1,column=1,padx=5)

Number_of_Rooms_label=tk.Label(info_frame,text="Number of Rooms").grid(row=0,column=2)
Number_of_Rooms_Entry=tk.Entry(info_frame)
Number_of_Rooms_Entry.grid(row=1,column=2)

Number_of_Bedrooms_label=tk.Label(info_frame,text="Number of Bedrooms").grid(row=2,column=0)
Number_of_Bedrooms_Entry=tk.Entry(info_frame)
Number_of_Bedrooms_Entry.grid(row=3,column=0)

Area_Population_label=tk.Label(info_frame,text="Area Population").grid(row=2,column=2)
Area_Population__Entry=tk.Entry(info_frame)
Area_Population__Entry.grid(row=3,column=2)

predict_button = tk.Button(info_frame, text="Predict Price", command=Pridect ).grid(row=3, column=1, padx=5)

window.mainloop()



