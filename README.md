🛠️ HOW TO RUN LOGGER SCRIPT
===========================

✅ 1. INSTALL PYTHON (IF NOT ALREADY)
-------------------------------------
- Download Python from: https://www.python.org/downloads/
- Run the installer and check the box that says “Add Python to PATH”
- Click Install

✅ 2. PREPARE YOUR PROJECT FOLDER
---------------------------------
Create a folder with the following structure:

PRODIGY_CS_4/
├── logger.py               # Your Python script
├── keylog.txt              # This will store raw keystrokes
├── full_message.txt        # This will store grouped key sentences
└── screenshots/            # (optional) folder to store screenshots

Make sure `keylog.txt` and `full_message.txt` exist — even if they are empty at first.

✅ 3. ADD SAMPLE LOGS FOR TESTING
---------------------------------
Open `keylog.txt` and add a few test characters:

✅ 4. (OPTIONAL) ADD SCREENSHOTS
--------------------------------
Put some `.png` image files inside the `screenshots/` folder for testing screenshot handling.

✅ 5. RUN THE SCRIPT
--------------------
Open PowerShell or Command Prompt.

Navigate to your project folder:

Example:
cd "C:\Users\HP\Documents\Cyb projects\prodigy infotech\PRODIGY_CS_4"

Then run:
python logger.py

✅ 6. CHECK OUTPUT
------------------
After running, check these:
- `full_message.txt`: should contain grouped words like `hello world`
- `keylog.txt`: should still contain all raw key logs
- Screenshots will stay in the `screenshots/` folder

===========================
✅ DONE! SCRIPT RAN LOCALLY
===========================

This version doesn’t send emails. It only saves the keylogs and screenshots locally for review.
You can run it any time by repeating Step 5.
