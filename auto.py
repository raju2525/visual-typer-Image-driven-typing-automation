import pyautogui
import time
import cv2

# Sample list of gift vouchers (replace with your 20 actual IDs and PINs)
gift_vouchers = [
    {"id": "1010040037078502", "pin": "129947"},
    {"id": "1010040038618962", "pin": "226462"},
    {"id": "1010040038699092", "pin": "103979"},
    {"id": "1010040039593605", "pin": "177993"},
    {"id": "1010040030697000", "pin": "156069"},
    {"id": "1010040030552423", "pin": "187024"},
    {"id": "1010040031649969", "pin": "226240"},
    {"id": "1010040031053011", "pin": "146804"},
    {"id": "1010040035572069", "pin": "142415"},
    {"id": "1010040031449237", "pin": "167382"},
    {"id": "1010040031666912", "pin": "179408"},
    {"id": "1010040033344936", "pin": "132348"},
    {"id": "1010040036094187", "pin": "127787"},
    {"id": "1010040035669795", "pin": "116993"},
    {"id": "1010040033908908", "pin": "161532"}
   
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
    id_field = wait_for_field("gv_id.png")
    pin_field = wait_for_field("pin.png")

    # Enter GV ID
    pyautogui.click(pyautogui.center(id_field))
    pyautogui.typewrite(gv["id"], interval=0.05)

    # Enter PIN
    pyautogui.click(pyautogui.center(pin_field))
    pyautogui.typewrite(gv["pin"], interval=0.05)

    print(f"✅ Entered GV: {gv['id']} | PIN: {gv['pin']}")
    print("Now manually click Apply → Add Another GV...")

    # Wait until GV ID field reappears to confirm ready for next
    while pyautogui.locateOnScreen("gv_id.png", confidence=0.8) is None:
        time.sleep(1)
    print("Detected next entry screen. Moving to next GV...")

print("🎉 All vouchers processed successfully!")
