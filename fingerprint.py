#!/usr/bin/env python

import platform

class OSType(object):

   def __getattr__(self, attr):
	if attr == "osx":
		return "osx"
	elif attr =="rhel":
		return "rhel"
	elif attr =="ubuntu":
		return "ubuntu"
	elif attr=="fbsd":
		return "FreeBSD"
	elif attr=="sun":
		return "SunOS"
	else:
		return "unknown"

   def linuxType(self):
	if platform.dist()[1] == self.rhel:
		return self.rhel
	elif platform.uname()[1] == self.ubu:
		return self.ubu
	else:
		return self.unknown_linux

   def queryOS(self):
	if platform.system() == "Darwin":
		return self.osx
	elif platform.system() == "Linux":
		return self.linuxType()
	elif platform.system() == self.sun:
		return self.sun
	elif platform.system() == self.fbsd:
		return self.fbsd

def fingerprint():
   type = OSType()
   print type.queryOS()

if __name__ =='__main__':
   fingerprint()

