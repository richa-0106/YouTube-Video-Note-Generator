import ollama

def summarize(transcript):

    prompt = f"""
    Convert the following video transcript into clean, structured notes.

    Format:
    - Use headings
    - Use bullet points
    - Keep it concise
    - Highlight key concepts

    Transcript:
    {transcript}
    """

    response = ollama.chat(
        model="mistral",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response["message"]["content"]