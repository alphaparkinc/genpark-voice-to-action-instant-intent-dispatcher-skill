from client import VoiceToActionInstantIntentDispatcherClient

def main():
    client = VoiceToActionInstantIntentDispatcherClient()
    transcript = "Schedule a team sync tomorrow at 10 AM for 30 minutes"
    res = client.dispatch_voice_action(transcript, ["Google_Calendar", "Slack"])
    print(f"Action: {res['dispatched_action']}")
    print(f"Status: {res['execution_status']}")
    print("Parameters:", res["payload_parameters"])

if __name__ == "__main__":
    main()
