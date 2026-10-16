#!/usr/bin/env python3
"""Read a CSV of Travel.pk URLs and print the HTTP status code of each.

Usage:
    python3 check_status.py [travel_pk_urls.csv]

The CSV must have a header row with a 'url' column. For each URL the script
issues a GET request and prints the final HTTP status code (after redirects).
Network or DNS failures are printed as ERROR instead of a status code.
"""
import csv
import sys
import urllib.request
import urllib.error

CSV_PATH = sys.argv[1] if len(sys.argv) > 1 else "travel_pk_urls.csv"
TIMEOUT = 25
USER_AGENT = "Mozilla/5.0 (URL status checker)"


def status_of(url):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            return str(resp.status)
    except urllib.error.HTTPError as e:
        return str(e.code)
    except Exception as e:
        return f"ERROR ({type(e).__name__})"


def main():
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if "url" not in (reader.fieldnames or []):
            print(f"CSV must have a 'url' column, found: {reader.fieldnames}",
                  file=sys.stderr)
            sys.exit(1)
        for row in reader:
            url = (row.get("url") or "").strip()
            if not url:
                continue
            print(f"{url} -> {status_of(url)}", flush=True)


if __name__ == "__main__":
    main()
