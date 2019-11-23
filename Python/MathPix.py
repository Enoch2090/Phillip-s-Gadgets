#!/usr/bin/env python

# example from https://github.com/Mathpix/api-examples/blob/master/python/mathpix.py

import os,base64,requests,json,pyperclip
from PIL import ImageGrab

env = os.environ
HOME = env.get('HOME') + "/Desktop/"

default_headers = {
	'app_id': 'YOUR_ID',
	'app_key': 'YOUR_KEY',
	'Content-type': 'application/json'
}

service = 'https://api.mathpix.com/v3/latex'


# Return the base64 encoding of an image with the given filename.
def image_uri(filename):
	image_data = open(filename, "rb").read()
	return "data:image/jpg;base64," + base64.b64encode(image_data).decode()

# Call the Mathpix service with the given arguments, headers, and timeout.
def latex(args, headers=default_headers, timeout=30):
	r = requests.post(service, data=json.dumps(args), headers=headers, timeout=timeout)
	return json.loads(r.text)

def mathpix():
	im = ImageGrab.grabclipboard()
	im.save(HOME+'screen.png','PNG')
	r = latex({
		'src': image_uri(HOME+"screen.png"),
		"ocr": ["math", "text"],
		'formats': ['latex_styled']
	})
	print(r['latex_styled'])
	pyperclip.copy(r['latex_styled'])
	os.remove("/Users/enoch/Desktop/screen.png")
if __name__ == '__main__':
	os.system("screencapture -i -c")
	mathpix()
