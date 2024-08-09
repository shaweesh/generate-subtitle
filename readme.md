## README for First Use

### Project Title: Video Subtitle Merger

### Description

This project allows you to merge subtitles into a video file. It uses Python and FFmpeg for processing video files.

### Prerequisites

Before you begin, ensure you have the following installed:

1. **Python**: Version 3.6 or higher.
2. **FFmpeg**: Make sure FFmpeg is installed and added to your system PATH. You can download it from [FFmpeg's official site](https://ffmpeg.org/download.html).

### Setup Instructions

1. **Clone the Repository**:
   Open your terminal or command prompt and clone the repository:

   ```bash
   git clone https://github.com/shaweesh/generate-subtitle
   cd generate-subtitle
   ```

2. **Create a Virtual Environment**:
   Create a virtual environment to manage dependencies:

   ```bash
   python -m venv env
   ```

3. **Activate the Virtual Environment**:

   - On Windows:
     ```bash
     env\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source env/bin/activate
     ```

4. **Install Required Packages**:
   Install the necessary Python packages:

   ```bash
   pip install ffmpeg-python faster-whisper
   ```

5. **Prepare Your Files**:
   - Place your video file (e.g., `input.mp4`) in the project directory.
   - Create or prepare your subtitle file (e.g., `subtitles.srt`) in the same directory.

### Usage Instructions

1. **Run the Script**:
   Execute the script to merge the subtitles:

   ```bash
   python merge_srt.py
   ```

2. **Output**:
   The output video will be saved as `output.mp4` in the same directory.

### Notes

- Ensure that your subtitle file is correctly formatted in SRT format and encoded in UTF-8.

---

## README for Subsequent Use

### Project Title: Video Subtitle Merger

### Description

This project allows you to merge subtitles into a video file. It uses Python and FFmpeg for processing video files.

### Prerequisites

Ensure you have completed the initial setup and have the environment prepared.

### Usage Instructions

1. **Activate the Virtual Environment**:

   - On Windows:
     ```bash
     env\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source env/bin/activate
     ```

2. **Prepare Your Files**:

   - Place your new video file (e.g., `input.mp4`) in the project directory.
   - Create or prepare your new subtitle file (e.g., `subtitles.srt`) in the same directory.

3. **Run the Script**:
   Execute the script to merge the subtitles:

   ```bash
   python merge_srt.py
   ```

4. **Output**:
   The output video will be saved as `output.mp4` in the same directory.

### Notes

- Ensure that your subtitle file is correctly formatted in SRT format and encoded in UTF-8.

### Troubleshooting

- If you encounter issues with the subtitles not appearing, check the formatting of your SRT file and ensure that FFmpeg is properly installed and accessible from your command line.
