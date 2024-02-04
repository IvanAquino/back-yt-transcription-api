from flask import Flask, jsonify, request
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)

@app.route('/transcript', methods=['GET'])
def get_transcript():
    video_id = request.args.get('video_id')
    languagesString = request.args.get('languages') if request.args.get('languages') else ['en']
    languagesArray = languagesString.split(',')
    print(languagesArray)

    if not video_id:
        return jsonify({'error': 'Missing video_id parameter'}), 400
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languagesArray)
        return jsonify(transcript)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

