from flask import Flask,render_template,request
app=Flask(__name__)

import joblib
model = joblib.load(r"C:\Users\RIya\Desktop\6month-Data-Science\machine learning\medical\medical_project\model\medical_disease_prediction_model.lb")
                    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST','GET'])
def predict():
    # Placeholder for prediction logic

    if request.method == 'POST':
        Age = int(request.form['Age'])
        BMI=float(request.form['BMI'])
        BloodPressure=float(request.form['BloodPressure'])
        GlucoseLevel=float(request.form['GlucoseLevel'])
        Cholesterol=float(request.form['Cholesterol'])
        HeartRate=float(request.form['HeartRate'])
        Smoking=int(request.form['Smoking'])
        FamilyHistory=int(request.form['FamilyHistory'])

        data=[[Age,BMI,BloodPressure,GlucoseLevel,Cholesterol,HeartRate,Smoking,FamilyHistory]]
        pred=model.predict(data)

        print("medical data :->>",data)

        pred=int(pred[0])

        pred_dict={
            0:"Diabetes", 1:"Healthy", 2:" Heart Disease ",3:"Hypertension",4:"Pre-Diabetes"
        }

        pred=pred_dict.get(int(pred))
    
        return render_template('result.html',prediction=pred)

if __name__=="__main__":
    app.run(debug=True)