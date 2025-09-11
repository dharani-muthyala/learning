from flask import Flask, request, jsonify
from flask_cors import CORS
import boto3
import json

app = Flask(__name__)

CORS(app, resources={r"/prompt": {"origins": "http://localhost:3000"}})

bedrock = boto3.client("bedrock-runtime")

@app.route('/prompt', methods=['POST'])
def prompt():
    data = request.get_json()
    prompt = data.get("prompt")

    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

   
    

    request_body = json.dumps({
        "inputText": prompt
    })

    try:
        response = bedrock.invoke_model(
            modelId="amazon.titan-text-express-v1",  
            body=request_body,
            contentType="application/json"
        )

        model_output = json.loads(response['body'].read())
        completion = model_output["results"][0]["outputText"]

        return jsonify({
            "prompt": prompt,
            "prompt_response": completion
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500
 
if __name__ == '__main__':
    app.run(debug=True, port=5000)
