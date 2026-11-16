# Mock interview brief · Inventory ledger

Build a Python command-line program that reads inventory movements from a CSV file and prints the final stock by SKU. Use Python 3 and its standard library. Run it as `python stock.py INPUT.csv`.

## Input and output

- Input is UTF-8 CSV with the required header `sku,delta` in that order. Use normal CSV quoting rules. Each data record has exactly two fields.
- An SKU matches `[A-Z][A-Z0-9-]*`. A delta is a base-10 integer with ASCII digits and an optional leading `+` or `-`, between −1,000,000 and +1,000,000 inclusive. Whitespace is significant.
- Process movements in file order. Each SKU starts at zero. Reject a movement that would make its running stock negative, even if a later movement would restore it.
- For valid input, exit with status 0. Write CSV to stdout with header `sku,stock` and one row per SKU seen, sorted by SKU. Include SKUs with zero stock. A header-only input produces a header-only output.
- On a missing or unreadable file, invalid header, invalid record, or negative running stock, exit with status 1. Write no stdout and print a readable error to stderr. For a data error, include `row N` where the header is row 1 and rows count CSV records. Expected input errors should have no traceback.

## Example

Input

```csv
sku,delta
B-2,4
A1,3
B-2,-4
A1,+2
```

Expected stdout

```csv
sku,stock
A1,5
B-2,0
```

## Deliverables and interview policy

Submit `stock.py`, a short `README.md` with the command to run it, and any tests you wrote. Submit locally by recording the exact paths and the time you marked them ready. Add a short AI-use disclosure to the README describing material assistance and what you verified. Keep Platoon's working notes separate from the submission.

You have two hours from the confirmed start time. AI coding assistants, prepared prompts, shell commands, and local working files are permitted. The synthetic brief and exercise files may be shared with the selected assistant. Use local files for the exercise and preserve them for the discussion. The reviewer will run additional black-box checks against this brief. Be ready to explain running balances, error handling, and your verification.
