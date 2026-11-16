# Instagram Uploader (Flask)

A small Flask web app that logs in to an Instagram account and uploads a video as a Reel.

## What it does

- Shows a login page and signs in to Instagram through the unofficial `instagrapi` client.
- Saves the login session to a local `dump.json` file so later logins can be faster.
- After login, shows an upload form with a media file, tags and a date-time field.
- Saves the uploaded file to `~/Windows/uploads` and posts it as a Reel.
- Includes an experimental helper for reading a Reel's details and downloading it by URL.

Scheduled posting with APScheduler is sketched in the code but commented out, so uploads happen immediately.

## Built with

- Python
- Flask (HTML templates in `templates/`, CSS in `static/`)
- [instagrapi](https://github.com/subzeroid/instagrapi) (unofficial Instagram private API client)
- APScheduler

## Run it

1. Install Python 3 and the dependencies:

       pip install flask instagrapi apscheduler

2. Keep credentials out of the code. Put your Instagram username and password in environment variables or a local `.env` file that is never committed (add `.env` and `dump.json` to `.gitignore`), and make sure no login details are hard-coded in `insta_api.py` before you run it.
3. Start the app:

       python app.py

4. Open http://localhost:5000, sign in, then choose a video and submit the form.

## Security

Never commit access tokens, passwords, session files (`dump.json`), cookies or other credentials. `instagrapi` uses Instagram's private API, which is not officially supported; automated logins can trigger account checks, so use a test account and follow Instagram's current terms.

## Project status

Early learning project. It is not maintained; error handling is minimal and the session is stored locally in plain JSON.

---

Part of [Aryan Gupta's projects](https://github.com/AryanGupta-234). Building [NOBAD](https://nobad-platform.aassworld99.workers.dev/): software with a point of view.
