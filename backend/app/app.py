import flask
import joblib
import numpy as np

app = flask.Flask(__name__)
model = None

@app.route('/')
def load_model():
    global model
    print(" * Loading pre-trained model ...")
    model = joblib.load("./trained-model/sample-model.pkl")
    print(' * Loading end')

@app.route('/predict', methods=['POST'])
def predict():
    response = {
        "success": False,
        "Content-Type": "application/json"
    }
    if flask.request.method == "POST":
        if flask.request.get_json().get("feature"):
            feature = flask.request.get_json().get("feature")

            feature = np.array(feature).reshape((1, -1))

            response["prediction"] = model.predict(feature).tolist()

            response["success"] = True
    return flask.jsonify(response)

if __name__ == '__main__':
    load_model()
    print(" * Flask starting server...")
    app.run()
    # app.run(host='0.0.0.0', port=5000)
