

## About

A kernel for a text based RPG (Made to be modified)

## Features

1. Combat system
2. Customizeable weapons
3. Customizeable enemies


## Usage 

1. Install "uv" (A fast python package manager)

On linux run:

curl -Ls https://astral.sh/uv/install.sh | sh



On windows:
(Powershell / Command Prompt)
iwr https://astral.sh/uv/install.ps1 -useb | iex


2. Download all the files (main.py, combat.py, text.py, game_data.py)

3. Put all the files in the same folder.

4. Go to the directory and start a command prompt there.

5. Run it. To do so, on linux run these 3 commands:

uv venv
source .venv/bin/activate
python main.py

If you're on windows:

uv venv
.venv\Scripts\activate (if in command prompt. If in powershell, run: .venv\Scripts\Activate.ps1)
python main.py



