from flask import Flask, jsonify, request
from openai import OpenAI

app = Flask(__name__)

def detect_dark_pattern(t):
    # Initialize OpenAI client
    client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

    # Loop for interaction
    completion = client.chat.completions.create(
        model="local-model",  # this field is currently unused
        messages=[
            {"role": "system", "content": """You are a dark pattern detector, especially for Forced action. The user wants to do something, but they are required to do something else undesirable in return. To do this, you will analyze these simple questions:

1. Is the desired action clearly presented as mandatory, without offering a clear alternative? Look for phrases like "I agree" or "I accept" that imply consent without providing an obvious opt-out option.

2. Are multiple agreements or actions bundled together without clear separation? Check if there are multiple requests or consent forms presented as a single action, making it difficult for users to selectively opt out.

3. Does the wording or presentation of the action attempt to obscure or downplay its significance? Look for instances where the language used minimizes the impact of the action or uses ambiguous terms that may confuse users about what they're agreeing to.

4. Is there a clear option to decline or opt out? Look for a visible "No thanks" or "I decline" button alongside the action being presented.

Examples/Instances:
1. Input: "I would like to join Backstage Pass & agree to the Terms & Conditions & to receive emails & other promotional offers."
   Output: "yes"

2. Input: "No thanks. I don't like free things..."
   Output: "no"

3. Input: "HURRY, LOW IN STOCK!"
   Output: "no"

4. Input: "I agree to receive marketing emails from Natural Life and agree to our Privacy Policy and terms of use."
   Output: "yes"

5. Input: "Pillowcases & Shams (1)"
   Output: "no"

6. Input: "Newsletter Signup (Privacy Policy) (2)"
   Output: "no"

7. Input: """ + t + """
            Output: [Please provide expected output here in yes or no]
            """},  
            {"role": "user", "content": t}
        ],
        temperature=0.7,
        max_tokens=1
    )

    # Output response
    return completion.choices[0].message.content

# Define a route for your API endpoint
@app.route('/api/hello', methods=['POST'])
def hello():
    data = request.json
    input_string = data.get('input_string')
    j = detect_dark_pattern(input_string)
    return jsonify({'message': j})

if __name__ == '__main__':
    app.run(debug=True, port=8888)  # Run the Flask app in debug mode

