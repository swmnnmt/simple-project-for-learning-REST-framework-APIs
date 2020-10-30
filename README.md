# Novel Series project
simple project for learning REST framework APIs

## How to run

To run in development mode; Just use steps below:

1. Install `python3.8`, `pip`, `virtualenv` in your system.
2. Clone the project `https://github.com/swmnnmt/simple-project-for-learning-REST-framework-APIs`.
3. Make development environment ready using commands below;

  ```bash
  git clone https://github.com/swmnnmt/simple-project-for-learning-REST-framework-APIs.git && cd simple-project-for-learning-REST-framework-APIs
  virtualenv -p python3 .venv  # Create virtualenv named .venv
  source .venv/bin/activate
  pip install -r requirements.txt
  python manage.py migrate  # Create database tables
  ```

4. Run `simple-project` using `python manage.py runserver`
5. Go to [http://localhost:8000](http://localhost:8000) to see your simple-project version.

## Run On Windows

If You're On A Windows Machine , Make Environment Ready By Following Steps Below:
1. Install `python3`, `pip`, `virtualenv` 
2. Clone the project using:  `https://github.com/swmnnmt/simple-project-for-learning-REST-framework-APIs.git`.
3. Make Environment Ready Like This:
``` Command Prompt
cd cd simple-project-for-learning-REST-framework-APIs
virutalenv -p "PATH\TO\Python.exe" .venv # Give Full Path To python.exe
.venv\Scripts\activate # Activate The Virutal Environment
pip install -r requirements.txt
