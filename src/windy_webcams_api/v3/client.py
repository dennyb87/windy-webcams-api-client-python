from typing import Iterable, Optional

import requests

from windy_webcams_api.v3.constants import Category, Continent, WebcamFeature


class WindyWebcamsClient:
    api_root: str = "https://api.windy.com/webcams/api/v3"

    class ResponseNotOkay(Exception):
        pass

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.headers = {"x-windy-api-key": self.api_key}

    @classmethod
    def _request(cls, url: str, **kwargs) -> dict:
        response = requests.get(url=url, **kwargs)
        if not response.ok:
            raise cls.ResponseNotOkay(f"{response.status_code}: {response.text}")
        return response.json()

    def webcam(
        self, webcam_id: str, features: Optional[Iterable[WebcamFeature]] = None
    ) -> dict:
        query = f"?include={','.join(features)}" if features else ""
        endpoint = f"{self.api_root}/webcams/{webcam_id}{query}"
        return self._request(url=endpoint, headers=self.headers)

    def regions(self):
        endpoint = f"{self.api_root}/regions"
        return self._request(url=endpoint, headers=self.headers)

    def countries(self):
        endpoint = f"{self.api_root}/countries"
        return self._request(url=endpoint, headers=self.headers)

    def webcams(
        self,
        limit: int = 10,
        offset: int = 0,
        regions: Optional[Iterable[str]] = None,
        continents: Optional[Iterable[Continent]] = None,
        webcam_ids: Iterable[str] = None,
        categories: Optional[Iterable[Category]] = None,
        features: Optional[Iterable[WebcamFeature]] = None,
    ) -> dict:
        query_params = dict(limit=limit, offset=offset)
        if regions:
            query_params.update(dict(regions=",".join(regions)))
        if continents:
            query_params.update(dict(continents=",".join(continents)))
        if webcam_ids:
            query_params.update(dict(webcamIds=",".join(webcam_ids)))
        if categories:
            query_params.update(dict(categories=",".join(categories)))
        if features:
            query_params.update(dict(include=",".join(features)))
        query = "&".join([f"{key}={value}" for key, value in query_params.items()])
        endpoint = f"{self.api_root}/webcams?{query}"
        return self._request(url=endpoint, headers=self.headers)
