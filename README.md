# mchacks12
Interview practice web-app developed for McHacks 12

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