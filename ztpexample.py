from ztprender import template_loader
from ztprender import dhcp_loader
import os

def main():

	# Location to place conf files after generation 
	conf_dest = '/usr/share/nginx/html/'
	# Location to place DHCP config file after generation 
	dhcp_conf_dest = '/etc/dhcp/dhcpd.conf'
	# Generate Juniper Config
	template_loader('csv/hosts_data.csv', conf_dest)
	# Generate DHCP Config
	dhcp_loader('csv/hosts_data.csv', dhcp_conf_dest)
	
	# Restart the DHCPD service
	os.system("sudo systemctl restart dhcpd")
	
	# Restart the Nginx service
	os.system("sudo systemctl restart nginx")

if __name__== "__main__":
	main()