#! /Users/pravar_ag/Python_Work/env1

import sys

PASSWORDS={'email':'F7minlBDDuvMJuxESSKHFhTxFtjVB6','blog':'VmALvQyKAxiVH5G8v01if1MLZF3sdt','luggage':'12345'}

if len(sys.argv)<1:
	print('Usage: python password.py [account] - copy account password')
	sys.exit()

account=sys.argv[1]

