import json
import csv
import argparse

def process_json_to_csv(json_file, csv_file='wps_results.csv'):
    with open(json_file, 'r') as file:
        data = json.load(file)
    
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Plugin', 'Vulnerability', 'CVE'])  # Changed 'Title' to 'Vulnerability'

        # Iterate through each plugin in the 'plugins' dictionary
        for plugin_name, plugin_data in data['plugins'].items():
            # Check if 'vulnerabilities' key exists and has items
            if 'vulnerabilities' in plugin_data and plugin_data['vulnerabilities']:
                for vulnerability in plugin_data['vulnerabilities']:
                    title = vulnerability['title']
                    cve = ', '.join(vulnerability['references']['cve']) if 'cve' in vulnerability['references'] else 'N/A'
                    # Write each vulnerability along with the plugin name
                    writer.writerow([plugin_name, title, cve])

def main():
    parser = argparse.ArgumentParser(description="Extracts vulnerabilities from a JSON file into a CSV file.")
    parser.add_argument('json_file', type=str, help='Path to the JSON input file.')
    parser.add_argument('-o', '--output', type=str, help='Optional: Output CSV file name (default is "wps_results.csv").', default='wps_results.csv')
    
    args = parser.parse_args()

    # Process the JSON to CSV conversion
    process_json_to_csv(args.json_file, args.output)
    print(f"Data has been successfully written to {args.output}")

if __name__ == '__main__':
    main()
