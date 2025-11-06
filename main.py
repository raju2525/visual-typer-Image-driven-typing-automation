import pyautogui
import time
import cv2

# Updated list of gift vouchers
gift_vouchers = [
    
# --- Vouchers added from your images ---


  { "id": "1010040036200170", "pin": "119171" },
  { "id": "1010040037748321", "pin": "131894" },
  { "id": "1010040035162058", "pin": "255885" },
  { "id": "1010040036231195", "pin": "141368" },
  { "id": "1010040032292451", "pin": "160015" }
  
 
 
    
    
]

# Time to open Cinepolis app window
print("You have 5 seconds to open and focus Cinepolis app...")
time.sleep(5)

# Function to wait for an image to appear on screen
def wait_for_field(image_path, confidence=0.7):
    print(f"⏳ Waiting for {image_path} to appear...")
    while True:
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=confidence)
            if location:
                print(f"✅ Found {image_path}!")
                return location
        except Exception:
            # Keep looping without quitting if not found
            pass
        time.sleep(1)

# Main loop to enter vouchers
for gv in gift_vouchers:
    # Wait for GV ID and PIN fields to appear
    id_field = wait_for_field("images/gv_id.png")
    pin_field = wait_for_field("images/pin.png")

    # Enter GV ID
    pyautogui.click(pyautogui.center(id_field))
    pyautogui.typewrite(gv["id"], interval=0.05)

    # Enter PIN
    pyautogui.click(pyautogui.center(pin_field))
    pyautogui.typewrite(gv["pin"], interval=0.05)

    print(f"✅ Entered GV: {gv['id']} | PIN: {gv['pin']}")
    print("Now manually click Apply → Add Another GV...")

    # Wait until GV ID field reappears to confirm ready for next
    while pyautogui.locateOnScreen("images/gv_id.png", confidence=0.8) is None:
        time.sleep(1)
    print("Detected next entry screen. Moving to next GV...")

print("🎉 All vouchers processed successfully!")
