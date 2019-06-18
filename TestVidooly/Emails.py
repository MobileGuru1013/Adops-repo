import imaplib
import email
import os

svdir = 'c:/Downloads/'

mail = imaplib.IMAP4('outlook.office365.com', port=993)
mail.login("dharmendra.mishra@neomediaworld.com", "Password2")
mail.select("Inbox")

typ, msgs = mail.search(None, '(SUBJECT "Report #160496147 : "AU report QTD date wise MediaOps" from Dhruv Sapra")')
msgs = msgs[0].split()


for emailid in msgs:
    print(emailid)
    exit()
    resp, data = mail.fetch(emailid, None)
    # mail.fetch()
    email_body = data[0][1]
    m = email.message_from_string(email_body)

    if m.get_content_maintype() != 'multipart':
        continue

    for part in m.walk():
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue

        filename = part.get_filename()
        if filename is not None:
            sv_path = os.path.join(svdir, filename)
            if not os.path.isfile(sv_path):
                print sv_path
                fp = open(sv_path, 'wb')
                fp.write(part.get_payload(decode=True))
                fp.close()