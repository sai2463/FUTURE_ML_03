from flask import Flask, render_template, request

app = Flask(__name__)

# Simple rule-based chatbot
faq = {
    "refund": "To request a refund, please contact support@company.com.",
    "cancel": "You can cancel an order by visiting your account > orders > cancel.",
    "late": "We apologize for the delay. Please provide your order ID.",
    "damage": "If your item is damaged, reach out to support with pictures attached.",
    "billing": "For billing issues, verify your payment method under account settings."
}

def chatbot_response(user_input):
    user_input = user_input.lower()
    for keyword in faq:
        if keyword in user_input:
            return faq[keyword]
    return "Sorry, I didn't quite understand. Could you rephrase?"

@app.route("/", methods=["GET", "POST"])
def chat():
    user_input = ""
    bot_reply = ""
    if request.method == "POST":
        user_input = request.form["user_input"]
        bot_reply = chatbot_response(user_input)
    return render_template("chat.html", user_input=user_input, bot_reply=bot_reply)

if __name__ == "__main__":
    print("✅ Chatbot Flask app is running!")
    app.run(debug=True)
