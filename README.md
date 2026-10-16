# Travel.pk URL Status Checker

A Python script that reads a CSV of 20 Travel.pk URLs and prints the HTTP status code of each.

## Files

- `check_status.py`: the script. Reads the `url` column of a CSV, issues a GET request per URL
  (Python standard library only, 25s timeout), and prints the final HTTP status code after redirects.
  Network or DNS failures print as ERROR.
- `travel_pk_urls.csv`: 20 real public URLs taken from the travel.pk sitemap
  (https://travel.pk/sitemap.xml).

## Run it

```
python3 check_status.py travel_pk_urls.csv
```

## Latest run (16 Oct 2026)

All 20 URLs returned HTTP 200.
