from ciscoconfparse import CiscoConfParse

ipsec_cfg = CiscoConfParse("ipsec.cfg")


crypto_pki = ipsec_cfg.find_objects(r"crypto map CRYPTO")

#Because it is a list we need to set it as such
crypto_pki = crypto_pki[0]
##

#crypto_pki.all_children


for i in crypto_pki.children:
    for child in crypto_pki.all_children:
	print child.text
    print i.text


#crypto_pki = crypto_pki[0]
#for child in crypto_pki.all_children:
#    print child.text

