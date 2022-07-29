VERSION := $(shell cat VERSION)
GIT_SHA := $(shell git rev-parse --short HEAD)
DOCKER_REPO := "skyvafnir/skyvafnir-network-test"
NAMESPACE ?= "skyvafnir-network-test"
CMD_HELM_TEMPLATE = (helm template -name $(NAMESPACE) deploy/skyvafnir-network-test)
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

k8s.template:
	@$(call CMD_HELM_TEMPLATE)

k8s.install:
	@$(call CMD_HELM_TEMPLATE) | kubectl apply -n $(NAMESPACE) -f -

k8s.uninstall:
	@$(call CMD_HELM_TEMPLATE) | kubectl delete -n $(NAMESPACE) -f -



run: docker.run  # docker run
shell: docker.shell  # open shell in docker contaienr
build: docker.build  # docker build
up: k8s.install  # Render helm template and apply resulting YAML to current k8s context.
down: k8s.uninstall
# build and push
release: docker.build docker.push