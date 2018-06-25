# Wolfram as a microservice

Visit the docs at http://products.wolframalpha.com/api/ for the endpoints (only the endpoints with url `api.wolframalpha`.com are supported).
You do *not* need to provide your API key via query param as it will be supplied via your environment variable.
Data will be returned as a JSON, unless result is defined as an image or string in the docs.

## Usage

```sh
omg exec wolfram -c get -a endpoint='/v2/query?input=solve+3x-7%3D11&podstate=Result__Step-by-step+solution'
```

The endpoint must be an endpoint of the `api.wolframalpha.com` domain. Ex: http://products.wolframalpha.com/show-steps-api/documentation/
