document.getElementById('speedRange').addEventListener('input', function(e) {
  document.getElementById('speedLabel').textContent = `Speed: ${e.target.value}x`;
});

document.getElementById('timelapseBtn').addEventListener('click', async () => {
  const [tab] = await browser.tabs.query({ active: true, currentWindow: true });
  if (!tab || !tab.url.includes('youtube.com/watch')) {
    document.getElementById('status').textContent = 'Not a YouTube video.';
    return;
  }
  const speed = document.getElementById('speedRange').value;
  document.getElementById('status').textContent = 'Processing...';
  try {
    await browser.runtime.sendNativeMessage('timelapsify', { url: tab.url, speed: speed });
    document.getElementById('status').textContent = 'Sent to host application.';
  } catch (err) {
    document.getElementById('status').textContent = 'Failed: ' + err;
  }
});
