# Aditi Varshney — Flask Portfolio

## Project Structure

```
aditi_portfolio/
├── app.py                     # Flask app & all profile data
├── requirements.txt           # Dependencies
├── templates/
│   └── index.html             # Jinja2 HTML template
└── static/
    └── images/
        └── aditi_photo.jpeg   # Profile photo
```

## Setup & Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the app
```bash
python app.py
```

### 3. Open in browser
```
http://127.0.0.1:5000
```

## Updating Content
All profile data (skills, projects, education, certifications, awards) lives in `app.py` inside the `profile` dictionary in the `index()` route. Edit that file to update any content — no need to touch the HTML template.

## Replacing the Photo
Drop a new image into `static/images/` and update the filename reference in `app.py`:
```python
# In templates/index.html this line auto-picks it:
url_for('static', filename='images/YOUR_PHOTO.jpeg')
```
