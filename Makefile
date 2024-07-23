DOCKER_COMPOSE = docker compose
DOCKER_COMPOSE_EXEC = $(DOCKER_COMPOSE) exec

.PHONY : clean all indexer downloader emby
all: indexer downloader tips

rxrw: indexer downloader plex-without-server

tips:
	echo "Tips:"
	echo "  You should start media server (Emby or Plex) after indexer and downloader. just run 'make emby' or 'make plex'"

indexer:
	echo "Starting Indexer..."
	$(DOCKER_COMPOSE) -f "docker-compose.indexer.yml" up -d

downloader:
	echo "Starting Downloader..."
	$(DOCKER_COMPOSE) -f "docker-compose.downloader.yml" up -d

emby:
	echo "Starting Emby and Overseerr..."
	$(DOCKER_COMPOSE) -f "docker-compose.emby.yml" up -d

plex:
	echo "Starting Plex..."
	$(DOCKER_COMPOSE) -f "docker-compose.plex.yml" up -d

plex-without-server:
	echo "Starting Plex without server..."
	$(DOCKER_COMPOSE) -f "docker-compose.plex.yml" up -d overseerr plextraktsync scheduler tautulli

status:
	$(DOCKER_COMPOSE) -f "docker-compose.indexer.yml" ps -a
	$(DOCKER_COMPOSE) -f "docker-compose.downloader.yml" ps -a
	$(DOCKER_COMPOSE) -f "docker-compose.emby.yml" ps -a
	$(DOCKER_COMPOSE) -f "docker-compose.plex.yml" ps -a

clean:
	$(DOCKER_COMPOSE) -f "docker-compose.downloader.yml" down
	$(DOCKER_COMPOSE) -f "docker-compose.indexer.yml" down
	$(DOCKER_COMPOSE) -f "docker-compose.emby.yml" down
	$(DOCKER_COMPOSE) -f "docker-compose.plex.yml" down
