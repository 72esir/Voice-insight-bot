from handlers.requests_handler import send_req_to_DS

async def processing_transcribation(transcribation) -> str:
    prompt = ("You are an expert in speech analysis and semantic linguistics. Analyze the following transcription of speech in Russian. Your task is to briefly but essentially describe:"
    "The main idea (what exactly the person is saying, without general words);"
    "The purpose of the statement (why is he saying this — to complain, describe, justify, etc.);"
    "Emotional state (in one or two words);"
    "The presence of a hidden meaning or subtext (if any);"
    "Evaluate the sincerity of the statement (sincerely / with irony / with sarcasm / unclear)."
    "The answer should be IN RUSSIAN LANGUAGE, concise and as specific as possible. Do not write introductions or repeat the transcription text. Just give me 5 points of analysis.")

    final_prompt = f"{prompt} Here is the transcription: {transcribation}"
    resp = send_req_to_DS(final_prompt)

    return resp
