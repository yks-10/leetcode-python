import pywhatkit as kit
import datetime

# Replace these values with the recipient's phone number and your message
recipient_phone_number = "+916383133966"  # Replace with recipient's phone number in E.164 format
message = "Hello, this is a test message from Python!"

# Get the current time
now = datetime.datetime.now()
hours = now.hour
minutes = now.minute + 1  # Schedule the message 1 minute from now

# Send the WhatsApp message

kit.sendwhatmsg(recipient_phone_number, message, hours, minutes)
