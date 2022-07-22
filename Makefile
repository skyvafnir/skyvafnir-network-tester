
build:
	@docker build -t skyvafnir-infra-test .

shell:
	@docker run -it skyvafnir-infra-test bash

up:
	@docker run -p 8000:8000 skyvafnir-infra-test