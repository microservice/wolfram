# _Wolfram_ OMG Microservice

[![Open Microservice Guide](https://img.shields.io/badge/OMG%20Enabled-👍-green.svg?)](https://microservice.guide)

Wolfram is a unique engine for computing answers and providing knowledge. It works by using its vast store of expert-level knowledge and algorithms to automatically answer questions, do analysis and generate reports.

## Direct usage in [Storyscript](https://storyscript.io/):

##### Answer
```coffee
wolfram answer query: "What's eight times ten?"
wolfram answer query: "What's eight times ten?" units: "imperial"  # units defaults to "metric"
```

## Obtaining Wolfram credentials

* [Wolfram AppID](https://products.wolframalpha.com/short-answers-api/documentation/)

Curious to [learn more](https://docs.storyscript.io/)?

✨🍰✨

## Usage with [OMG CLI](https://www.npmjs.com/package/omg)

##### Answer
```shell
$ omg run answer -a query=<QUERY> -a units=<UNITS> -e WOLFRAM_APP_ID=<WOLFRAM_APP_ID>
```

**Note**: The OMG CLI requires [Docker](https://docs.docker.com/install/) to be installed.

## License
[MIT License](https://github.com/omg-services/wolfram/blob/master/LICENSE).
