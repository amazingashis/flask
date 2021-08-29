"# flask" 

//////////////////////////   Extract The requirements ////////////////////////

pip freeze > requirements.txt

///////////////////////////     App redirect        /////////////////////
Create a Procfile
web: gunicorn app:app     #Give the Path
pip install gunicorn
