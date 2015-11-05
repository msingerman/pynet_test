#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse

cisco_file = 'cisco_ipsec.txt'

cisco_cfg = CiscoConfParse(cisco_file)
cryptos = cisco_cfg.find_objects_w_child(parentspec=r'crypto map CRYPTO', childspec=r'pfs group2')
print "\nCrypto Maps using PFS group2:"
for entry in cryptos:
    print "  {0}".format(entry.text)
print
