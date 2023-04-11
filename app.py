from flask import Flask , render_template,jsonify

app = Flask(__name__)

JOBS = [
    {
        'id':1,
        'title':'Data analyst',
        'location': 'Bengaluru,India',
        'salary': 'Rs 10,00,000',
          },

     {
        'id':2,
        'title':'Data scientist',
        'location': 'Delhi,India',
        'salary': 'Rs 10,00,000',
          },

        {
        'id':3,
        'title':'Frontend engineer',
        'location': 'remote',
        'salary': 'Rs 12,00,000',
          },

     {
        'id':4,
        'title':'Backend devloper',
        'location': 'Remote',
        'salary': 'Rs 12,00,000',
          },
]

@app.route("/")
def home():
    return render_template('home.html', jobs=JOBS, company_name="Jovian")


@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__== '__main__':
    app.run(host='0.0.0.0',debug=True)