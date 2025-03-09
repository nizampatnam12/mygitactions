import openai
import time

# Set your OpenAI API key here
openai.api_key = 'your-api-key'

# Function to generate text using GPT
def generate_text(prompt):
    try:
        # Call OpenAI API with the chat-based model using /v1/chat/completions
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use "gpt-4" if you want GPT-4
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},  # Optional system message to guide behavior
                {"role": "user", "content": prompt}  # User's input prompt
            ],
            max_tokens=100  # Limit the number of tokens in the response
        )
        
        # Extract and print the generated text from the response
        generated_text = response['choices'][0]['message']['content'].strip()
        print(f"Generated Text: {generated_text}")
        
    except Exception as e:
        print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    prompt = "Why sky is blue?"
    generate_text(prompt)
    time.sleep(2)  # Optional delay before the next request
