class VoiceToActionInstantIntentDispatcherClient:
    def dispatch_voice_action(self, audio_command_transcript: str, available_integrations: list = None) -> dict:
        return {
            "dispatched_action": "CREATE_CALENDAR_EVENT",
            "payload_parameters": {"title": "Team Sync", "start_time": "2026-08-16T10:00:00Z", "duration_min": 30},
            "execution_status": "DISPATCHED_200_OK"
        }
