import tkinter

window = tkinter.Tk()
window.title("BMI Calculator")
window.config(padx=65, pady=30)


def calculateBMI():
    height = heightInput.get()
    weight = weightInput.get()

    if weight == "" or height == "":
        resultLabel.config(text="Enter both weight and height!")
    else:
        try:
            bmi = float(weight) / (float(height)/100) ** 2
            resultString = writeResult(bmi)
            resultLabel.config(text=resultString)
        except:
            resultLabel.config(text="Enter a valid number!")


def writeResult(bmi):
    resultString = f"Your BMI is: {round(bmi,2)}.You are "
    if bmi <= 16:
        resultString += "severely thin!"
    elif 16 < bmi <= 17:
        resultString += "moderately thin!"
    elif 17 < bmi <= 18.5:
        resultString += "mild thin!"
    elif 18.5 < bmi <= 25:
        resultString += "normal"
    elif 25 < bmi <= 30:
        resultString += "overweight"
    elif 30 < bmi <= 35:
        resultString += "obese class 1"
    elif 35 < bmi <= 40:
        resultString += "obese class 2!"
    else:
        resultString += "obese class 3"
    return resultString
# UI


weightInputLabel = tkinter.Label(text="Enter your weight (kg)")
weightInputLabel.pack()

weightInput = tkinter.Entry(width=10)
weightInput.pack()

heightInputLabel = tkinter.Label(text="Enter your height (cm)")
heightInputLabel.pack()

heightInput = tkinter.Entry(width=10)
heightInput.pack()

calculateButton = tkinter.Button(text="Calculator", command=calculateBMI)
calculateButton.pack()

resultLabel = tkinter.Label()
resultLabel.pack()


window.mainloop()
