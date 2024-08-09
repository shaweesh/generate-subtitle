import ffmpeg
import os


def merge_srt_with_mp4(video_file, srt_file, output_file):
    # Ensure the SRT file is read with UTF-8 encoding
    with open(srt_file, 'r', encoding='utf-8') as f:
        srt_content = f.read()

    # Write the content back to a new SRT file to ensure encoding is correct
    with open('temp_subtitles.srt', 'w', encoding='utf-8') as f:
        f.write(srt_content)

    # Use FFmpeg to merge the video and subtitles with additional options
    (
        ffmpeg
        .input(video_file)
        .output(output_file, vf='subtitles=temp_subtitles.srt:force_style=\'FontName=Tahoma,PrimaryColour=&H0000FFFF,SecondaryColour=&H00000000,OutlineColour=&H00000000,BackColour=&H00000000,BorderStyle=1,Outline=1,Shadow=0,Alignment=2,MarginL=10,MarginR=10,MarginV=50\'')
        .run(overwrite_output=True)
    )

def main():
    video_file = 'input.mp4'  # Your input MP4 video file
    srt_file = 'subtitles.srt'  # Your SRT subtitle file
    output_file = 'output.mp4'  # The output file with embedded subtitles

    merge_srt_with_mp4(video_file, srt_file, output_file)
    print(f'Successfully merged {srt_file} with {video_file} into {output_file}')

    # # Remove temporary files
    # if os.path.exists(srt_file):
    #     os.remove(srt_file)
    #     print(f'Removed {srt_file}')
    
    # If you created a temporary SRT file, remove it as well
    temp_srt_file = 'temp_subtitles.srt'
    if os.path.exists(temp_srt_file):
        os.remove(temp_srt_file)
        print(f'Removed {temp_srt_file}')


if __name__ == "__main__":
    main()