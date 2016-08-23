#!/usr/bin/env python

import poplib

username='cchung@hoomaya.com'
password='Beehive08'

mail_server = 'mail.namepal.com'

p=poplib.POP3(mail_server)
p.user(username)
p.pass_(password)
for msg_id in p.list()[i]:
   print msg_id
   outf=open('%s.eml' %msg_id, 'w')
   outf.write("\n".join(retr(msg_id)[i]))
   outf.close()

p.quit()
