import pexpect
import os

PASS = os.environ.get("PASS_SERVER")
NAME = os.environ.get("NAME_SERVER")
if NAME == None :
    NAME = "server"

print("Launching Script for GEN-REQ server")
child = pexpect.spawn("/etc/openvpn/EasyRSA-3.0.7/easyrsa gen-req server")
print("Child spawned")
child.expect("pass phrase")
print("PASS Expected")
child.send(PASS+"\n")
print("Send PASS")
child.expect("pass phrase")
print("PASS Expected")
child.send(PASS+"\n")
print("Send PASS")
child.expect("Common Name")
print("Expect NAME")
child.send(NAME+"\n")
print("Send NAME")
child.expect(pexpect.EOF)
print("END of Script")
child.close()
print("Close Child")
