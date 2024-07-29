# Sentiment Analysis Challenge - CTF

## About This CTF 

This Capture The Flag (CTF) challenge focuses on adversarial machine learning in the context of sentiment analysis. Participants are tasked with creating "adversarial examples" - inputs designed to fool a sentiment analysis model. The goal is to craft a sentence that appears positive to human readers but is classified as negative by the machine learning model.

This challenge aims to:
1. Demonstrate the vulnerability of machine learning models to carefully crafted inputs
2. Encourage creative thinking about AI security
3. Provide hands-on experience with adversarial machine learning concepts

## Screenshot:
<img width="873" alt="Screenshot 2024-07-29 at 3 27 12 PM" src="https://github.com/user-attachments/assets/d9c6c230-a043-404d-9e90-fd1f24d5a8ca">

### Solution:
<img width="873" alt="Screenshot 2024-07-29 at 3 27 53 PM" src="https://github.com/user-attachments/assets/2314e9ac-4d44-4434-b9d9-161ff6e67d2b">

## Installation

To set up this CTF challenge on your local machine, follow these steps:

1. Clone this repository:
   ```
   git clone https://github.com/AI-Security-Research-Group/Adversarial-Examples-CTF.git
   cd Adversarial-Examples-CTF
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install flask
   ```

4. Run the application:
   ```
   python app.py
   ```

5. Open a web browser and navigate to `http://localhost:5000`

## How to Play

1. Once you've accessed the web interface, you'll see a text input area and some sample positive and negative sentences.

2. Your challenge is to create a sentence that sounds positive but is classified as negative by the model.

3. Enter your crafted sentence into the text area and click "Analyze Sentiment".

4. If your sentence successfully fools the model (i.e., it sounds positive but is classified as negative), you'll see the flag appear in the results.

5. Keep trying different approaches until you successfully retrieve the flag!

## Flag Format

The flag for this challenge will be in the following format:

```
AISRG-CTF{...}
```

Where `...` will be replaced with a specific string when you successfully complete the challenge.

## Follow for More CTFs

If you enjoyed this challenge and want to stay updated on more CTFs and security challenges:

- Follow us on GitHub: [AISRG](https://github.com/AI-Security-Research-Group)

We regularly release new challenges and host live CTF events. Don't miss out on the opportunity to further develop your skills in AI security.

Happy hacking! 🥷
