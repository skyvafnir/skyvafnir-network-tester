VERSION := $(shell cat VERSION)
GIT_SHA := $(shell git rev-parse --short HEAD)
DOCKER_REPO := "skyvafnir/skyvafnir-network-test"

run: docker.run
shell: docker.shell
build:docker.build


# build and push
release: docker.build docker.push

docker.build:
	@docker build -t skyvafnir-infra-test .

docker.shell:
	@docker run -it skyvafnir-infra-test bash

docker.run:
	@docker run -p 8000:8000 skyvafnir-infra-test

docker.build:
	docker build --build-arg VERSION=$(VERSION)-local --build-arg GIT_SHA=$(GIT_SHA) -t $(DOCKER_REPO):$(VERSION) .

docker.push:
	@echo "## Pushing $(DOCKER_REPO):$(VERSION)"
	@docker push $(DOCKER_REPO):$(VERSION)
	@echo "## Pushing $(DOCKER_REPO):latest"
	@docker tag "$(DOCKER_REPO):$(VERSION)" "$(DOCKER_REPO):latest"
	@docker push "$(DOCKER_REPO):latest"