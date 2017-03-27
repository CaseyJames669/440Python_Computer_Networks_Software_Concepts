# Help from: http://www.voidynullness.net/blog/2013/07/25/gmail-email-with-python-via-imap/

# The first example includes a screenshot from my phone showing an email
# that shows google has actually BLOCKED the email. So, we know we're
# hitting the IMAP exchange.

#First step is to create an IMAP4 instance, preferably the SSL variant for security, 
#connected to the Gmail server at imap.gmail.com:
import sys
import imaplib
import getpass
import email
import datetime

M = imaplib.IMAP4_SSL('imap.gmail.com')

# with the mailbox seleted, we can now get the email within it.

def process_mailbox(M):
  rv, data = M.search(None, "ALL")
  if rv != 'OK':
      print("No messages found!")
      return

  for num in data[0].split():
      rv, data = M.fetch(num, '(RFC822)')
      if rv != 'OK':
          print("ERROR getting message", num)
          return

      msg = email.message_from_string(data[0][1])
      print('Message %s: %s' % (num, msg['Subject']))
      print('Raw Date:', msg['Date'])
      date_tuple = email.utils.parsedate_tz(msg['Date'])
      if date_tuple:
          local_date = datetime.datetime.fromtimestamp(
              email.utils.mktime_tz(date_tuple))
          print("Local Date:", \
              local_date.strftime("%a, %d %b %Y %H:%M:%S"))

#Next we can attempt to login. If the login fails, 
#an exception of type imaplib.IMAP4.error: will be raised:

try:
    M.login('caseybladow2@gmail.com', getpass.getpass())
except imaplib.IMAP4.error:
    print("LOGIN FAILED!!! ")
    # ... exit or deal with failure...

# If the login is successful, we can now do IMAPy things with out IMAP4 object. Most methods
# of IMAP4 return a tuple where the first element is the return status of the operation
# (usually 'OK' for success), and the second element will be either a strin or tuple with
# data from the operation.

# For example, to get a list of mailboxes on the server, we call list():

rv, mailboxes = M.list()
if rv == 'OK':
    print("Mailboxes:")
    print(mailboxes)

# With Gmail, that will return a list of labels, To open one of the mailboxes/labels, call
# select():

rv, data = M.select("INBOX")
if rv == 'OK':
    print("Processing mailbox...\n")
    process_mailbox(M) # ... do something with emails, see below ...
    M.close()
M.logout()

