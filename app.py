from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/voicemail-webhook', methods=['POST'])
def receive_voicemail():
    data = request.json
    print("Webhook received!")

    # Get caller number and audio URL
    caller = data.get("caller_id")
    audio_url = data.get("call_recording_link")  # Confirm the correct key in your test
    print(f"From: {caller}")
    print(f"Audio link: {audio_url}")

    # Download audio file
    if audio_url:
        audio_data = requests.get(audio_url).content
        filename = f"voicemail_{caller.replace('+', '')}.wav"
        with open(filename, "wb") as f:
            f.write(audio_data)
        print(f" Voicemail saved as {filename}")

    return "OK", 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9999, debug=True)
    print("Server is running on port 9999") # Make sure to run this script with Flask installed and the server accessible
    # You can test this by sending a POST request to http://localhost:9999/voicemail-webhook with a JSON body
