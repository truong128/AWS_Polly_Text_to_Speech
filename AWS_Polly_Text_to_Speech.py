import boto3
from contextlib import closing

def text_to_speech(text, output_file, voice_id="Matthew", engine="standard"):
    """
    Convert text to speech using Amazon Polly and save to an audio file
    
    Parameters:
    - text: The text to convert to speech
    - output_file: Path to save the audio file (should end in .mp3)
    - voice_id: The voice to use (default: Matthew)
    - engine: The engine type (standard or neural)
    """
    
    # Create a client using boto3
    session = boto3.Session(region_name='us-east-1')
    polly = session.client('polly')
    
    try:
        # Request speech synthesis
        response = polly.synthesize_speech(
            Text=text,
            OutputFormat='mp3',
            VoiceId=voice_id,
            Engine=engine
        )
        
        # Save the audio stream to file
        if "AudioStream" in response:
            with closing(response["AudioStream"]) as stream:
                with open(output_file, "wb") as file:
                    file.write(stream.read())
                    print(f"Audio content saved to {output_file}")
                    
    except Exception as e:
        print(f"Error: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Sample text to convert
    text = """
    Hello! This is a test of Amazon Polly text to speech conversion.
    You can input any text here and it will be converted to speech.
    """
    
    # Output file path
    output_file = "Matthew_output_speech.mp3"
    
    # Convert text to speech
    text_to_speech(
        text=text,
        output_file=output_file,
        voice_id="Matthew",  # You can change to other voices like Matthew, Salli, etc.
        engine="standard"     # Use 'standard' for non-neural voices
    )
