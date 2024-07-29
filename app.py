from flask import Flask, request, jsonify, render_template_string
import random

app = Flask(__name__)

# Sample positive sentences
positive_samples = [
    "I absolutely love this product! It exceeded all my expectations.",
    "The customer service was outstanding and resolved my issue quickly.",
    "What a beautiful day! The sun is shining and the birds are singing.",
    "I'm thrilled with my new job, the team is amazing and supportive.",
    "The movie was fantastic, with great acting and an engaging plot.",
    "I'm grateful for all the wonderful friends in my life.",
    "This restaurant serves the most delicious food I've ever tasted.",
    "I'm so proud of my daughter's academic achievements this year.",
    "The vacation was perfect, with breathtaking views and relaxing moments.",
    "I'm feeling optimistic about the future and excited for new opportunities."
]

# Sample negative sentences
negative_samples = [
    "I'm extremely disappointed with the quality of this product.",
    "The customer support was terrible and didn't resolve my issue at all.",
    "What a horrible day! It's raining, and I forgot my umbrella.",
    "I'm stressed out about my job, the workload is overwhelming.",
    "The movie was awful, with poor acting and a confusing plot.",
    "I feel lonely and miss having close friends around.",
    "This restaurant serves the worst food I've ever had.",
    "I'm worried about my son's declining grades this semester.",
    "The vacation was a disaster, with delayed flights and lost luggage.",
    "I'm feeling pessimistic about the future and anxious about uncertainties."
]

# Encode the flag
encoded_flag = "QUlTUkctQ1RGe0FkdmVyc2FyaWFsU2VudGltZW50TWFzdGVyfQ=="

def decode_flag():
    return base64.b64decode(encoded_flag).decode('utf-8')

# Dummy sentiment analyzer (replace this with the Hugging Face model later)
def dummy_sentiment_analyzer(text):
    return {"label": "POSITIVE" if "good" in text.lower() else "NEGATIVE", "score": 0.9}

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sentiment Analysis Challenge</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f4f4f4;
        }
        h1, h2, h3 {
            color: #2c3e50;
        }
        #textInput {
            width: 100%;
            padding: 10px;
            margin-bottom: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        #submitBtn {
            background-color: #3498db;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 4px;
            cursor: pointer;
        }
        #submitBtn:hover {
            background-color: #2980b9;
        }
        #result {
            background-color: white;
            border: 1px solid #ddd;
            border-radius: 4px;
            padding: 20px;
            margin-top: 20px;
            white-space: pre-wrap;
        }
        .hidden {
            display: none;
        }
        .positive {
            color: green;
        }
        .negative {
            color: red;
        }
        #samples {
            margin-top: 30px;
            background-color: white;
            border: 1px solid #ddd;
            border-radius: 4px;
            padding: 20px;
        }
        #samples ul {
            padding-left: 20px;
        }
    </style>
</head>
<body>
    <h1>Sentiment Analysis Challenge</h1>
    <p>Enter a piece of text below and try to trick the sentiment analyzer. Can you create a positive-sounding sentence that the model classifies as negative?</p>
    <textarea id="textInput" rows="4" placeholder="Enter your text here..."></textarea>
    <button id="submitBtn">Analyze Sentiment</button>
    <div id="result" class="hidden"></div>
    
    <div id="samples">
        <h2>Sample Sentences:</h2>
        <h3>Positive:</h3>
        <ul id="positiveSamples"></ul>
        <h3>Negative:</h3>
        <ul id="negativeSamples"></ul>
    </div>

    <script>
        const textInput = document.getElementById('textInput');
        const submitBtn = document.getElementById('submitBtn');
        const result = document.getElementById('result');
        const positiveSamples = document.getElementById('positiveSamples');
        const negativeSamples = document.getElementById('negativeSamples');

        // Function to add sample sentences
        function addSamples(samples, element) {
            samples.forEach(sample => {
                const li = document.createElement('li');
                li.textContent = sample;
                element.appendChild(li);
            });
        }

        // Add sample sentences
        addSamples({{ positive_samples|tojson }}, positiveSamples);
        addSamples({{ negative_samples|tojson }}, negativeSamples);

        submitBtn.addEventListener('click', async () => {
            const text = textInput.value.trim();
            if (!text) {
                alert('Please enter some text.');
                return;
            }

            try {
                const response = await fetch('/analyze', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ text }),
                });

                const data = await response.json();
                result.innerHTML = `
                    <strong>Text:</strong> ${data.text}
                    <br><br>
                    <strong>Sentiment:</strong> <span class="${data.sentiment.toLowerCase()}">${data.sentiment}</span>
                    <br>
                    <strong>Score:</strong> ${data.score.toFixed(2)}
                    <br>
                    <strong>Is Adversarial:</strong> ${data.is_adversarial}
                    ${data.flag ? '<br><br><strong>Flag:</strong> ' + atob(data.flag) : ''}
                `;
                result.classList.remove('hidden');
            } catch (error) {
                console.error('Error:', error);
                result.textContent = 'An error occurred while analyzing the sentiment.';
                result.classList.remove('hidden');
            }
        });
    </script>
</body>
</html>
"""

@app.route('/', methods=['GET'])
def index():
    return render_template_string(HTML_TEMPLATE, 
                                  positive_samples=random.sample(positive_samples, 3),
                                  negative_samples=random.sample(negative_samples, 3))

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    data = request.json
    text = data.get('text', '')
    
    if not text:
        return jsonify({"error": "No text provided"}), 400
    
    # Perform sentiment analysis
    result = dummy_sentiment_analyzer(text)
    
    # Check if it's an adversarial example (positive text classified as negative)
    is_adversarial = result['label'] == 'NEGATIVE' and any(word in text.lower() for word in ['good', 'great', 'excellent', 'wonderful', 'amazing'])
    
    response = {
        "text": text,
        "sentiment": result['label'],
        "score": result['score'],
        "is_adversarial": is_adversarial
    }
    
    # Add the flag if it's a successful adversarial example
    if is_adversarial:
        response["flag"] = encoded_flag
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)