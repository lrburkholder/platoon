"""Run the inventory ledger acceptance checks against an exercise folder."""

import argparse
import csv
from io import StringIO
from pathlib import Path
import re
import subprocess
import sys
from tempfile import TemporaryDirectory


CASES = (
    (
        "combine movements, sort SKUs, retain zero balances",
        'sku,delta\r\n"B-2",4\r\nA1,3\r\nB-2,-4\r\nA1,+2\r\n',
        "sku,stock\nA1,5\nB-2,0\n",
        None,
    ),
    ("header only", "sku,delta\n", "sku,stock\n", None),
    ("bad header", "delta,sku\n2,A1\n", None, None),
    ("bad SKU after a valid movement", "sku,delta\nA1,2\na1,3\n", None, 3),
    ("fractional delta", "sku,delta\nA1,1.5\n", None, 2),
    ("delta outside allowed range", "sku,delta\nA1,1000001\n", None, 2),
    ("extra field", "sku,delta\nA1,1,extra\n", None, 2),
    ("negative balance before recovery", "sku,delta\nA1,2\nA1,-3\nA1,5\n", None, 3),
    ("missing file", None, None, None),
)


def check_result(result, expected_output, error_row):
    if expected_output is not None:
        if result.returncode == 0:
            try:
                rows = list(csv.reader(StringIO(result.stdout), strict=True))
            except csv.Error as error:
                return f"stdout is invalid CSV ({error})"
            if rows == list(csv.reader(StringIO(expected_output))):
                return None
        return f"expected status 0 and CSV matching {expected_output!r}"

    if result.returncode != 1 or result.stdout or not result.stderr.strip():
        return "expected status 1, empty stdout, and an error on stderr"
    if "Traceback (most recent call last)" in result.stderr:
        return "expected a readable error without a traceback"
    if error_row is not None and not re.search(
        rf"\brow\s+{error_row}\b", result.stderr, re.IGNORECASE
    ):
        return f"expected row {error_row} in the error"
    return None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("exercise", type=Path, help="Folder containing stock.py")
    exercise = parser.parse_args().exercise.resolve()
    program = exercise / "stock.py"
    if not program.is_file():
        print(f"Pending implementation: {program} does not exist.", file=sys.stderr)
        return 1

    failures = 0
    with TemporaryDirectory(prefix="platoon-inventory-") as directory:
        for index, (label, csv_input, expected_output, error_row) in enumerate(CASES):
            input_file = Path(directory) / f"input {index}.csv"
            if csv_input is not None:
                input_file.write_bytes(csv_input.encode("utf-8"))
            try:
                result = subprocess.run(
                    [sys.executable, str(program), str(input_file)],
                    cwd=exercise,
                    capture_output=True,
                    text=True,
                    errors="replace",
                    timeout=5,
                )
            except subprocess.TimeoutExpired:
                failures += 1
                print(f"FAIL {label} (timed out)")
                continue
            problem = check_result(result, expected_output, error_row)
            if problem:
                failures += 1
                print(
                    f"FAIL {label} ({problem}). "
                    f"Got status {result.returncode}, stdout {result.stdout!r}, "
                    f"stderr {result.stderr!r}."
                )
            else:
                print(f"PASS {label}")

    print(f"{len(CASES) - failures}/{len(CASES)} checks passed.")
    return int(failures != 0)


if __name__ == "__main__":
    sys.exit(main())
