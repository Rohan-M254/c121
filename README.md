# OpenCV Camera Effects

A small OpenCV practice project with two webcam experiments.

## Scripts

- `c121/blackScreen.py` — attempts a black-colour masking effect using a neutral black replacement background.
- `c121/invisablityCloak.py` — an incomplete experiment that begins capturing a background frame for a colour-based invisibility effect.

## Requirements

```bash
pip install opencv-python numpy
```

## Run

Run from the repository root:

```bash
python c121/blackScreen.py
```

Press `q` to exit the camera window.

## Status and limitations

These are experimental scripts, not finished applications. The invisibility-cloak script is incomplete. The black-screen script's colour thresholds are fixed and may need calibration for different lighting and cameras. Camera access is required.

The unidentified image previously referenced by the black-screen script has been removed from the proposed cleanup branch.