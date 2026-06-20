from django.shortcuts import render

# =============================================================================
# Webcam testing tool (used in place of a live model deployment).
# The trained model could not yet be deployed, so this is GazeRecorder's own
# web app — the same tool used to collect the project's custom gaze dataset.
# =============================================================================
WEBCAM_TEST_URL = "https://app.gazerecorder.com/Study/Test/?StudyID=e407abfc133eb183a37e85ef99f8cdd2&lang=en&RespondentID=null"

GITHUB_URL = "https://github.com/PrakharSaxena144/Minor_Project_2"  


def home(request):
    return render(request, 'core/home.html', {
        "webcam_url": WEBCAM_TEST_URL,
        "github_url": GITHUB_URL,
    })


def about(request):
    return render(request, 'core/about.html')


def contact(request):
    return render(request, 'core/contact.html')


def documentation(request):
    return render(request, 'core/documentation.html')


def results(request):
    """
    Final benchmark results for the three preprocessing pipelines evaluated
    on the ASD Saliency dataset (Zenodo 2647418).
    """
    pipelines = [
        {
            "name": "Pipeline 1 — Full Complex (Over-processed)",
            "steps": "Bilateral + Gaussian + CLAHE + Binarized + Adaptive + Morphological + Watershed",
            "accuracy": 61.36,
            "f1": 0.5854,
            "precision": 0.6316,
            "recall": 0.5455,
            "loss": 0.6845,
            "verdict": "worst",
        },
        {
            "name": "Pipeline 2 — Balanced",
            "steps": "CLAHE + Bilateral + Min-Max Norm + Binarized (best stage: CLAHE+Bilateral)",
            "accuracy": 82.31,
            "f1": 0.7965,
            "precision": 0.9375,
            "recall": 0.6923,
            "loss": 0.5154,
            "verdict": "good",
        },
        {
            "name": "Pipeline 3 — Best Overall",
            "steps": "CLAHE + Bilateral + Min-Max Norm (best stage: CLAHE+Bilateral)",
            "accuracy": 83.08,
            "f1": 0.8136,
            "precision": 0.9057,
            "recall": 0.7385,
            "loss": 0.4814,
            "verdict": "best",
        },
    ]

    confusion_matrix = {
        "tn": 60, "fp": 5, "fn": 17, "tp": 48,
        "accuracy": 83.08, "precision": 0.9057, "recall": 0.7385, "f1": 0.8136,
    }

    eda_features = [
        {"feature": "Entropy", "asd": 4.8083, "td": 4.7438, "direction": "ASD > TD"},
        {"feature": "Mean Intensity", "asd": 0.3271, "td": 0.3126, "direction": "ASD > TD"},
        {"feature": "Blob Spread", "asd": 51.8480, "td": 53.7431, "direction": "TD > ASD"},
        {"feature": "Contrast (RMS)", "asd": 0.1554, "td": 0.1509, "direction": "ASD > TD"},
        {"feature": "Mean Blob Size (px)", "asd": 1079.9533, "td": 1033.4023, "direction": "ASD > TD"},
        {"feature": "Number of Hotspots", "asd": 10.4481, "td": 10.8585, "direction": "TD > ASD"},
        {"feature": "Hot Area (%)", "asd": 24.9264, "td": 24.8876, "direction": "ASD > TD"},
    ]

    return render(request, "core/results.html", {
        "pipelines": pipelines,
        "confusion_matrix": confusion_matrix,
        "eda_features": eda_features,
        "webcam_url": WEBCAM_TEST_URL,
    })


def gallery(request):
    """
    Image Gallery — every pipeline visual from the report & presentation,
    grouped by stage of the project. Images live in
    static/images/gallery/ and are referenced by filename below.
    """
    base = "images/gallery/"
    categories = [
        {
            "key": "overview",
            "label": "ASD Spectrum & Dataset",
            "items": [
                {
                    "file": base + "slide04_img001.png",
                    "caption": "Autism Spectrum Disorder — Levels 1–3 (High-Functioning to Severe)",
                    "tag": "Background",
                },
                {
                    "file": base + "slide09_img004.png",
                    "caption": "Fixation point heatmap derived from raw scanpath data",
                    "tag": "Dataset",
                },
            ],
        },
        {
            "key": "heatmap-rationale",
            "label": "Why Heatmaps?",
            "items": [
                {
                    "file": base + "slide10_img005.png",
                    "caption": "Attention span level 4 — fully resolved fixation hotspot",
                    "tag": "Heatmap Construction",
                },
                {
                    "file": base + "slide10_img006.png",
                    "caption": "Attention span level 2 — early-stage gaze accumulation",
                    "tag": "Heatmap Construction",
                },
                {
                    "file": base + "slide10_img007.png",
                    "caption": "Attention span level 3 — intermediate gaze accumulation",
                    "tag": "Heatmap Construction",
                },
                {
                    "file": base + "slide10_img008.png",
                    "caption": "Attention span level 1 — initial diffuse gaze signal",
                    "tag": "Heatmap Construction",
                },
                {
                    "file": base + "slide10_img009.png",
                    "caption": "Real heatmap overlay — AMU Sir Syed House gate, gaze concentrated on the archway",
                    "tag": "Heatmap Construction",
                },
            ],
        },
        {
            "key": "custom-data",
            "label": "Custom GazeRecorder Data Collection",
            "items": [
                {
                    "file": base + "slide11_img010.png",
                    "caption": "GazeRecorder live session — heatmap overlay on AMU campus building",
                    "tag": "Custom Dataset",
                },
                {
                    "file": base + "slide12_img011.png",
                    "caption": "Custom dataset batch 1 — raw AMU landmark photographs (1–8)",
                    "tag": "Custom Dataset",
                },
                {
                    "file": base + "slide12_img012.png",
                    "caption": "Custom dataset batch 2 — corresponding gaze heatmap overlays (1–8)",
                    "tag": "Custom Dataset",
                },
            ],
        },
        {
            "key": "preprocessing-variants",
            "label": "Preprocessing Technique Variants",
            "items": [
                {
                    "file": base + "slide16_img014.png",
                    "caption": "All preprocessing variants on a single test image — raw, bilateral, gaussian, CLAHE, binarized (Otsu/adaptive), watershed, morphological",
                    "tag": "Preprocessing",
                },
            ],
        },
        {
            "key": "pipeline1",
            "label": "Pipeline 1 — Full Complex (Serial)",
            "items": [
                {
                    "file": base + "slide17_img016.png",
                    "caption": "Pipeline 1 serial stages — each step adds to the previous (Bilateral → Gaussian → CLAHE → Binarized → Adaptive → Morphological → Watershed)",
                    "tag": "Pipeline 1",
                },
                {
                    "file": base + "slide18_img017.png",
                    "caption": "Pipeline 1 results table — accuracy peaks at Stage 2 (80.77%), degrades with over-processing",
                    "tag": "Pipeline 1",
                },
                {
                    "file": base + "slide19_img018.png",
                    "caption": "Pipeline 1 best stage (bilateral+gaussian) — confusion matrix & test metrics",
                    "tag": "Pipeline 1",
                },
                {
                    "file": base + "slide20_img019.png",
                    "caption": "Pipeline 1 — accuracy, F1, precision & recall across all 7 cumulative stages",
                    "tag": "Pipeline 1",
                },
            ],
        },
        {
            "key": "pipeline2",
            "label": "Pipeline 2 — Balanced",
            "items": [
                {
                    "file": base + "slide21_img020.png",
                    "caption": "Pipeline 2 stages on raw stimulus image — CLAHE → Bilateral → Min-Max Norm → Binarized",
                    "tag": "Pipeline 2",
                },
                {
                    "file": base + "slide21_img021.png",
                    "caption": "Pipeline 2 stages on TD heatmap overlay",
                    "tag": "Pipeline 2",
                },
                {
                    "file": base + "slide22_img022.png",
                    "caption": "Pipeline 2 stages on ASD heatmap overlay",
                    "tag": "Pipeline 2",
                },
                {
                    "file": base + "slide22_img023.png",
                    "caption": "ASD vs TD difference map at final stage — 8.47% pixel difference",
                    "tag": "Pipeline 2",
                },
                {
                    "file": base + "slide23_img024.png",
                    "caption": "Pipeline 2 results table — best stage CLAHE+Bilateral at 82.31% accuracy",
                    "tag": "Pipeline 2",
                },
                {
                    "file": base + "slide24_img025.jpg",
                    "caption": "Pipeline 2 best stage (CLAHE+Bilateral) — confusion matrix & test metrics",
                    "tag": "Pipeline 2",
                },
                {
                    "file": base + "slide25_img026.png",
                    "caption": "Pipeline 2 — accuracy, F1, precision & recall across all cumulative stages",
                    "tag": "Pipeline 2",
                },
            ],
        },
        {
            "key": "pipeline3",
            "label": "Pipeline 3 — Best Overall",
            "items": [
                {
                    "file": base + "slide26_img027.png",
                    "caption": "Pipeline 3 stages on ASD heatmap — CLAHE → Bilateral → Min-Max Norm",
                    "tag": "Pipeline 3",
                },
                {
                    "file": base + "slide26_img028.png",
                    "caption": "Pipeline 3 stages on TD heatmap overlay",
                    "tag": "Pipeline 3",
                },
                {
                    "file": base + "slide27_img029.png",
                    "caption": "Pipeline 3 stages on raw stimulus image",
                    "tag": "Pipeline 3",
                },
                {
                    "file": base + "slide27_img030.png",
                    "caption": "ASD vs TD difference map — 97.32% difference (no binarisation, richer signal preserved)",
                    "tag": "Pipeline 3",
                },
                {
                    "file": base + "slide28_img031.png",
                    "caption": "Pipeline 3 results table — best stage CLAHE+Bilateral at 83.08% accuracy (highest overall)",
                    "tag": "Pipeline 3",
                },
                {
                    "file": base + "slide29_img032.jpg",
                    "caption": "Pipeline 3 best stage (CLAHE+Bilateral) — confusion matrix & test metrics",
                    "tag": "Pipeline 3",
                },
                {
                    "file": base + "slide30_img033.png",
                    "caption": "Pipeline 3 — accuracy, F1, precision & recall across all cumulative stages",
                    "tag": "Pipeline 3",
                },
            ],
        },
        {
            "key": "architecture",
            "label": "Final Model Architecture",
            "items": [
                {
                    "file": base + "slide31_img034.png",
                    "caption": "Final two-stage architecture — HSI preprocessing → GazePredictorUNet (Model 1) → OverlayClassifier (Model 2)",
                    "tag": "Architecture",
                },
                {
                    "file": base + "slide32_img035.png",
                    "caption": "Model 1 prediction example — ASD/TD region overlays with confidence scores on a test image",
                    "tag": "Architecture",
                },
            ],
        },
        {
            "key": "final-results",
            "label": "Final Comparative Results",
            "items": [
                {
                    "file": base + "slide33_img036.png",
                    "caption": "Final comparison — Pipeline 1 vs 2 vs 3 across all metrics; Pipeline 3 wins on accuracy, F1 and test loss",
                    "tag": "Final Results",
                },
            ],
        },
    ]

    return render(request, "core/gallery.html", {"categories": categories})


def code_explorer(request):
    """
    Lists the Google Colab notebooks used across the project's lifecycle,
    grouped by development phase, exactly as tracked in the project's
    internal Colab file index.
    """
    phases = [
        {
            "phase": "1. Early Work",
            "items": [
                {
                    "title": "CNNmodelASD — Load data & show raw images",
                    "desc": "Initial data loading utility to read the ASD Saliency dataset and preview raw stimulus/heatmap pairs before any preprocessing.",
                    "url": "https://colab.research.google.com/drive/1wtrAljVyoI2y521mk7aqWW1NQV3HkTN3",
                },
                {
                    "title": "ASD_DatasetLoading_Preprocessing — Special ASD preprocessing",
                    "desc": "Early experiments in loading and preprocessing ASD/TD heatmap pairs prior to settling on the final 3-pipeline strategy.",
                    "url": "https://colab.research.google.com/drive/1x6CUrZN4JlW3PQ_8UoWEJ08QQfpQd48R",
                },
            ],
        },
        {
            "phase": "2. Real Images and Models",
            "items": [
                {
                    "title": "ASD_Train_DA — Image display & rough training code",
                    "desc": "Draft training script with data augmentation, used to visualize sample images and rough out the training loop.",
                    "url": "https://colab.research.google.com/drive/1UrK69FBh215j_NnQ802_Dgh27wre3WA4",
                },
                {
                    "title": "EidSpecial — First structured model (Test Acc 62.5%)",
                    "desc": "First end-to-end model with defined architecture. Diagnosed with a data-leakage issue between train/test splits, capped at 62.5% test accuracy — informed the leak-proof split strategy used in later notebooks.",
                    "url": "https://colab.research.google.com/drive/1t8ABV-TFM-_46IBIZlxSzbJl11RyjKBl",
                },
            ],
        },
        {
            "phase": "3. Exploratory Data Analysis (EDA)",
            "items": [
                {
                    "title": "ASD_EDA_FeatureExtraction — Feature extraction & filtering",
                    "desc": "Dropped near-duplicate / very close facial fixation images; extracted heatmap-level statistical features (entropy, blob spread, contrast, hotspot count) summarized in the Results page.",
                    "url": "https://colab.research.google.com/drive/157bsOjOrU2o_myLd55CPNuVGiNwiLifa",
                },
            ],
        },
        {
            "phase": "4. Preprocessed Images",
            "items": [
                {
                    "title": "Main Preprocessing Pipeline Notebook",
                    "desc": "Implements the three serial preprocessing pipelines (CLAHE, Bilateral Filter, Gaussian Blur, Binarization, Morphological Ops, Watershed) and benchmarks each cumulative stage.",
                    "url": None,
                },
            ],
        },
        {
            "phase": "5. Better ASD Intensity Spots & Preprocessed Images",
            "items": [
                {
                    "title": "Intensity-Spot Refinement Experiments",
                    "desc": "Attempted refinement of ASD-discriminative hotspot detection on preprocessed heatmaps. Yielded poor accuracy relative to the CLAHE+Bilateral pipeline and was not carried forward into the final architecture.",
                    "url": None,
                },
            ],
        },
    ]

    final_architecture = {
        "title": "Final Two-Stage Architecture",
        "model1": "GazePredictorUNet — U-Net encoder-decoder with Squeeze-and-Excitation (SE) attention. "
                   "Input: [B,3,128,128] preprocessed stimulus. Output: [B,2,128,128] predicted ASD + TD gaze maps.",
        "model2": "OverlayClassifier — Residual CNN with Channel Attention. Input: 3-channel overlay "
                   "(actual heatmap, M1 prediction, element-wise product). Output: [B,2] logits (TD / ASD).",
    }

    selected_phase = request.GET.get("phase")

    return render(request, "core/code_explorer.html", {
        "phases": phases,
        "final_architecture": final_architecture,
        "selected_phase": selected_phase,
    })
