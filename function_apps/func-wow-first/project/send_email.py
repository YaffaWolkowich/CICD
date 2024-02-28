import os
import sys
import base64
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import project.download_excel
import logging
def build_email_message(recipient_email, subject, body, excel):
    logging.info(f"recipient_email - {recipient_email}")
    logging.info(f"subject - {subject}")
    logging.info(f"body - {body}")
    logging.info(f"excel - {excel}")
    if excel != None:
        logging.warn("excel is not None")
        attachment_file = project.download_excel.download_blob_excel(excel)
        attachment_file_base64 = base64.b64encode(attachment_file).decode("utf-8")
        attachment = {
            "@odata.type": "#microsoft.graph.fileAttachment",
            "name": excel,
            "contentBytes": attachment_file_base64
        }
        email_message = {
            "message": {
                "subject": subject,
                "body": {
                    "contentType": "Text",
                    "content": body,
                },
                "toRecipients": [
                    {
                        "emailAddress": {
                            "address": recipient_email
                        }
                    }
                ],
                "attachments": [
                    attachment
                ]
            }
        }
        logging.warn(f"------------------ {email_message}")
        project.download_excel.delete_blob_excel('excel',excel)
        return email_message
    else:
        logging.info("+++++++++++++++++++++++++++++++++++++++++++++++++")
        email_message = {
            "message": {
                "subject": subject,
                "body": {
                    "contentType": "Text",
                    "content": body,
                },
                "toRecipients": [
                    {
                        "emailAddress": {
                            "address": recipient_email
                        }
                    }
                ]
            }
        }
        logging.warn(f"?????????{email_message}")
        return email_message
