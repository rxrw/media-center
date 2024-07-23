# media-center
## Full-featured media center in docker
This project is a full-featured media center in docker. It is based on the following components:
- [Emby](https://emby.media/) or [Plex](https://www.plex.tv/) for media server
- [Radarr](https://radarr.video/) for movie management
- [Sonarr](https://sonarr.tv/) for TV show management
- [Lidarr](https://lidarr.audio/) for music management
- [Prowlarr](https://prowlarr.com/) for indexer management
- [Flexget](https://flexget.com/) for torrent management
- Jellyseerr or [Overseerr](https://overseerr.dev/) for requesting media
- Qbittorrent and Transmission for downloading torrents
- [Bazarr](https://www.bazarr.media/) for subtitles
- [Searcharr](https://github.com/toddrob99/searcharr) for telegram tool

## Installation
1. Clone this repository
2. Create a `.env` file in the root directory of the repository:
    ```bash
    cp .env.example .env
    ```
3. Modify the `.env` file to your needs
4. Start the media center:
    ```bash
      make
    ```
   This will only start indexers and downloaders.
5. To start emby:
    ```bash
      make emby
    ```
6. To start plex:
    ```bash
      make plex
    ```
   
## Usage
- Emby: [http://localhost:8096](http://localhost:8096)
- Plex: [http://localhost:32400](http://localhost:32400)
- Radarr: [http://localhost:7878](http://localhost:7878)
- Sonarr: [http://localhost:8989](http://localhost:8989)
- Lidarr: [http://localhost:8686](http://localhost:8686)
- Prowlarr: [http://localhost:9696](http://localhost:9696)
- Flexget: [http://localhost:5050](http://localhost:5050)
- Overseerr: [http://localhost:5055](http://localhost:5055)
- Bazarr: [http://localhost:6767](http://localhost:6767)