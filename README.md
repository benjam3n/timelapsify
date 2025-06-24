# Timelapsify Firefox Extension

This repository contains a minimal Firefox extension and a Python native
messaging host that downloads the current YouTube video and plays it back as a
timelapse at a selected speed (2x–50x).

## Usage

### Automatic setup

Run `./install.sh` on an Ubuntu system to install the required
dependencies and register the native messaging host automatically.

### Manual setup

1. Install `yt-dlp` and `ffmpeg` on your system.
2. Copy `timelapsify.py` somewhere on your system and create a native
   messaging host manifest pointing to it. For example on Linux:
   `~/.mozilla/native-messaging-hosts/timelapsify.json`:

```json
{
  "name": "timelapsify",
  "description": "Timelapse helper",
  "path": "/path/to/timelapsify.py",
  "type": "stdio",
  "allowed_extensions": ["timelapsify@example.com"]
}
```

3. Load the `extension/` directory as a temporary add-on in Firefox.
4. Open any YouTube video, click the extension button, choose your speed and
   press **Create Timelapse**. The video will be downloaded, processed, and
   played without sound.
