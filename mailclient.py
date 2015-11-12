#
# mail client using SMTP
# 11.Nov.2015 nagisa
#
# how to send mail with smtp
# 1. connect server
# 2. send HELO command
# 3. send address whose mail from with 'MAIL FROM' command
# 4. send address whose mail to with 'RCPT To' command
# 5. send header and message with 'DATA\r\n' command
#    end of message is '.'
# 6. close connection with ''
#

import socket
import sys

# create socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to server
server = 'mail.uni-wuppertal.de'
address = (server, 25)
print >> sys.stderr, 'connecting to %s port %s' % address
try:
  sock.connect(address)
except socket.error, msg:
  print >>sys.stderr, msg
  sys.exit(1)

print '--- connection succeed ----'

recv = sock.recv(1024)
print recv
if recv[:3] != '220':
  print 'connection error'
  sys.exit(1)

print '--- say HELO ---'

# send greeting to server
# and wait apply from server
greeting = 'HELO Bob\r\n'
try:
  sock.send(greeting)
except socket.error, msg:
  print >>sys.stderr, msg
  sys.exit(1)
recv_greeting = sock.recv(1024)
print recv_greeting
if recv_greeting[:3] != '250':
  print 'greeting error'

#print '--- starttls connection ---'
#try:
#  sock.send('STARTTLS\r\n')
#except socket.error, msg:
#  print >>sys.stderr, msg
#  sys.exit(1)
#recv_starttls = sock.recv(1024)
#print recv_starttls

print '--- send sender address ---'

# send address whose sender
sender_address = '1530235@uni-wuppertal.de'
try:
  sock.send('MAIL FROM:<' + sender_address + '>\r\n')
except socket.error, msg:
  print >>sys.stderr, msg
  sys.exit(1)
recv_sender = sock.recv(1024)
print recv_sender
if recv_sender[:3] != '250':
  print 'sender address error'

print '--- send receiver address ---'

# send address whose receive person
receiver_address = raw_input('raw_input receiver address:')
sock.send('RCPT TO:<' + receiver_address + '>\r\n')
recv_receiver = sock.recv(1024)
print recv_receiver
if recv_receiver[:3] != '250':
  print 'receiver address error'

print '--- send ---'

# send header and message
data = 'DATA\r\n'
sock.send(data)
recv_data = sock.recv(1024)
print recv_data
if recv_data[:3] != '250':
  print 'data error'

message = raw_input("raw_input message:")
sock.send(message + '\r\n.\r\n')
recv_message = sock.recv(1024)
print recv_message
if recv_message[:3] != '250':
  print 'message error'

print '--- close connection ---'

# close connection
sock.send('QUIT\r\n')
recv_quit = sock.recv(1024)
print recv_quit
if recv_quit[:3] != '221':
  print 'quit error'

sock.close()

