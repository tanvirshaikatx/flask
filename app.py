from flask import Flask, render_template, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Set up Google API key
genai.configure(api_key="AIzaSyD6_jpVAUib4QLbt49UHZBnyZGhrno-6rY")

def generate_quote():
    try:
        # Initialize the GenerativeModel
        model = genai.GenerativeModel("gemini-1.5-flash")
        
        # Generate content
        response = model.generate_content("Provide a motivational quote with the author name, change every time, don't repeat the same quote")
        
        # Return the generated text
        return response.text.strip()
    except Exception as e:
        return f"Error generating quote: {e}"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/get-quote', methods=['GET'])
def get_quote():
    quote = generate_quote()
    return jsonify({"quote": quote})

if __name__ == '__main__':
    app.run(debug=True)





# chat with ai
'''from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Set up Google API key
genai.configure(api_key="AIzaSyD6_jpVAUib4QLbt49UHZBnyZGhrno-6rY")

def generate_answer(question):
    try:
        # Initialize the GenerativeModel
        model = genai.GenerativeModel("gemini-1.5-flash")
        
        # Generate a response based on the user's question
        response = model.generate_content(question)
        
        # Return the generated text
        return response.text.strip()
    except Exception as e:
        return f"Error generating answer: {e}"

@app.route('/')
def home():
    return render_template('chat.html')

@app.route('/ask-question', methods=['POST'])
def ask_question():
    data = request.json
    question = data.get('question', '')
    if not question:
        return jsonify({"answer": "Please ask a valid question!"})
    
    # Generate the answer
    answer = generate_answer(question)
    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(debug=True)
'''