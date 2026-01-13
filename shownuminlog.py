#!/usr/bin/env python3
import argparse
import math
import sys

RESET = "\033[0m"
GREEN_BG = "\033[42m"
GRAY_BG = "\033[100m"


def calculate_bounds(value: float) -> tuple[float, float]:
    exponent = math.floor(math.log10(value))
    minimum = 10 ** exponent
    maximum = 10 ** (exponent + 1)
    return minimum, maximum


def build_label_line(width: int, position: int, label: str) -> str:
    position = max(0, min(width, position))
    line = [" "] * (width + 1)
    start = max(0, min(width - len(label) + 1, position - len(label) // 2))
    for idx, char in enumerate(label):
        if start + idx <= width:
            line[start + idx] = char
    return "".join(line)


def render_bar(value: float, width: int = 40) -> str:
    minimum, maximum = calculate_bounds(value)
    progress = math.log10(value / minimum)
    percent = progress * 100

    filled = int(round(progress * width))
    filled = max(0, min(width, filled))

    bar = f"{GREEN_BG}{' ' * filled}{GRAY_BG}{' ' * (width - filled)}{RESET}"

    percent_label = f"{percent:.1f}%"
    percent_line = build_label_line(width, filled, percent_label)

    min_label = f"{minimum:g}"
    max_label = f"{maximum:g}"
    min_max_line = min_label.ljust(width + 1 - len(max_label)) + max_label

    value_label = f"{value:g}"
    value_line = build_label_line(width, filled, value_label)

    return "\n".join([percent_line, bar, min_max_line, value_line])


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Show a logarithmic progress bar for a positive number.")
    parser.add_argument("value", type=float, help="Input number (must be > 0)")
    parser.add_argument(
        "--width",
        type=int,
        default=40,
        help="Width of the bar in characters (default: 40)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.value <= 0:
        print("Error: value must be greater than 0.", file=sys.stderr)
        return 1
    if args.width <= 0:
        print("Error: width must be greater than 0.", file=sys.stderr)
        return 1

    print(render_bar(args.value, args.width))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
