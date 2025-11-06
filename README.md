# Cinepolis Auto GV Enter

A small Python automation script that detects input fields on-screen using image matching and types gift voucher IDs and PINs for you.

It is app-agnostic — as long as the target application's input fields are visible and you provide matching screenshots, the script will find the fields, click them, and type the values from `script.py`.

## Features
- Detects on-screen fields by matching provided images (e.g., `gv_id.png`, `pin.png`).
- Clicks detected fields and types voucher ID and PIN pairs from a list in `script.py`.
- Minimal dependencies and straightforward configuration.

## Quick contract
- Inputs: reference images of the target fields (PNG) and a Python list of vouchers in `script.py`.
- Outputs: keyboard input sent to the focused application and console progress messages.
- Error modes: image not found (script waits), wrong window focused, DPI/scale mismatch.

## Requirements
- Python 3.8+
- Windows (recommended) or any OS supported by `pyautogui`.

Suggested `requirements.txt`:
```
pyautogui==0.9.54
opencv-python==4.8.0.76
Pillow==9.5.0
```

Note: On Windows, `pyautogui` may require `pywin32` — pip usually installs the right dependencies.

## Setup
1. Create and activate a virtual environment, then install requirements:

```powershell
python -m venv .venv
; .\.venv\Scripts\Activate.ps1
; pip install -r requirements.txt
```

2. Place your reference images in the repository root or an `images/` folder. By default the script expects `gv_id.png` and `pin.png`.

## Preparing field images
- Capture a screenshot of the visual area of the input field (label, placeholder, or border).
- Save them as `gv_id.png` and `pin.png` (or update `script.py` with their paths).
- Ensure screenshots are taken at the same display scaling/DPI as when you run the script.

## Usage
1. Focus the target application where voucher entries should be typed.
2. Run the script:

```powershell
; .\.venv\Scripts\Activate.ps1
; python script.py
```

3. You have 5 seconds to focus the app after the script starts. The script will then wait for the field images to appear, click them, and type values from the `gift_vouchers` list.

The script currently asks you to manually click "Apply → Add Another GV" between entries; follow the printed prompts.

## Configuration
Edit `script.py` and modify the `gift_vouchers` list. Each entry has the form:

```python
{ "id": "1010040036200170", "pin": "119171" }
```

## Tuning & Tips
- Increase or decrease the `confidence` argument used in `pyautogui.locateOnScreen()` to make matching stricter or looser.
- Crop images to stable UI elements if parts of the UI animate.
- Use the same display scaling when capturing screenshots and when running the script.

## Safety
- Test with one voucher first.
- Keep sensitive data out of version control. Add voucher lists and images to `.gitignore` if needed.
- Use responsibly and respect the target app's terms of service.

## Troubleshooting
- "Image not found": re-capture screenshots, check display scaling, or lower confidence.
- "Typing in wrong window": make sure the app is focused during the 5-second window.
- Permission errors on Windows: run PowerShell as Administrator if necessary.

## Extending to other apps
Replace `gv_id.png` and `pin.png` with screenshots from the new app and add or adapt the typing flow in `script.py`.
