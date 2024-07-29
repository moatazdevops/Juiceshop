import requests
import sys
# sys.argv[1] means first attribute after script name
file_name= sys.argv[1]
scan_type= ''

# select scan_type based on file_name
if file_name == 'gitleaks.json':
    scan_type = 'Gitleaks Scan'
elif file_name == 'semgrep.json':
    scan_type = 'Semgrep JSON Report'
elif file_name == 'retire.json':
    scan_type = 'Retire.js Scan'

headers= {'Authorization': 'Token fa53ea0ff326840d427174cd89fce6345a83712a'}
url = 'https://demo.defectdojo.org/api/v2/import-scan/'
data= {'active': True, 'verified': True, 'scan_type': scan_type, 'minimum_severity': 'Low', 'engagement': 14}
files= {'file': open(file_name, 'rb')}
response= requests.post(url, headers=headers, data=data, files=files)

if response.status_code == 201:
    print('scan results imported successfully')
else:
    print(f'failed to import scan results: {response.content}')
    