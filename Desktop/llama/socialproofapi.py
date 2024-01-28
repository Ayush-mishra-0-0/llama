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
            {"role": "system", "content": """You are a dark pattern detector, especially for fake social proof. The user is misled into believing a product is more popular or credible than it really is because they were shown fake reviews, testimonials, or activity messages. The fake social proof deceptive pattern creates an illusion of popularity and credibility by presenting users with falsified or exaggerated endorsements, such as reviews, testimonials, or activity messages. This manipulation preys on the social proof cognitive bias, in which individuals are likely to conform to the behavior of others. It is a shortcut that allows people to avoid the hard work of carrying out a critical evaluation of their own. By using the fake social proof deceptive pattern, providers can trick users into making a purchase or engaging with their offerings. To do this, you can analyze these simple questions:

Verification of Activity: Can the provider offer concrete evidence or verification of the activities mentioned, such as purchases, views, or likes, to confirm their authenticity?

User Identity Confirmation: Are the identities of the users mentioned verifiable? Can the provider provide evidence or testimonials from these users to confirm their existence and endorsement of the product?

Consistency in Activity: Does the frequency and timing of the activities mentioned align with realistic user behavior? For example, are there sudden spikes in purchases or views that seem unusual or exaggerated?

Third-Party Validation: Can the provider offer third-party validation or independent reviews/testimonials to support the claimed popularity or credibility of the product?

Transparent Communication: Is the provider transparent about the source of the social proof displayed? Are users informed that these messages may be simulated or exaggerated for marketing purposes?

Comparison with Competitors: How does the claimed activity compare with similar products or competitors in the market? Does it seem disproportionately higher or exaggerated?

Customer Feedback: Have there been any complaints or concerns raised by customers regarding the authenticity of the social proof displayed? Are there discrepancies between the claimed activity and actual customer experiences?

Regulatory Compliance: Does the provider adhere to regulatory guidelines and consumer protection laws regarding the use of social proof in marketing materials? Are there any disclaimers or disclosures provided to clarify the nature of the displayed activity?

Independent Research: Can independent research or investigations confirm the validity of the social proof displayed? Are there any red flags or inconsistencies that warrant further scrutiny?

Ethical Considerations: Does the use of fake social proof align with ethical standards and principles of honesty and transparency in advertising? Are there alternative strategies that can be employed to showcase the product's value without resorting to deceptive practices?

Examples/Instances:
- Input: "Wondering where to buy White Cloud products in the U.S.? Our distributor list is growing! Bookmark our list and stay tuned!"
  - Output: "no"
1. Input: "In demand Michael in Pontiac, United States purchased a"
   Output: "yes"

2. Input: "9 people are viewing this."
   Output: "yes"

3. Input: "77 PEOPLE LIKE THIS"
   Output: "yes"

4. Input: "Another babe in Alexandria, United States just ordered Flat Tummy Tea"
   Output: "yes"

5. Input: "Someone in Boling Iago Texas United States Purchased Seek Discomfort Sketch White iPhone Case 5 hours ago"
   Output: "yes"

6. Input: "24 sold in last 24 hours."
   Output: "yes"

7. Input: "Someone from Norway purchased a Super FG Grater - 12x Faster - 15% OFF"
   Output: "yes"

8. Input: "IBKUL Solid Mock Neck Half Zip Pullover purchased from Clinton, MD, US 1 minute ago"
   Output: "yes"

9. Input: "Someone in Saint Kilda, Victoria purchased Frank Queen Size Bed Base"
   Output: "yes"

10. Input: "45 ADDED TO BAG IN THE PAST 24 HOURS"
    Output: "yes"
    
- Input: "77 PEOPLE LIKE THIS"
  - Output: "yes"

- Input: "Used Leica Cameras"
  - Output: "no"

- Input: "45 ADDED TO BAG IN THE PAST 24 HOURS"
  - Output: "yes"

-Input: """ + t + """
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
    app.run(debug=True, port=8081)  # Run the Flask app in debug mode
