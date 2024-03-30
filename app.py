from flask import Flask, render_template, request

app = Flask(__name__)

hospitals = []

@app.route('/')
def index():
    return render_template('index.html', hospitals=hospitals)

@app.route('/add_doctor', methods=['GET', 'POST'])
def add_doctor():
    if request.method == 'POST':
        # Process form submission
        hospital = request.form['hospital']
        doctor_name = request.form['doctor_name']
        specialty = request.form['specialty']
        # You can process the data further (e.g., add to a database)
        return 'Doctor added successfully!'
    else:
        return render_template('add_doctor.html', hospitals=hospitals)

@app.route('/add_patient', methods=['GET', 'POST'])
def add_patient():
    if request.method == 'POST':
        # Process form submission
        hospital = request.form['hospital']
        patient_name = request.form['patient_name']
        patient_age = request.form['patient_age']
        patient_issue = request.form['patient_issue']
        # You can process the data further (e.g., add to a database)
        return 'Patient added successfully!'
    else:
        return render_template('add_patient.html', hospitals=hospitals)

@app.route('/add_prescription', methods=['GET', 'POST'])
def add_prescription():
    if request.method == 'POST':
        # Process form submission

        patient_id = request.form['patient_id']
        doctor_name = request.form['doctor_name']
        prescription = request.form['prescription']
        # You can process the data further (e.g., add to a database)
        return 'Prescription added successfully!'
    else:
        return render_template('add_prescription.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
