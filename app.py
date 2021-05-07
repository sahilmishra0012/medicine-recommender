from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import json
import predict
app = Flask(__name__)
cors = CORS(app)

@app.route('/result', methods=['POST'])
def result():
    book_name = json.loads(request.get_data())['data']['complaints']
    predictions = predict.predict(book_name)
    print(predictions)
    return {"predictions":predictions[0]}


if __name__ == "__main__":
    app.run(port=8080)