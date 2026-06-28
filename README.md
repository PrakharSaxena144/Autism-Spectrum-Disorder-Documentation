# ASD Gaze Screening AI — Documentation Website

A Django documentation site for **Early Screening of Autism in Children Through
Eye-Movement & Sensory Signals** (Minor Project II, AIP3952).

Built as a sibling project to the UrbanDeviationAI documentation site, restyled
for a healthcare/clinical-research visual identity.

## Pages

| Route | Purpose |
|---|---|
| `/` | Hero, epidemiology stats, pipeline snapshot |
| `/documentation/` | Full technical write-up — dataset, EDA, CLAHE, preprocessing pipelines, Model 1 (GazePredictorUNet), Model 2 (OverlayClassifier), evaluation |
| `/results/` | Pipeline comparison table, confusion matrix, EDA statistical table, key observations |
| `/gallery/` | Filterable image gallery — all figures from the report & slide deck, with lightbox viewer |
| `/code-explorer/` | All Google Colab notebooks from the project, grouped by development phase |
| `/about/` | Team & supervision |
| `/contact/` | Contact card |

## Live Webcam Test

Because the trained classifier is **not yet deployed for live inference**, every
"try it" call-to-action across the site links out to:

```
https://app.gazerecorder.com/
```

This is the same webcam-based eye-tracking tool used to collect this project's
custom gaze dataset. Update `WEBCAM_TEST_URL` in `core/views.py` once a real
model endpoint is deployed.

## Local Setup

```bash
python -m venv venv
source venv/bin/activate        # venv\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py runserver
```

Visit `http://127.0.0.1:8000/`.

## Deploying to Render

1. Push this repo to GitHub.
2. On [Render](https://render.com), create a new **Web Service** from the repo —
   `render.yaml` is already configured (build + start commands, Python version).
3. Render will run:
   ```
   pip install -r requirements.txt && python manage.py collectstatic --noinput
   gunicorn asd_screening_ai.wsgi:application
   ```
4. No environment variables are required beyond what's in `render.yaml`.

## Editing Content

All project content (pipeline results, EDA table, confusion matrix, Colab notebook
list) lives as plain Python data structures in **`core/views.py`** — no database
required. Update the lists/dicts there and the templates re-render automatically.

To add a new Colab notebook to the Code Explorer, add an entry to the relevant
`phase["items"]` list in the `code_explorer` view:

```python
{
    "title": "Notebook Title",
    "desc": "What this notebook does and why it matters.",
    "url": "https://colab.research.google.com/drive/...",
}
```

To add a new image to the Gallery, drop the file into
`static/images/gallery/` and add an entry to the relevant category's
`items` list in the `gallery` view:

```python
{
    "file": base + "your_image.png",
    "caption": "What this figure shows.",
    "tag": "Pipeline 3",   # shown as the small label above the caption
}
```

Run `python manage.py collectstatic --noinput` after adding new static images
so whitenoise picks them up.

## Project Structure

```
asd_screening_ai/
├── core/
│   ├── templates/core/   # base, home, documentation, results, code_explorer, about, contact
│   ├── views.py          # all content as Python data + render() calls
│   ├── urls.py
│   └── models.py         # intentionally empty — static content site
├── static/
│   └── css/style.css     # clinical/healthcare visual identity
├── asd_screening_ai/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
└── render.yaml
```

## Code Base
I have upload all the experiments and data on the following github repo:-

Link: https://github.com/PrakharSaxena144/Minor_Project_2

## Credits

- Dataset: ASD Saliency Dataset, Zenodo DOI `10.5281/zenodo.2647418`
- Webcam eye-tracking: [GazeRecorder](https://gazerecorder.com)
- Team: Prakhar Saxena (23AIBEA187), Aryan Parashar (23AIBEA214)
- Supervisor: Junaid Ali Reshi, Interdisciplinary Centre for AI, ZHCET, AMU
