#!/bin/bash
set -e

# Install dependencies
if ! command -v ffmpeg >/dev/null 2>&1; then
    echo "Installing ffmpeg..."
    sudo apt-get update && sudo apt-get install -y ffmpeg
fi

if ! command -v yt-dlp >/dev/null 2>&1; then
    echo "Installing yt-dlp via pip..."
    python3 -m pip install --user --upgrade yt-dlp
fi

# Install host script
TARGET="/usr/local/bin/timelapsify.py"
echo "Copying timelapsify.py to $TARGET"
sudo install -m 755 timelapsify.py "$TARGET"

# Native messaging manifest
MANIFEST_DIR="$HOME/.mozilla/native-messaging-hosts"
MANIFEST="$MANIFEST_DIR/timelapsify.json"
echo "Creating native messaging manifest at $MANIFEST"
mkdir -p "$MANIFEST_DIR"
cat > "$MANIFEST" <<MANIFEST
{
  "name": "timelapsify",
  "description": "Timelapse helper",
  "path": "$TARGET",
  "type": "stdio",
  "allowed_extensions": ["timelapsify@example.com"]
}
MANIFEST

chmod 644 "$MANIFEST"

cat <<DONE
Installation complete.
Load the 'extension/' directory in Firefox as a temporary add-on.
DONE
