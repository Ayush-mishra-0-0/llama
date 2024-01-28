'''from flask import Flask, jsonify

app = Flask(__name__)




from openai import OpenAI

def detect_dark_pattern():
    # Initialize OpenAI client
    client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

    # Loop for interaction
        # User input
        #t = input("Enter the text: ")
         t= "only 3 left"
        # Chat completion
        completion = client.chat.completions.create(
            model="local-model",  # this field is currently unused
            messages=[
                {"role": "system", "content": """You are a dark pattern detector, especially for  Scarcity. Signal the limited availability or high demand of a product, thus increasing its perceived value and desirability.Fake scarcity works by creating an artificial sense of limited availability around a product or service, pushing users to act quickly out of fear of missing out. This is achieved by displaying misleading messages about low stock levels or high demand. By tapping into the scarcity cognitive bias, this deceptive pattern preys on users' natural tendency to assign more value to items that appear rare or exclusive, pushing them into making hasty purchasing decisions without fully evaluating their options. To do this, you can analyze these simple questions:
Stock Accuracy:

How accurate is the displayed stock information?
Can the stock levels be independently verified?
Are there any consequences for falsely claiming limited stock?
Purchase Pressure:

Are there tactics employed to rush the user into making a purchase decision?
How is urgency conveyed to the user?
Are there time limits or countdowns associated with product availability?
Pattern Consistency:

Do messages about limited availability appear consistently or frequently across products?
Is there a noticeable pattern in how stock levels are portrayed?
Actual Demand vs. Displayed Demand:

Can the displayed demand for a product be independently verified?
How does the displayed demand compare to actual demand for the product?
Behavioral Impact:

Have there been any studies or analyses on how these scarcity tactics influence user behavior?
Are there any user complaints or feedback related to feeling pressured to make quick purchasing decisions?
Transparency and Disclosure:

Is there clear disclosure about the methodology behind displaying stock levels and demand?
Are users informed about the potential use of scarcity tactics?
Alternative Options:

Are users presented with alternative products or options if the desired item appears to be low in stock?
How does the platform handle scenarios where a product becomes out of stock?
Regulatory Compliance:

Does the platform adhere to any regulations or guidelines regarding transparency in advertising and sales practices?
Are there any legal considerations regarding the use of fake scarcity tactics?

Examples/Instances:
Input: "Jeanne E. Bray Memorial Scholarship"
Output: "no"

Input: "Only 3 items left"
Output: "yes"

Input: "In demand"
Output: "yes"

Input: "Light powerful."
Output: "no"

Input: "Summer Simple Breathable Socks"
Output: "no"

Input: "Low Stock Alert: Only 8 left in inventory"
Output: "yes"

Input: "OH SHIP! Looks like that page wasn't found"
Output: "no"

Input: "Cropped Jeans"
Output: "no"

Input: "iPhones"
Output: "no"

Input: "Limited Availability"
Output: "yes"

Input: "ONLY 3 LEFT"
Output: "yes"

Input: "Hurry! Only 2 left"
Output: "yes"

Input: "Exotic Bird Food"
Output: "no"

Input: "In Stock only 3 left"
Output: "yes"

Input: "In demand"
Output: "no"

Input: "The site was easy to navigate. I haven't received my shoes yet, but overall a good experience."
Output: "no"

Input: "Scarves & Snoods"
Output: "no"

Input: "Mountboard"
Output: "no"

Input: "Value of Product"
Output: "no"

Input: "Graduations"
Output: "no"

Input: "894 Claimed! Hurry, only a few left!"
Output: "yes"

Input: "Either because we're updating the site or because someone spilled coffee on it again. We'll be back just as soon as we finish the update or clean up the coffee."
Output: "no"

Input: "Boardshorts"
Output: "no"

Input: "4 items left"
Output: "yes"

Input: "Arthritis Aids"
Output: "no"

Input: "Hurry! Only 2 left in stock"
Output: "yes"

Input: "Cheaney"
Output: "no"

Input: "Only 7 left in stock."
Output: "yes"

Input: "87% offers claimed. Hurry up!"
Output: "yes"

Input: "≡ Filter Reviews Clicking on the following button will update the content below"
Output: "no"

Input: "1 in Stock"
Output: "yes"

Input: """+t+"""
   Output: [Please provide expected output here in yes or no]
"""},  # Insert the long text here
                {"role": "user", "content": t}
            ],
            temperature=0.7,
            max_tokens=1
        )

        # Output response
        return((completion.choices[0].message.content))

# Call the function to start detection
j=(detect_dark_pattern())






# Define a route for your API endpoint
@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({'message': j})

# Define other routes as needed for your API

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app in debug mode
'''
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
            {"role": "system", "content": """You are a dark pattern detector, especially for  Scarcity. Signal the limited availability or high demand of a product, thus increasing its perceived value and desirability.Fake scarcity works by creating an artificial sense of limited availability around a product or service, pushing users to act quickly out of fear of missing out. This is achieved by displaying misleading messages about low stock levels or high demand. By tapping into the scarcity cognitive bias, this deceptive pattern preys on users' natural tendency to assign more value to items that appear rare or exclusive, pushing them into making hasty purchasing decisions without fully evaluating their options. To do this, you can analyze these simple questions:
            Stock Accuracy:

            How accurate is the displayed stock information?
            Can the stock levels be independently verified?
            Are there any consequences for falsely claiming limited stock?
            Purchase Pressure:

            Are there tactics employed to rush the user into making a purchase decision?
            How is urgency conveyed to the user?
            Are there time limits or countdowns associated with product availability?
            Pattern Consistency:

            Do messages about limited availability appear consistently or frequently across products?
            Is there a noticeable pattern in how stock levels are portrayed?
            Actual Demand vs. Displayed Demand:

            Can the displayed demand for a product be independently verified?
            How does the displayed demand compare to actual demand for the product?
            Behavioral Impact:

            Have there been any studies or analyses on how these scarcity tactics influence user behavior?
            Are there any user complaints or feedback related to feeling pressured to make quick purchasing decisions?
            Transparency and Disclosure:

            Is there clear disclosure about the methodology behind displaying stock levels and demand?
            Are users informed about the potential use of scarcity tactics?
            Alternative Options:

            Are users presented with alternative products or options if the desired item appears to be low in stock?
            How does the platform handle scenarios where a product becomes out of stock?
            Regulatory Compliance:

            Does the platform adhere to any regulations or guidelines regarding transparency in advertising and sales practices?
            Are there any legal considerations regarding the use of fake scarcity tactics?

            Examples/Instances:
            Input: "Jeanne E. Bray Memorial Scholarship"
            Output: "no"

            Input: "Only 3 items left"
            Output: "yes"

            Input: "In demand"
            Output: "yes"

            Input: "Light powerful."
            Output: "no"

            Input: "Summer Simple Breathable Socks"
            Output: "no"

            Input: "Low Stock Alert: Only 8 left in inventory"
            Output: "yes"

            Input: "OH SHIP! Looks like that page wasn't found"
            Output: "no"

            Input: "Cropped Jeans"
            Output: "no"

            Input: "iPhones"
            Output: "no"

            Input: "Limited Availability"
            Output: "yes"

            Input: "ONLY 3 LEFT"
            Output: "yes"

            Input: "Hurry! Only 2 left"
            Output: "yes"

            Input: "Exotic Bird Food"
            Output: "no"

            Input: "In Stock only 3 left"
            Output: "yes"

            Input: "In demand"
            Output: "no"

            Input: "The site was easy to navigate. I haven't received my shoes yet, but overall a good experience."
            Output: "no"

            Input: "Scarves & Snoods"
            Output: "no"

            Input: "Mountboard"
            Output: "no"

            Input: "Value of Product"
            Output: "no"

            Input: "Graduations"
            Output: "no"

            Input: "894 Claimed! Hurry, only a few left!"
            Output: "yes"

            Input: "Either because we're updating the site or because someone spilled coffee on it again. We'll be back just as soon as we finish the update or clean up the coffee."
            Output: "no"

            Input: "Boardshorts"
            Output: "no"

            Input: "4 items left"
            Output: "yes"

            Input: "Arthritis Aids"
            Output: "no"

            Input: "Hurry! Only 2 left in stock"
            Output: "yes"

            Input: "Cheaney"
            Output: "no"

            Input: "Only 7 left in stock."
            Output: "yes"

            Input: "87% offers claimed. Hurry up!"
            Output: "yes"

            Input: "≡ Filter Reviews Clicking on the following button will update the content below"
            Output: "no"

            Input: "1 in Stock"
            Output: "yes"

            Input: """ + t + """
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
    app.run(debug=True, port=8080)  # Run the Flask app in debug mode
