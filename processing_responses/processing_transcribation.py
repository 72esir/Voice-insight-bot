from handlers.requests_handler import send_req_to_DS

async def processing_transcribation(transcribation) -> str:
    prompt = f"You are an expert communication analyst. Analyze the following audio transcription for tone, intent, emotional state, and any underlying meaning. Identify whether the speaker is being sincere, sarcastic, emotional, or neutral. Provide a short summary and label the tone with 1–2 descriptive words. Here is the transcription: {transcribation}"
    resp = send_req_to_DS(prompt)

    return resp
