import ffmpeg
from faster_whisper import WhisperModel
import os

# Function to extract audio from video
def extract_audio(input_video):
    audio_file = "audio.wav"
    ffmpeg.input(input_video).output(audio_file, format='wav').run(overwrite_output=True)
    return audio_file

# Function to transcribe audio to subtitles
def transcribe_audio(audio_file):
    model = WhisperModel("large", device="cpu")  # Use a smaller model and run on CPU
    segments, _ = model.transcribe(audio_file, language='he')  # Correct language code for Hebrew
    return segments

# Function to generate SRT file from transcription
def generate_srt(segments, output_file='subtitles.srt', min_display_duration=1.0):
    with open(output_file, 'w', encoding='utf-8') as f:
        for i, segment in enumerate(segments):
            start_time = segment.start
            end_time = segment.end
            text = segment.text.strip()

            # Calculate the adjusted end time based on the minimum display duration
            adjusted_end_time = start_time + max(end_time - start_time, min_display_duration)

            # Format time in SRT format
            start_time_str = f"{int(start_time // 3600):02}:{int((start_time % 3600) // 60):02}:{int(start_time % 60):02},{int((start_time % 1) * 1000):03}"
            end_time_str = f"{int(adjusted_end_time // 3600):02}:{int((adjusted_end_time % 3600) // 60):02}:{int(adjusted_end_time % 60):02},{int((adjusted_end_time % 1) * 1000):03}"

            # Write to SRT file
            f.write(f"{i + 1}\n{start_time_str} --> {end_time_str}\n{text}\n\n")

# Main function
def main():
    input_video = "input.mp4"  # Your input video file
    audio_file = extract_audio(input_video)
    segments = transcribe_audio(audio_file)
    generate_srt(segments, min_display_duration=1.0)  # Set minimum display duration to 1 second

    
    # If you have an audio file, remove it as well (if applicable)
    audio_file = 'audio.wav'
    if os.path.exists(audio_file):
        os.remove(audio_file)
        print(f'Removed {audio_file}')

if __name__ == "__main__":
    main()