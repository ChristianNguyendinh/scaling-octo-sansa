### search for your favorite celeb xD ###

REQ: python3, pip, npm

SETUP:
pip install -r requirements.txt
npm install

START:
python manager.py runserver

FOR DEV:
runserver in background,
npm run build       (watches for changes and recompiles)

----------------------------------------------------------

TODO:
- facebook page search uses user api key, that is annoying. Find another source for profile pic or just use google image search.
- convert to ES6
- have twitter refresh everytime page is loaded
- have news articles refresh once a day? -- have to delete old ones
- Handle API failures more gracefully
  
######
REAL TODOS:
######
- add actual css/bootstrap

Future:
- use a custom sql database for practice?
