
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: python mcb.pyw save <keyword> - Saves clipboard to keyword.
#        python mcb.pyw <keyword> - Loads keyword to clipboard.
#        python mcb.pyw list - Loads all keywords to clipboard.

import shelve, pyperclip, sys

mcbshelf=shelve.open('mcb')

# Save clipboard content
#lists keyword and load content

if len(sys.argv) == 3 and sys.argv[1].lower()=='save':
	mcbshelf[sys.argv[2]]=pyperclip.paste()
elif len(sys.argv)==2:
	if sys.argv[1].lower=='list':
		pyperclip.copy(str(list(mcbshelf.keys())))
	elif sys.argv[1] in mcbshelf:
		pyperclip.copy(mcbshelf[sys.argv[1]])

mcbshelf.close()


