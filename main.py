import meraki
import os

# Initialize Dashboard API
api_key = os.getenv('YOUR_API_KEY')
dashboard = meraki.DashboardAPI(api_key)

# Organization ID
ORGANIZATION_ID = 'YOUR_ORGANIZATION_ID'
OPTION_ADDRESS = "IP_ADDRESS"


def update_dhcp_options(network_id):
    try:
        # Fetch VLANs in the network
        vlans = dashboard.appliance.getNetworkApplianceVlans(network_id)
        print(vlans)
        # Find VLAN 100
        vlan100 = next((vlan for vlan in vlans if vlan['id'] == 100), None)
        print(vlan100)
        if vlan100:
            # Update DHCP options if VLAN 100 exists
            dhcp_options = [{'code': '161', 'type': 'text', 'value': OPTION_ADDRESS},
                            {'code': '186', 'type': 'text', 'value': OPTION_ADDRESS}]
            dashboard.appliance.updateNetworkApplianceVlan(network_id, '100', dhcpOptions=dhcp_options)
            print(f'Updated DHCP options for VLAN 100 in network {network_id}')
    except Exception as e:
        print(f'Error updating VLAN 100 DHCP options in network {network_id}: {e}')


def main():
    try:
        # Get all devices in the organization
        devices = dashboard.organizations.getOrganizationDevices(ORGANIZATION_ID)
        # Filter for MX devices
        mx_devices = [device for device in devices if 'MX' in device['model']]
        # Update DHCP options for each MX device
        for device in mx_devices:
            print(device)
            update_dhcp_options(device['networkId'])
    except Exception as e:
        print(f'Error retrieving devices or updating DHCP options: {e}')


if __name__ == "__main__":
    main()
