# Python Calculator 🧮

Built this while learning Tkinter — wanted something more useful than
a hello world app. Ended up adding a history sidebar because I kept
forgetting what I calculated two steps ago.

## What it does
- Basic calculator — add, subtract, multiply, divide, percentage, decimal
- History sidebar shows past calculations
- History saves to a file so it's still there when you reopen the app
- Type numbers directly from keyboard — way faster than clicking
- Backspace to delete last digit, Escape to clear everything

## What I learned
- Tkinter grid layout — took a while to get buttons filling properly
- JSON for saving and loading data between sessions
- Keyboard event binding — `keysym` vs `event.char` was confusing at first
- Structuring a desktop app into a proper class

## Tech used
Python, Tkinter, JSON

## How to run
```bash
python main.py
```

## Known issues
- Doesn't handle very long equations well — display overflows
- History clears if you delete the JSON file manually

## What I want to add next
- Scientific mode with sin, cos, sqrt
- Copy result to clipboard button

## Author
Yogesh Madhukumar — still learning, building as I go 🚀