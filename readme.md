* # Title: My First Real Python Script: The Downloads Organizer

* The Goal: I have a bad habit of starting tutorials and never finishing a real project. My Downloads folder was a mess of images, so I decided to actually build a tool to fix it. This is my first step toward getting ready for GSoC 2026.

* What it actually does: It looks into my C:\Users\...\Downloads folder and finds all the pictures (.jpg, .png, .gif, etc.). It then moves them into a new folder called "Images" so I don't have to do it manually.

* My Learning Journey (The Hard Parts):

    The "OS" Mystery: At first, I didn't understand how Python could "touch" my computer. I used the os library to handle paths. I learned that os.path.join is better than just typing slashes because it's more professional.

    Breaking the Logic: I initially struggled with the if statements. I had to figure out how to check if a file already exists so I didn't accidentally delete my photos by overwriting them.

    Using Tools: I used an AI partner to help me understand the structure when I got stuck, but I wrote the logic for the file counter and the multi-extension support myself.

  * "DAY_2 ADDITIONS"

    After getting the image move to work, I realized a real Downloads folder needs more logic. I upgraded the script to:
    * Categorize by Type: I moved from a simple list to a Python Dictionary. Now the script handles Images, Documents, Applications, Videos, and Music.

    * Multi Need Folders: The script now creates the folder only if it finds a file that belongs there.

    * The break logic: Added break logic to stop the loop early once a match is found.

  * Day 3: Making it "Professional"

      I realized that if I want to reach GSoC, my code can't just work—it has to be safe and smart.

      * Error Handling: I added a "safety net." If a file is open or locked, the script doesn't crash anymore; it just skips it and moves to the next one.

      * Logging: The script now keeps a "diary" (organizer_log.txt). It records exactly what happened and when, so I don't have to guess.

      * Safety Checks: I added a summary at the end. It tells me exactly how many files were moved, which helps me make sure no one has messed with my logs.
  * Day 4: Architectural Changes (Modularization & Config)

    Today it became quite easy to go with the flow and from "basic scripts" I started building a real system with help of AI.

    * Modularization: I broke my code into specialized "tools" (functions). One for logging, one for folder creation, and one for loading data. This makes the code cleaner and easier to fix.

    * External Configuration (JSON): I separated the Logic from the Data. Instead of having folder names inside my code, I moved them to a config.json file.

    -> Why: Now, I can change which files get organized without ever touching the Python code. 
How to run it:

1. Make sure Python is installed.

2. Keep organizer.py and config.json in the same folder.

3. Change the path variable to your own Downloads folder.

3. Run python organizer.py