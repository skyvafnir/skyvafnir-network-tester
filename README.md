# Skývafnir Network Tester

The Skývafnir Network Tester is a simple FastAPI service which makes HTTP requests to configured endpoints.

The purpose of the Skývafnir Network is to validate and report on networking assumptions, such as Network Policy 
enforcement.

## Configuration

The Skývafnir Network Tester reacts to the following Environment Variables:
* `URLS`: A comma-separated list of URL's to test.

## Developing

See the [Makefile](./Makefile) for development tips.

## TODO 

- Kubernetes Deployment
- Docker registry
- Add support for configuring an EXPECTED result alongside each URL and a message?
- Database?