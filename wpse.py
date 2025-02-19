import json
import csv
import argparse

def process_json_to_csv(json_file, csv_file='wps_results.csv'):
    with open(json_file, 'r') as file:
        data = json.load(file)
    
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Plugin', 'Status', 'Current Version', 'Latest Version', 'Vulnerability', 'CVE'])

        # Process main theme if it exists and is outdated
        if 'main_theme' in data and data['main_theme'].get('outdated'):
            theme_data = data['main_theme']
            theme_name = f"Theme: {theme_data.get('style_name', 'Unknown')}"
            current_ver = theme_data.get('version', {}).get('number', 'Unknown')
            latest_ver = theme_data.get('latest_version', 'Unknown')
            
            if 'vulnerabilities' in theme_data and theme_data['vulnerabilities']:
                for vuln in theme_data['vulnerabilities']:
                    cve = ', '.join(vuln['references'].get('cve', [])) if 'references' in vuln and 'cve' in vuln['references'] else 'N/A'
                    writer.writerow([theme_name, 'Outdated', current_ver, latest_ver, vuln.get('title', 'Unknown'), cve])
            else:
                writer.writerow([theme_name, 'Outdated', current_ver, latest_ver, 'No known vulnerabilities', 'N/A'])

        # Process plugins
        for plugin_name, plugin_data in data['plugins'].items():
            if plugin_data.get('outdated'):
                current_ver = plugin_data.get('version', {}).get('number', 'Unknown')
                latest_ver = plugin_data.get('latest_version', 'Unknown')
                
                if 'vulnerabilities' in plugin_data and plugin_data['vulnerabilities']:
                    for vuln in plugin_data['vulnerabilities']:
                        cve = ', '.join(vuln['references'].get('cve', [])) if 'references' in vuln and 'cve' in vuln['references'] else 'N/A'
                        writer.writerow([plugin_name, 'Outdated', current_ver, latest_ver, vuln.get('title', 'Unknown'), cve])
                else:
                    writer.writerow([plugin_name, 'Outdated', current_ver, latest_ver, 'No known vulnerabilities', 'N/A'])

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
