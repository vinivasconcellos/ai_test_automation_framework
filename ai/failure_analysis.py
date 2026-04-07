from utils.api_client import get_client

def analyze_failure(feature_description, error_log):
    client = get_client()

    prompt = f"""
    You are a senior QA engineer.

    Feature:
    {feature_description}

    Error:
    {error_log}

    Provide:
    1. Root cause analysis
    2. Debugging steps
    3. Suggested test improvements
    4. Risk assessment
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile", #groq
        #model="gpt-4o-mini", #openai
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    feature_description = """
    User can connect their smartphone via Bluetooth to the infotainment system 
    and play music through the car speakers.
    """

    error_log = """
    Bluetooth connection failed after pairing. Device appears connected but no audio is transmitted.
    """

    print("\nFailure Analysis:\n")
    print(analyze_failure(feature_description, error_log))