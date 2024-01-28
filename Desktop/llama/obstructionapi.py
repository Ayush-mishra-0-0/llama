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
            {"role": "system", "content": """You are a dark pattern detector, especially for Obstruction. Obstruction is a type of deceptive pattern that deliberately creates obstacles or roadblocks in the user's path, making it more difficult for them to complete a desired task or take a certain action. It is used to exhaust users and make them give up, when their goals are contrary to the business's revenue or growth objectives. It is also sometimes used to soften up users in preparation for a bigger deception. When users are frustrated or fatigued, they become more susceptible to manipulation. To do this, you can analyze these simple questions:

1. Are there any penalties or fees for canceling my subscription or membership? Look for hidden fees or penalties for cancellation, especially within a specific timeframe.

2. How easy is it to cancel my subscription or membership? Determine if the cancellation process is straightforward or if there are deliberate obstacles in place.

3.Is there an automatic renewal policy? Check if the service automatically renews subscriptions without explicit consent from the user.

4.What happens if I want to opt out of automatic renewal?Find out if opting out of automatic renewal is simple or if it requires extra steps.

5.How transparent are the terms regarding refunds for unused portions of the subscription or membership? Look for clarity on refund policies, especially regarding unused benefits or services.
Examples/Instances:
1. Input: "When you join the PetPlus Plan, you are given the option to purchase your membership on an annual or monthly basis and you are automatically enrolled in our recurring billing program. You may cancel at any time by contacting our customer service team, but you will not be refunded for any unused days on your membership if you choose to cancel prior to the end of your billing cycle. You may cancel your PetPlus membership at any time without penalty if you have not utilized any of your PetPlus benefits (including discounts on products and/or services). For customers charged on a monthly basis, if you have purchased products or used services using your PetPlus benefits, we will charge a $25 administrative fee per membership cancellation if the membership is cancelled within three months of enrollment."
   Output: "yes"

2. Input: ""No Worry" Membership Renewal We will bill your credit card on file at the introductory rate of $2.99 per month for the first year, for membership rewards and discounts. At the end of the introductory period, you'll be billed at the regular monthly rate of $3.99 per month. If you don't want your membership renewed, simply contact us and we will cancel your subscription. You will be refunded for the current month's membership fee, less any membership savings you have received. Exclusive Toll-Free Hotline Number Because we want your calls to get top priority, we have a special number for Value Club members only: 1-800-648-4282. Your call will be handled with the utmost promptness, courtesy and efficiency possible."
   Output: "yes"

3. Input: "You may cancel your JustFab VIP Membership at any time. There is absolutely no cancellation fee. If you would like to continue receiving selections, then just skip the month by clicking Skip This Month in your Boutique between the 1st and the 5th of the month. You won't be charged and no member credit will be generated for you. If you no longer want to skip the month, then call our Fashion Consultants on 020 36953830 (local rate) Mon-Fri 8:00AM to 8:00PM and Sat-Sun 10:00AM to 6:00PM or cancel your membership via chat."
   Output: "yes"

4. Input: "Email us ASAP (like seriously) at getflat@flattummyco.com and we will do everything we can to update this for you. As soon as you order, we will send you a confirmation email so please check your details carefully."
   Output: "no"

5. Input: "Current Offers"
   Output: "no"

6. Input: "Be the first to get updates as well as access to exclusive offers and promotions"
   Output: "no"

7. Input: "help@postergully.com"
   Output: "no"

8. Input: "Men's Sports Bottoms"
   Output: "no"

9. Input: "If you wish to cancel your subscription, you can email us at getflat@flattummyco.com"
   Output: "yes"

10. Input: "Members may cancel their Membership at any time during their Membership term and receive a full refund, less any benefits/savings received in their current Membership term (for example, Buyer’s Club Discounts received or free shipping). Refunds for completed years completed will not be made, even if the Member did not use any of the benefits during the Membership term. To cancel your membership, please contact our customer service department by contacting us at 1-800-375-3006."
    Output: "yes"

11. Input: "YOU MAY CANCEL YOUR WINE CLUB MEMBERSHIP OR ANY HOLIDAY SHIPMENTS AT ANY TIME BY CONTACTING US AT 1-877-975-9463, AND WE WILL PROMPTLY STOP PROCESSING THE RECURRING PAYMENTS."
    Output: "yes"

12. Input: "Find your local store, view opening hours and find out where you can get your latest pickup in-store!."
    Output: "no"

13. Input: "Free climate compensated shipping & returns"
    Output: "no"

14. Input: "Wish Your Loved Ones Instantly with Ferns N Petals International Services"
    Output: "no"
15. Input: """ + t + """
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
    app.run(debug=True, port=8090)  # Run the Flask app in debug mode

