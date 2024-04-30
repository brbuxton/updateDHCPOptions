# Meraki DHCP Option Updater
This Python script automates the process of updating DHCP options for VLAN 100 on Meraki MX devices within a specified organization. It specifically sets the DHCP options 161 and 186 to a predefined IP address.

## Requirements
Python 3.6 or higher
meraki Python module
Access to a Meraki organization with appropriate administrative privileges
## Installation
### Clone the repository:
```bash
git clone [repository-url]
cd [repository-folder]
```
### Install dependencies:
```bash
pip install -r requirements.txt
```
### Set up environment variables and constants:
YOUR_API_KEY: Your Meraki Dashboard API key.
YOUR_ORGANIZATION_ID: The ID of your Meraki organization.
IP_ADDRESS: The IP address you want to set for DHCP options 161 and 186.
It's recommended to set these variables in your environment to avoid hard-coding sensitive information in your scripts.
```bash
export YOUR_API_KEY='your_api_key_here'
```
## Usage
Once the environment variables are set, you can run the script directly from the command line:

```bash
python update_dhcp_options.py
```
### How It Works
1. __Initialization:__
The script initializes the Meraki Dashboard API client using the API key from the environment variables.
2. __Device Retrieval:__
It retrieves all devices from the specified organization and filters out the MX models.
3. __DHCP Option Update:__
For each MX device, it checks if VLAN 100 exists. If it does, the script updates DHCP options 161 and 186 to the specified IP address.
4. __Error Handling:__
The script includes basic error handling to manage potential issues during the API calls.
## License
https://github.com/CiscoSE/cisco-sample-code/blob/master/LICENSE

## Disclaimer

This script is provided "as is", without warranty of any kind. Use it at your own risk.