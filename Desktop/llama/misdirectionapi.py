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
            {"role": "system", "content": """You are a dark pattern detector, especially for  Misdirection. Misdirection in the context of user experience design refers to intentionally steering users toward or away from making a particular choice through deceptive or manipulative tactics. To do this, you can analyze these simple questions:

1. Is the choice being presented clear and transparent? Look for instances where choices are obfuscated or hidden within the design, making it difficult for users to understand the implications of their actions.

2. Are there any elements designed to create a sense of urgency or scarcity? Identify any messages or visual cues that pressure users into making a quick decision without fully considering their options.

Examples/Instances:
1. Input: "No thanks. I don't like free things..."
   Output: "yes"
   
2. Input: "I don't feel lucky"
   Output: "yes"
   
3. Input: "I don't want to save money"
   Output: "yes"

4. Input: "No, I'll rather pay full price."
   Output: "yes"
5. Input: " Books About Indian Culture "
   Output: "no"
6. Input: "Game Extraction & Prep"
   Output: "no"
7. Input: "Find your local store, view opening hours and find out where you can get your latest pickup in-store!."
   Output: "no"
8. Input: "Free climate compensated shipping & returns"
   Output: "no"
9. Input: "Wish Your Loved Ones Instantly with Ferns N Petals International Services"
   Output: "no"
10. Input:  """ + t + """
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
    app.run(debug=True, port=5001)  # Run the Flask app in debug mode
