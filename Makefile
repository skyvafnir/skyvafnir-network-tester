VERSION := $(shell cat VERSION)
GIT_SHA := $(shell git rev-parse --short HEAD)
DOCKER_REPO := "skyvafnir/skyvafnir-network-test"

docker.shell:
	@docker run -it $(DOCKER_REPO):$(VERSION) bash

docker.run:
	@docker run -p 8000:8000 $(DOCKER_REPO):$(VERSION)

docker.build:
	docker build --build-arg VERSION=$(VERSION)-local --build-arg GIT_SHA=$(GIT_SHA) -t $(DOCKER_REPO):$(VERSION) .

docker.push:
	@echo "## Pushing $(DOCKER_REPO):$(VERSION)"
	@docker push $(DOCKER_REPO):$(VERSION)
	@echo "## Pushing $(DOCKER_REPO):latest"
	@docker tag "$(DOCKER_REPO):$(VERSION)" "$(DOCKER_REPO):latest"
	@docker push "$(DOCKER_REPO):latest"

k8s.install:
	@helm template -name skyvafnir-network-test deploy/skyvafnir-network-test | kubectl apply -n skyvafnir -f -


run: docker.run  # docker run
shell: docker.shell  # open shell in docker contaienr
build: docker.build  # docker build
up: k8s.install  # Render helm template and apply resulting YAML to current k8s context.

# build and push
release: docker.build docker.push