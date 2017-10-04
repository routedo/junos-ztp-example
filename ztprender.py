import jinja2
import csv
#import collections
import os
from shutil import copyfile

## cvs_file = Location of the file containing variables to use with the jinja2 template
## conf_dest = Location to place generated config file.

def template_loader(cvs_file, conf_dest):

	template_filename = 'template/jun_tor_template.j2'
	wan_template_filename = 'template/jun_access_template.j2'
	
	env = jinja2.Environment(loader=jinja2.FileSystemLoader('./'))

	tor_template = env.get_template(template_filename)
	wan_template = env.get_template(wan_template_filename)

	for row in csv.DictReader(open(cvs_file)):
		with open(conf_dest + row['hostname'] + '.config', 'w+') as f:
			g = str(row['hostname'])
			if 'tor' in g:
				f.write(tor_template.render(row))
			else:
				f.write(wan_template.render(row))
				
## cvs_file = Location of the file containing variables to use with the jinja2 template
## dhcp_conf_dest = Location to place generated dhcpd.conf file

def dhcp_loader(cvs_file, dhcp_conf_dest):

	dhcp_template_filename = 'template/junos_dhcp.j2'
	dhcp_conf_base = 'template/dhcpd_base.conf'

	try:
		## Atempt to delete exsisting dhcpd.conf file
		os.remove(dhcp_conf_dest)
	except OSError:
		pass

	## Copy dhcpd.conf file from the templates folder	
	copyfile(dhcp_conf_base, dhcp_conf_dest)
	
	env = jinja2.Environment(loader=jinja2.FileSystemLoader('./'))

	template = env.get_template(dhcp_template_filename)

	for row in csv.DictReader(open(cvs_file)):
		with open(dhcp_conf_dest, 'a') as f:
			g = str(row['hostname'])
			f.write(template.render(row))
		
	with open(dhcp_conf_dest, 'a') as f:
		f.write('}')