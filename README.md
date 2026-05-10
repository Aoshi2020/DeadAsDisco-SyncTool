# DeadAsDisco-SyncTool
A desktop tool for accurately syncing songs in Dead as Disco. Drop in any audio file and it auto-detects BPM, Beat Offset, and Start Time.
Auto-detects BPM, Beat Offset, and Start Time for any song.
Built for Dead as Disco mapping.

## Features
- Auto BPM detection with candidate list
- Auto beat offset calculation
- Start Time detection (trim silent intros)
- BPM Sections for variable-tempo songs
- Real waveform viewer with beat grid overlay
- Fully offline — no internet required after install

## Usage
1. Run `BUILD.bat` to build the exe (requires Python + internet for first build)
2. Drop any audio file onto the app (MP3, OGG, WAV, FLAC, M4A)
3. Copy BPM, Beat Offset, and Start Time into Dead as Disco's Advanced Editor
