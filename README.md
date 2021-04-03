# Calls Music 1 — [pytgcalls](https://github.com/MarshalX/tgcalls)-based group call bot with queue and multiple chat support

## Requirements

- FFmpeg
- Python 3.7+

## Deployment

### Config

Copy `example.env` to `.env` and fill it with your credentials.

### The good way

1. Install Python requirements:
   ```bash
   pip install -U -r requirements.txt
   ```
2. Run:
   ```bash
   python main.py
   ```

### Docker

1. Build:
   ```bash
   docker build -t musicplayer .
   ```
2. Run:
   ```bash
   docker run --env-file .env musicplayer
   ```

### Heroku

[Click here](https://heroku.com/deploy?template=https://github.com/xrrmli/kntlmusik)

## Commands

| Command | Description                                          |
| ------- | ---------------------------------------------------- |
| /play   | play the replied audio file or YouTube video         |
| /pause  | pause the audio stream                               |
| /resume | resume the audio stream                              |
| /skip   | skip the current audio stream                        |
| /mute   | mute the userbot                                     |
| /unmute | unmute the userbot                                   |
| /stop   | clear the queue and remove the userbot from the call |

## License

### GNU Affero General Public License v3.0

[Read more](http://www.gnu.org/licenses/#AGPL)
