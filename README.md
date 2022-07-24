# Skývafnir Network Tester

The Skývafnir Network Tester is a simple FastAPI service which makes HTTP requests to configured endpoints.

The purpose of the Skývafnir Network is to validate and report on networking assumptions, such as Network Policy 
enforcement.

## Configuration

The Skývafnir Network Tester reacts to the following Environment Variable:
* `URLS`: A comma-separated list of URL's to test. This variable is exposed through the Helm chart's [values.yaml](deploy/skyvafnir-network-test/values.yaml)

## Developing

The repository contains a [Makefile](./Makefile) with some useful targets. Highlights include: 

1. Build docker image:
   ```shell
   $ make build
   ```

2. Run docker locally:
   ```shell
   $ make run
   ```

3. Apply k8s manifests to working kube context: 
   ```shell
   $ make up
   ```

# Releasing

The Skývafnir Network Tester is released via [Github Releases / Tags](https://github.com/skyvafnir/skyvafnir-network-tester/releases)

To release a new version, push a `tag` - a new version of the service will be built and pushed to Docker Hub
via Github Actions - tagged as `skyvafnir/skyvafnir-network-tester:[your new tag]`



# TODO 

- Add support for configuring an EXPECTED result alongside each URL and a message?
- Database?