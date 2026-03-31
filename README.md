# House Price Prediction System for Day Scholars

## Project Overview

This project is a Machine Learning-based system that predicts house rental prices for students (day scholars) who prefer living outside college hostels. The prediction is based on features such as area, number of rooms, distance from college, and furnishing status.

The system helps students make informed decisions while choosing accommodation.

---

## Features

* Predicts house rent based on input parameters
* Uses Machine Learning (Linear Regression)
* Simple and user-friendly console interface
* Model saving and loading using pickle

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Pickle

---

## Project Structure

```
house-price-prediction/
│── data.csv
│── main.py
│── model.pkl
│── requirements.txt
│── README.md
```

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/house-price-prediction.git
```

2. Navigate to the project folder:

```bash
cd house-price-prediction
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Requirements File

Create a file named `requirements.txt` with the following content:

```
pandas
numpy
scikit-learn
```

---

## Dataset

The project uses a dataset file named `data.csv`.

If the file is not available, create it manually with the following format:

```
area,bedrooms,bathrooms,location_distance,furnishing,price
1200,2,2,5,1,15000
800,1,1,2,0,10000
1500,3,2,8,1,20000
1000,2,1,3,0,12000
1300,2,2,6,1,17000
```

### Important:

* File name must be exactly `data.csv`
* It should be placed in the same folder as `main.py`

---

## How to Run

1. Ensure Python is installed on your system
2. Make sure `data.csv` is present in the project folder
3. Run the program:

```bash
python main.py
```

4. Enter the required details when prompted
5. The system will display the predicted rent

---

## Example

```
Area (sq ft): 1200
Bedrooms: 2
Bathrooms: 2
Distance from college (km): 5
Furnishing (1 = Yes, 0 = No): 1

Estimated Rent: ₹ 15000
```

---

## Machine Learning Model

* Algorithm Used: Linear Regression
* Type: Supervised Learning
* Task: Regression

---


## References

* Scikit-learn Documentation
* Python Documentation
* Machine Learning Course Materials

---
