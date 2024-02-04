# YouTube Transcription Flask API

This project provides a simple Flask API to fetch and serve transcriptions for YouTube videos using the `youtube-transcript-api` library. It's designed to be a starting point for integrating YouTube transcriptions into web applications or for further development into more complex systems.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Ensure you have Conda installed on your system. If not, follow the instructions at [Conda Installation](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) to set it up.

### Installing

```bash
git clone https://github.com/IvanAquino/yt-transcription-api.git
```

1. Create and activate a Conda environment

```bash
conda create --name myflaskenv python=3.12
conda activate myflaskenv
```

2. Install the requirements

Inside the activated environment, install the required packages using:

```bash
pip install -r requirements.txt
```

3. Start the Flask application

```bash
flask run
```

### Usage

Example url

**http://127.0.0.1:5000/transcript?video_id=U9mJuUkhUzk&languages=en**

