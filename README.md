# About Project
  This project shows examples of how to use Python and Jinja2 to automate the setup of a Juniper [zero touch provisioning (ZTP)](https://www.juniper.net/documentation/en_US/junos/topics/concept/software-image-and-configuration-automatic-provisioning-understanding.html) environment.
 
# System requirements

###### Tested using:
	python 2.7.5 
	jinja2 2.9.6

###### Dependencies
	Jinja2
	 pip install jinja2 
# Example

###### ztpExample.py
	This file contains the following examples:
	# template_loader(cvs_file)
		This function generates a Juniper configuration file using jinja2 templates.
		The code for this function is located in a file named ztpRender.py.
	
	# dhcp_loader(cvs_file, dhcp_conf_dest)
		This function generates an updated dhcpd.conf file using jinja2 templates.
		The code for this function is located in a file named ztpRender.py.

# License
  Apache License

# Author Information
  [Matthew McGeehan](http://routedo.com/)
