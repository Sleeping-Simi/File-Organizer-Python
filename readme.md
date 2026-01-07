* # Title: My First Real Python Script: The Downloads Organizer

* The Goal: I have a bad habit of starting tutorials and never finishing a real project. My Downloads folder was a mess of images, so I decided to actually build a tool to fix it. This is my first step toward getting ready for GSoC 2026.

* What it actually does: It looks into my C:\Users\...\Downloads folder and finds all the pictures (.jpg, .png, .gif, etc.). It then moves them into a new folder called "Images" so I don't have to do it manually.

* My Learning Journey (The Hard Parts):

    The "OS" Mystery: At first, I didn't understand how Python could "touch" my computer. I used the os library to handle paths. I learned that os.path.join is better than just typing slashes because it's more professional.

    Breaking the Logic: I initially struggled with the if statements. I had to figure out how to check if a file already exists so I didn't accidentally delete my photos by overwriting them.

    Using Tools: I used an AI partner to help me understand the structure when I got stuck, but I wrote the logic for the file counter and the multi-extension support myself.

How to run it:

1. Make sure Python is installed.

2. Change the path variable to your own Downloads folder.

3. Run python organizer.py