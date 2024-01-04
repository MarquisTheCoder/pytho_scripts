

import pexpect

password = "user password"

possible_passwords = [
		"s"
]

try:
	child = pexpect.spawn("sudo -S /bin/bash -c 'echo hello world'")
	child.expect("Password:")
	child.sendline(password)
	child.interact()
except pexpect.TIMEOUT:
	print("password was not succesfully cracked")
	exit(-1)
