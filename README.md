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

## Usage
1. Download the RAR file
2. Extract the RAR file anywhere
3. Run `DeadAsDisco-SyncTool.exe`
4. Drop any audio file onto the app (MP3, OGG, WAV, FLAC, M4A)
5. Copy BPM, Beat Offset, and Start Time into Dead as Disco's Advanced Editor

## Notice
Some antivirus engines (especially heuristic-based scanners such as VirusTotal aggregators) may flag packaged Python executables as “suspicious” or “generic malware.”
This is a known false positive pattern caused by bundling tools like PyInstaller and embedded assets.

## Verification
You can verify the safety of this project by:
1. Reviewing the source code in this repository
2. Running the Python script directly (dead_as_disco_sync.py)
3. Observing that all execution is local (127.0.0.1 only)
