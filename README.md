# shownuminlog

A small program to show a number in a logarithmic progress bar.

## Usage

```bash
python3 shownuminlog.py 20
python3 shownuminlog.py 300 --width 50
```

The bar adjusts its minimum and maximum bounds to the surrounding powers of 10.
The finished portion is green, the unfinished portion is gray, and labels show
percentage, bounds, and the input value.
