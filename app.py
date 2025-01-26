from flask import Flask, render_template, request, jsonify
from pydub import AudioSegment
import os
import CV.eye_contact
import transcription

import CV.main
import analysis.transcription_processor
import analysis.word_counter
import analysis.chat_calls
import analysis.word_density
import analysis.word_per_min
import random
import json

app = Flask(__name__)

QUESTION = ""

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():
        
    return render_template("index.html")

@app.route("/interview", methods=["POST"])
def start_interview():
    global QUESTION
    # get the question selection from main
    question_type = request.form['question-type']

    with open('questions.json') as f:
        data = json.load(f)
        index = random.randrange(0, len(data[question_type]))
        QUESTION = data[question_type][index]

    return render_template("interview.html", question=QUESTION)

@app.route("/start_record", methods=["POST"])
def start_recording():
    CV.main.start_record()  
    return jsonify({"status": "Recording started"})

@app.route("/stop_record", methods=["POST"])
def stop_recording():
    CV.main.stop_record()  
    blink_rate, eye_contact_percentage = CV.eye_contact.results('logs/eye_log.csv') # \ for windows?
    return jsonify({"status": "Recording stopped",
                    "blink_rate": blink_rate,
                    "eye_contact_percentage": eye_contact_percentage
    })

@app.route("/upload_audio", methods=["POST"])
def upload_audio():
    global QUESTION
    if "audio" not in request.files:
        return jsonify({"error": "No audio file uploaded"}), 400

    audio_file = request.files["audio"]
    input_path = os.path.join(UPLOAD_FOLDER, "recording.webm")
    output_path = os.path.join(UPLOAD_FOLDER, "recording.mp3")

    # Save the uploaded file
    audio_file.save(input_path)

    # Convert WebM to MP3 using pydub
    
    try:
        audio = AudioSegment.from_file(input_path, format="webm")
        audio.export(output_path, format="mp3")
        #return jsonify({"message": "Audio uploaded and converted successfully!"}), 200
        data = run_python_script(output_path)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
        
    return render_template("summary.html", question=QUESTION, data=data)





# Function to run a Python script on the uploaded file
def run_python_script(file_path):

    data = {}

    # get transcription
    t = transcription.get_trans(file_path)

    print(t)

    # clean up transition, turn into string of word tokens
    processed = analysis.transcription_processor.process(t)

    print(processed)

    # get open ai chat gpt feedback on the response
    feedback = analysis.chat_calls.get_feedback(QUESTION, t)

    # calculated metrics 
    total_count = analysis.word_counter.total_count(processed)
    dense_words = analysis.word_density.find_dense(processed) # indices of dense words
    wpm = round(analysis.word_per_min.get_wpm(len(processed), file_path), 2)

    data['transcription'] = t
    data['feedback'] = feedback
    data['total_count'] = total_count
    data['dense_words'] = dense_words
    data['wpm'] = wpm

    return data



if __name__ == "__main__":
    app.run(debug=True)
