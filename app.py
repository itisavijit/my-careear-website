from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'tittle': 'Data Analyst',
  'location': 'Bang,Ind',
  'salary': 'Rs. 15,00,00'
}, {
  'id': 2,
  'tittle': 'Software Engineer',
  'location': 'Bang,Ind',
  'salary': 'Rs. 10,00,00'
}, {
  'id': 3,
  'tittle': 'Data Engineer',
  'location': 'Bang,Ind'
}]


@app.route("/")
def hello_my_careear():
  return render_template('home.html', jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
