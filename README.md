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
- convert to ES6
- have twitter refresh everytime page is loaded
- have news articles refresh once a day? -- have to delete old ones -- put in queries 
		-- Entry.objects.filter(pub_date__year=2005).delete()

######
REAL TODOS:
######
- add actual css/bootstrap
- switch to imgur for picture
- Handle API failures more gracefully

Future:
- use a custom sql database for practice?
- some stuff with d3
