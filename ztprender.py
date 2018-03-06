"""
This function generates configuration files using jinja2 templates
"""

import os
import csv
from shutil import copyfile
import jinja2

def template_loader(cvs_file, conf_dest):
    """
    This function generates a Juniper configuration file using jinja2 templates.

    cvs_file = Location of the file containing variables to use with the jinja2 template.
    conf_dest = Location to place generated config file.
    """

    tor_template_filename = 'template/jun_tor_template.j2'
    access_template_filename = 'template/jun_access_template.j2'

    env = jinja2.Environment(loader=jinja2.FileSystemLoader('./'))

    tor_template = env.get_template(tor_template_filename)
    wan_template = env.get_template(access_template_filename)

    for row in csv.DictReader(open(cvs_file)):
        with open(conf_dest + row['hostname'] + '.config', 'w+') as f:
            g = str(row['hostname'])
            if 'tor' in g:
                f.write(tor_template.render(row))
            else:
                f.write(wan_template.render(row))

def dhcp_loader(cvs_file, dhcp_conf_dest):
    """
    This function generates an updated dhcpd.conf file using jinja2 templates.

    cvs_file = Location of the file containing variables to use with the jinja2 template.
    dhcp_conf_dest = Location to place generated dhcpd.conf file.
    """

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
            f.write(template.render(row))

    with open(dhcp_conf_dest, 'a') as f:
        f.write('}')
