import pickle
import numpy as np
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Load trained model
try:
    with open("house_price_model.pkl", "rb") as file:
        model = pickle.load(file)
    print("MODEL LOADED SUCCESSFULLY")
except Exception as e:
    print("MODEL LOAD ERROR:", e)
    model = None


# HOME PAGE (UI)
@app.route("/")
def home():
    return render_template("index.html")


# STUDENT ENDPOINT
@app.route("/student", methods=["GET"])
def student():
    return jsonify({
        "name": "Sebin",
        "course": "Computer Science"
    })


# ADD ENDPOINT
@app.route("/add", methods=["POST"])
def add():

    data = request.get_json()

    return jsonify({
        "sum": data["a"] + data["b"]
    })


# UPDATE ENDPOINT
@app.route("/update", methods=["PUT"])
def update():

    data = request.get_json()

    return jsonify({
        "message": "Record Updated",
        "data": data
    })


# DELETE ENDPOINT
@app.route("/delete", methods=["DELETE"])
def delete():

    return jsonify({
        "message": "Record Deleted Successfully"
    })


# PREDICT ENDPOINT
@app.route("/predict", methods=["POST"])
def predict():

    if model is None:
        return jsonify({
            "error": "Model not loaded"
        }), 500

    try:

        data = request.get_json()

        features = [[
            data["OverallQual"],
            data["YearBuilt"],
            data["YearRemodAdd"],
            data["TotalBsmtSF"],
            data["1stFlrSF"],
            data["GrLivArea"],
            data["FullBath"],
            data["TotRmsAbvGrd"],
            data["GarageCars"],
            data["GarageArea"],
            data["MSZoning_C (all)"],
            data["MSZoning_FV"],
            data["MSZoning_RH"],
            data["MSZoning_RL"],
            data["MSZoning_RM"],
            data["Utilities_AllPub"],
            data["Utilities_NoSeWa"],
            data["BldgType_1Fam"],
            data["BldgType_2fmCon"],
            data["BldgType_Duplex"],
            data["BldgType_Twnhs"],
            data["BldgType_TwnhsE"],
            data["Heating_Floor"],
            data["Heating_GasA"],
            data["Heating_GasW"],
            data["Heating_Grav"],
            data["Heating_OthW"],
            data["Heating_Wall"],
            data["KitchenQual_Ex"],
            data["KitchenQual_Fa"],
            data["KitchenQual_Gd"],
            data["KitchenQual_TA"],
            data["SaleCondition_Abnorml"],
            data["SaleCondition_AdjLand"],
            data["SaleCondition_Alloca"],
            data["SaleCondition_Family"],
            data["SaleCondition_Normal"],
            data["SaleCondition_Partial"],
            data["LandSlope_Gtl"],
            data["LandSlope_Mod"],
            data["LandSlope_Sev"]
        ]]

        prediction = model.predict(np.array(features))

        return jsonify({
            "Predicted Price": float(prediction[0])
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)