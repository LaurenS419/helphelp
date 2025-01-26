## Help Help
Interview practice web-app developed for McHacks 12

## Interview Practice

Finding internships is hard 😭 (as you know). So when you get the chance to have an interview, you better nail it 💪.

##What it does
We designed and built an interview practice web-app to help poor students like you practice and perfect their ~~yapping~~ interview skills. The interface auto-generates questions based on the type of interview you want to practice. Then, the user gets to face the weight of judgemental eyes as they answer a very high-stakes question, and when they're done, they get personalized feedback designed to help improve their interview skills. It contains a transcript of their answer, custom AI-generated feedback, calculated metrics, and eye-tracking information on their blink rate and eye contact.

##How we built it
The web-app is flask-based with a Python backend and a Python/JavaScript frontend. It uses a variety of AI models, from Whisper from Open AI to an eye-tracking model that gathers data on eye contact and blinking, along with some processing methods.

The eye-tracking model is composed of three main components.

1️⃣ **Step 1**: We begin by detecting important facial landmarks in real-time using MediaPipe's FaceMesh model.

2️⃣ **Step 2**: To determine if the interviewee is maintaining good eye contact, we use the head pose, which is estimated using the solvePnP algorithm. It takes in a predefined 3D facial model and corresponding 2D landmarks found in Step 1. Based on the head angle, it is easy to determine if the user is looking down, up, left, right, or forward.

3️⃣ **Step 3**: To detect the number of blinks, we implemented a gaze estimation function by calculating the Eye Aspect Ratio (EAR) for each eye and detecting blinks based on certain thresholds.

To generate helpful metrics for the user, we developed our own algorithms to calculate redundant words and stumbling. Repeated words like "like... hum... like" will be highlighted in yellow in the transcript. By leveraging natural language processing (NLP) techniques, our algorithms identify patterns in word choice, sentence structure, and conversational flow. These help users understand their performance, improve communication skills, and deliver more impactful responses during interviews. 

##Challenges

We are all backend people. The frontend does not agree with us. 

## What's Next?
There are a lot of exciting next steps!!
To expand, we'd like to implement a design that uses an uploaded resume to tailor the questions, since it would simulate a more realistic interview conversation. There is also a lot of other metrics we wanted to implement such as tracking smiles and other body language signals.


## Development

### Installing Node Dependencies

Make sure you have node & npm installed.

Then, run 
```
npm install
```
to install the necessary node depencies for the project from `package.json`.


### Installing Python Dependencies

Activate the projects virtual environment with
```
.venv\Scripts\activate
```
for Windows, or
```
source .venv/bin/activate
```
for MacOS/Linux.

Once activated, install/update the python packages with 
```
pip install -r requirements.txt
```

### Running the App

To run the app, go the root directory of the project, and run:
```
python app.py
```

For live TailwindCSS debugging, you should open another terminal and run:
```
npx @tailwindcss/cli -i ./static/style.css -o ./static/output.css --watch
```
