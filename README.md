# WPScan Extractor

Quick and easy was to extract outdated plugins from a WordPress site following a WPscan, especially useful to get an overview if there are many outdated plugins.
Output is a CSV file with 3 columns: outdated plugin name, vulnerability and CVE (if available).

## Usage

Run wpscan using the following flag `-o wpscan.json --format json`

Then run

`python3 wpse.py wpscan.json`

For help use `-h` flag
