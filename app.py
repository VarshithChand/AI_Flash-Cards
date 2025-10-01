import os
import json
import re
import random
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Get API key from environment variable for security
API_KEY = os.getenv("GOOGLE_API_KEY", "AIzaSyB3jaEj4MSB4BqwpkmYSD7grLIj7ED8d_s")

# Initialize the client with the API key
genai.configure(api_key=API_KEY)

# Configure generation settings for randomness
generation_config = genai.types.GenerationConfig(
    temperature=0.9,  # Higher temperature for more randomness (0.0-1.0)
    top_p=0.8,        # Nucleus sampling parameter
    top_k=40,         # Top-k sampling parameter
    max_output_tokens=2048,
)

model = genai.GenerativeModel('gemini-2.0-flash-exp')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_questions', methods=['POST'])
def get_questions():
    data = request.get_json()
    topic = data.get("topic", "general programming")

    # Add randomness to the prompt
    variation_phrases = [
        "Generate exactly 6 unique interview flashcards",
        "Create 6 diverse interview questions and answers",
        "Develop 6 varied interview flashcards",
        "Produce 6 different interview Q&A pairs",
        "Generate 6 distinct interview questions with answers"
    ]
    
    difficulty_levels = [
        "ranging from beginner to advanced level",
        "covering different aspects and complexity levels",
        "with varying difficulty from basic to expert",
        "including fundamental and advanced concepts",
        "spanning entry-level to senior-level topics"
    ]
    
    random_variation = random.choice(variation_phrases)
    random_difficulty = random.choice(difficulty_levels)
    random_seed = random.randint(1000, 9999)
    
    prompt = (
        f"{random_variation} on the topic '{topic}' {random_difficulty}. "
        f"Focus on practical, real-world scenarios and current best practices. "
        f"Session ID: {random_seed}. "
        "Return ONLY a valid JSON array with objects containing 'question' and 'answer' fields. "
        "Do not include any other text, explanations, or markdown formatting. "
        "Example format: [{{\"question\": \"What is...\", \"answer\": \"The answer is...\"}}]"
    )
    
    try:
        # Call the model with generation config for randomness
        response = model.generate_content(prompt, generation_config=generation_config)
        
        # Get the generated text
        generated_text = response.text.strip()
        
        # Print the raw response for debugging
        print("Raw response:", generated_text)
        
        # Try to extract JSON from the response
        # Sometimes the model wraps JSON in code blocks or adds extra text
        json_match = re.search(r'\[.*\]', generated_text, re.DOTALL)
        if json_match:
            json_text = json_match.group(0)
        else:
            json_text = generated_text
        
        # Parse the JSON output
        questions = json.loads(json_text)
        
        # Validate the structure
        if not isinstance(questions, list):
            raise ValueError("Response is not a list")
        
        # Ensure we have the right structure
        valid_questions = []
        for item in questions:
            if isinstance(item, dict) and 'question' in item and 'answer' in item:
                valid_questions.append({
                    'question': str(item['question']),
                    'answer': str(item['answer'])
                })
        
        if not valid_questions:
            raise ValueError("No valid questions found in response")
        
        return jsonify(valid_questions)
        
    except json.JSONDecodeError as e:
        print(f"JSON parsing error: {e}")
        return jsonify([{
            "question": "JSON Parsing Error", 
            "answer": f"The model returned invalid JSON. Raw response: {generated_text[:200]}..."
        }])
    except Exception as e:
        print(f"General error: {e}")
        return jsonify([{
            "question": "Generation Error", 
            "answer": f"Failed to generate questions: {str(e)}"
        }])

if __name__ == "__main__":
    app.run(debug=True) 