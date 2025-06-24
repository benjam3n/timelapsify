#!/usr/bin/env python3
import json
import sys
import subprocess
import tempfile
import os

def read_message():
    raw_length = sys.stdin.buffer.read(4)
    if len(raw_length) == 0:
        return None
    message_length = int.from_bytes(raw_length, byteorder='little')
    message = sys.stdin.buffer.read(message_length).decode('utf-8')
    return json.loads(message)

def send_message(message):
    encoded = json.dumps(message).encode('utf-8')
    sys.stdout.buffer.write(len(encoded).to_bytes(4, byteorder='little'))
    sys.stdout.buffer.write(encoded)
    sys.stdout.flush()


def process(url, speed):
    with tempfile.TemporaryDirectory() as tmpdir:
        video_path = os.path.join(tmpdir, 'video.mp4')
        cmd = ['yt-dlp', '-f', 'best', '-o', video_path, url]
        subprocess.run(cmd, check=True)
        output = os.path.join(tmpdir, 'timelapse.mp4')
        ffmpeg_cmd = [
            'ffmpeg', '-y', '-i', video_path,
            '-filter:v', f'setpts=PTS/{speed}',
            '-an', output
        ]
        subprocess.run(ffmpeg_cmd, check=True)
        subprocess.Popen(['xdg-open', output])

if __name__ == '__main__':
    msg = read_message()
    if not msg:
        sys.exit(0)
    url = msg.get('url')
    speed = msg.get('speed', '2')
    try:
        process(url, speed)
        send_message({'status': 'ok'})
    except Exception as e:
        send_message({'status': 'error', 'message': str(e)})
