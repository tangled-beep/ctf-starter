import requests
import os
from bs4 import BeautifulSoup

def main():
	print("Starting ctf-starter...")
	IP = input("Enter the IP address of this mf box:")
	r = requests.get(f'http://{IP}')
	if r.status_code == 200:
		print("Found a HTTP server, diggin for a wordlist now...")
		soup = BeautifulSoup(r.content, 'html.parser')
		text = soup.get_text().strip()
		f = open(f"{IP}words.txt", "x")
		f.write(text)
		f.close()
		print("created a text file!")

#	else:
#		print("tryin' an HTTPS server instead")
#		r = requests.get(f'https://{IP}')
#		if r.status_code == 200:
#			print("Found a https server, diggin for a wordlist now...")
#			text = r.text
#			f = open(f"{IP}words.txt", "x")
#			f.write(text)
#			f.close()
#			print("created a text file!")
#		else:
#			print("no web servers found for wordlists")




if __name__ == '__main__':
	main()