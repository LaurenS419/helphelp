from flask import Flask, render_template, request, jsonify
from pydub import AudioSegment
import os
import transcription
import analysis.transcription_processor
import analysis.word_counter
import analysis.chat_calls

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/interview", methods=["POST"])
def start_interview():
    return render_template("interview.html")

@app.route("/upload_audio", methods=["POST"])
def upload_audio():
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
    except Exception as e:
        return jsonify({"error": str(e)}), 500
        

    # Run the Python script (this can be a custom function or a separate script)
    result = run_python_script(output_path)

    return f"Processing complete", 200

# Function to run a Python script on the uploaded file
def run_python_script(file_path):

    data = {}
    question = "" ### GET REAL QUESTION SOMEHOW

    # get transcription
    t = transcription.get_trans(file_path)

    print(t)

    # clean up transition, turn into string of word tokens
    processed = analysis.transcription_processor.process(t)

    # get open ai chat gpt feedback on the response
    feedback = analysis.chat_calls.get_feedback(question, t)

    # calculated metrics 
    #counts = analysis.word_counter.count(processed)
    total_count = analysis.word_counter.total_count(processed)

    #print(counts)
    print(total_count)

    return data



if __name__ == "__main__":
    app.run(debug=True)
