from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import logging
import json
import os

# Set up logging to debug issues
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for frontend requests

# File to log unmatched questions
UNMATCHED_QUESTIONS_FILE = "unmatched_questions.json"

# Initialize unmatched questions file if it doesn't exist
if not os.path.exists(UNMATCHED_QUESTIONS_FILE):
    with open(UNMATCHED_QUESTIONS_FILE, 'w') as f:
        json.dump([], f)

# Predefined responses based on Vipul Singh's resume
responses = {
    "what should we know about your life story": "I’m Vipul Singh, a Data Analyst and Data Scientist from Delhi with a B.Tech in Information Technology from CSJM University, Kanpur, completed in 2024. I’ve worked at NS Matrix and as an ML intern at Externclub IIT K, where I turned large datasets into actionable insights using Python, SQL, and machine learning. I’m passionate about coding, problem-solving, and driving data-driven decisions, and I’m eager to contribute to Home.LLC.",
    "what’s your number one superpower": "My #1 superpower is analyzing complex datasets to uncover insights—like reducing data processing time by 20% at NS Matrix or building a fraud detection model with 97% accuracy during my internship.",
    "what are the top three areas you’d like to grow in": "I want to grow in advanced machine learning with tools like TensorFlow, leadership to manage data teams, and data storytelling with Tableau and Power BI to make insights more impactful.",
    "what misconception do your coworkers have about you": "Some might think I’m only about data because of my technical focus, but I’m also a team player who enjoys collaborating—like when I fine-tuned fraud detection algorithms with my team at Externclub IIT K.",
    "how do you push your boundaries and limits": "I push myself by tackling tough challenges, like building a sales forecast model from scratch or competing in ICPC regionals. I also honed my skills to rank in the top 6% on LeetCode globally."
}

# Function to log unmatched questions
def log_unmatched_question(question):
    with open(UNMATCHED_QUESTIONS_FILE, 'r') as f:
        unmatched_questions = json.load(f)
    unmatched_questions.append(question)
    with open(UNMATCHED_QUESTIONS_FILE, 'w') as f:
        json.dump(unmatched_questions, f, indent=4)
    logger.info(f"Logged unmatched question: {question}")

# Function to get response with enhanced local fallback
def get_response(question):
    logger.debug(f"Received question: {question}")
    question = question.lower()

    # Check for predefined responses
    for key in responses:
        if key in question:
            logger.debug(f"Matched predefined response for: {key}")
            return responses[key]

    # Enhanced local fallback for a wide range of questions
    logger.debug("No predefined response found, using enhanced local fallback")

    # Handle appreciation or compliments
    if any(word in question for word in ["good", "great", "nice", "well done", "awesome", "amazing", "excellent", "fantastic", "impressive", "brilliant"]):
        return "Thank you! I really appreciate your kind words."

    # Questions about experience
    if "experience" in question or "work" in question or "job" in question or "internship" in question:
        return "I have experience as a Data Analyst at NS Matrix from March 2024 to December 2024, where I reduced data processing time by 20%. I also worked as an ML intern at Externclub IIT K from March 2023 to May 2023, where I fine-tuned fraud detection algorithms and built a model with 97% accuracy."

    # Questions about skills
    if "skill" in question or "what can you do" in question or "what are you good at" in question:
        return "I’m skilled in Python, R, SQL, Java, Pandas, NumPy, TensorFlow, Scikit-learn, Power BI, and Tableau. I use these tools to analyze data, build machine learning models, and create insightful dashboards."

    # Questions about projects
    if "project" in question or "what have you worked on" in question or "what did you build" in question:
        return "I’ve worked on a Fraud Detection System with 95% accuracy using machine learning, and an E-Commerce Sales Forecast dashboard using Power BI. At NS Matrix, I optimized data processing, and at Externclub IIT K, I contributed to fraud detection algorithms."

    # Questions about education
    if "education" in question or "where did you study" in question or "degree" in question:
        return "I have a B.Tech in Information Technology from CSJM University, Kanpur, completed in 2024."

    # Questions about achievements
    if "achievement" in question or "what are you proud of" in question or "accomplishment" in question:
        return "I’m proud of being a 5-star coder on HackerRank, ranking in the top 6% on LeetCode, and competing in ICPC regionals."

    # Questions about hobbies or interests
    if "hobby" in question or "what do you like to do" in question or "interest" in question or "free time" in question:
        return "I enjoy coding, problem-solving, and exploring new data analysis techniques. I also like to challenge myself with competitive programming."

    # Questions about location
    if "where are you from" in question or "location" in question or "where do you live" in question:
        return "I’m from Delhi, India."

    # Questions about goals or aspirations
    if "goal" in question or "aspire" in question or "future" in question or "where do you see yourself" in question:
        return "My goal is to become a leading data scientist, leveraging advanced machine learning to solve real-world problems and drive impactful decisions at companies like Home.LLC."

    # Questions about personal details
    if "how old are you" in question or "age" in question or "when were you born" in question:
        return "I’m 22 years old, born in 2002."  # Placeholder, please update with your actual age

    if "family" in question or "parents" in question or "siblings" in question:
        return "I come from a supportive family in Delhi. I have a younger sibling who’s also interested in technology."  # Placeholder, please update

    if "language" in question or "what languages do you speak" in question:
        return "I speak English and Hindi fluently."  # Placeholder, please update

    # Questions about preferences
    if "favorite programming language" in question or "favorite technology" in question:
        return "My favorite programming language is Python because of its versatility in data analysis and machine learning."  # Placeholder, please update

    if "favorite project" in question:
        return "My favorite project is the Fraud Detection System I built, as it had a real impact with 95% accuracy."  # Placeholder, please update

    if "favorite book" in question:
        return "I enjoy reading 'The Alchemist' by Paulo Coelho—it’s inspiring and thought-provoking."  # Placeholder, please update

    if "favorite movie" in question:
        return "My favorite movie is 'Inception'—I love its complex storytelling."  # Placeholder, please update

    if "favorite food" in question:
        return "I love Indian cuisine, especially butter chicken with naan."  # Placeholder, please update

    # Questions about challenges
    if "challenge" in question or "difficult" in question or "struggle" in question:
        return "One challenge I faced was optimizing a large dataset at NS Matrix. I overcame it by implementing efficient data processing techniques, reducing processing time by 20%."

    if "recently learned" in question or "last thing you learned" in question:
        return "I recently learned about advanced feature engineering techniques in machine learning to improve model performance."  # Placeholder, please update

    # Questions about personality and values
    if "describe yourself" in question or "what are you like" in question:
        return "I’d describe myself as analytical, curious, and collaborative. I love solving problems and working with teams to achieve goals."  # Placeholder, please update

    if "motivate" in question or "what drives you" in question:
        return "I’m motivated by the opportunity to solve real-world problems with data and make a meaningful impact."  # Placeholder, please update

    if "principle" in question or "value" in question or "belief" in question:
        return "I believe in continuous learning and always striving to improve, both personally and professionally."  # Placeholder, please update

    # Questions about Home.LLC or the role
    if "why home.llc" in question or "why this company" in question:
        return "I’m excited about Home.LLC because of its innovative approach to leveraging data for real estate solutions. I believe my data analysis and machine learning skills can contribute to the company’s growth."

    if "why should we hire you" in question or "why you" in question:
        return "You should hire me because I bring a strong background in data analysis and machine learning, with proven results like reducing data processing time by 20% at NS Matrix and building a fraud detection model with 97% accuracy. I’m passionate, collaborative, and eager to contribute to Home.LLC’s success."

    # Generic fallback for all other questions
    log_unmatched_question(question)
    return "I’m not sure how to answer that, but I’m Vipul Singh, a Data Analyst with experience in data science and machine learning. I’ve worked at NS Matrix and Externclub IIT K, and I’m skilled in Python, SQL, and Tableau. Can you ask something about my experience, skills, or projects?"

# Flask routes
@app.route("/")
def index():
    logger.debug("Serving index.html")
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    try:
        data = request.get_json()
        logger.debug(f"Received data: {data}")
        question = data.get("question", "")
        if not question:
            logger.warning("No question provided in request")
            return jsonify({"error": "No question provided"}), 400
        response = get_response(question)
        return jsonify({"question": question, "response": response})
    except Exception as e:
        logger.error(f"Error in /ask endpoint: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
