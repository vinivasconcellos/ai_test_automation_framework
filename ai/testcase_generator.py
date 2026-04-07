from utils.api_client import get_client

def generate_test_cases(feature_description):
    client = get_client()

    prompt = f"""
    You are a senior QA engineer.

    Generate detailed test cases for the following feature:

    {feature_description}

    Include:
    - Positive scenarios
    - Negative scenarios
    - Edge cases
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

    print("\nGenerated Test Cases:\n")
    print(generate_test_cases(feature_description))