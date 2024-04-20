# windy-webcams-api-client-python  

Simple python client for [windy webcams api](https://api.windy.com/webcams/api/v3/docs)  

## Basic usage  

Generate `api_key` [here](https://api.windy.com/keys) and instantiate the client.  

```
client = WindyWebcamsClient(api_key=api_key)
client.webcam(webcam_id="1664921834")
``` 