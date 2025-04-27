from twilio.rest import Client
import keys
import time  # Optional: To add delay between messages

# Initialize the Twilio client
client = Client(keys.account_sid, keys.auth_token)

# List of all verified numbers (ensure these numbers are added in Twilio Console)
verified_numbers = [keys.my_phone_number, keys.another_verified_number]  # Add more if needed

# Send the message to all verified numbers
for number in verified_numbers:
    message = client.messages.create(
        body="Today you attended class",
        from_=keys.twilio_number,
        to=number
    )
    print(f"Message sent to {number}: {message.sid}")
    
    time.sleep(2)  # Optional: Prevents rate-limiting issues by adding a 2-second delay

