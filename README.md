# magic-optimizer
Optimizes your images for the web using (Image)Magic(k).

## Installation
Installation and running is fairly straightforward, even if you aren't familiar with Python.

1. Download and install [ImageMagick](https://imagemagick.org/script/download.php), if you haven't already
2. Download and install a recent version of [Python](https://www.python.org/downloads/), if you haven't already
3. Download this repository. There are several ways to do this:
   1. (preferred) Git Clone
      1. Open up a terminal (If you're on windows, be sure to use Git Bash instead of `cmd` or powershell)
      2. Type in `git clone https://github.com/lumitry/magic-optimizer` (use `cd <path>` beforehand to get to your preferred directory, if desired)
      3. Type in `cd magic-optimizer` after the clone has completed
      4. Run `python optim.py` to run the program!
      5. When you want to update the program, just open up your terminal, run `cd magic-optimizer` then `git pull`
   2. Download as Zip
      1. Click on the green "Code" button next to the 'about' section near the top of this page.
      2. Click on the "Download Zip" button at the bottom of that pop-up.
      3. Unzip the file as you would any other zip file.
      4. If desired, move the unzipped folder into another folder where you'd like the program to be.
      5. Open up your terminal into the unzipped "magic-optimizer" folder and type in `python optim.py` then hit enter.
4. That's it! You're done! 😄

## Usage
Should be self-explanatory, I'll add more details about usage later. (TODO)

## Roadmap
- [ ] Fix TODOs in `README.md`
- [ ] Fix TODOs in `optim.py`
- [ ] Use CLI args instead of stdin (e.g., `python optim.py --input 'sample_image.jpg' --formats jpeg avif png --qualities 0.5 1 2 --output ~/Pictures/web_safe`)
  - [ ] Gooey for GUI?
- [ ] Move global variables to a `config.txt` file
- [ ] Maybe separate into multiple files where applicable?
- [ ] Add license
- [ ] Set up actions to release a .zip file to simplify installation process

## Modification
It is possible to modify the code to make it work more to certain needs:
- Allowing odd file types (like `.pdf`) to be converted to images
  - TODO: Explain how
- probably others
  - TODO: Add more

Of course, I can't provide support

## Usage as a Library
It's not recommended, but `optim.py` is designed to be able to be used by other python scripts with few issues. If you're encountering errors, I can't guarantee that I will provide support, but feel free to open a GitHub Issue and describe your problem. I'd like to make this the best program I possibly can