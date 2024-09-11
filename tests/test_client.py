import json
import unittest
from copy import deepcopy

import responses

from windy_webcams_api.v3.client import WindyWebcamsClient
from windy_webcams_api.v3.constants import Category, Continent, WebcamFeature
from tests.sample_responses import (
    COUNTRIES_DATA,
    REGIONS_DATA,
    WEBCAM_DATA,
    WEBCAM_LIST_DATA,
)


class WindyWebcamsClientTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.dummy_webcam_id = "dummy_webcam_id"
        self.webcam_data = deepcopy(WEBCAM_DATA)
        self.webcam_list_data = deepcopy(WEBCAM_LIST_DATA)
        self.regions_data = deepcopy(REGIONS_DATA)
        self.countries_data = deepcopy(COUNTRIES_DATA)

        self.webcam_body = json.dumps(self.webcam_data)
        self.webcam_list_body = json.dumps(self.webcam_list_data)
        self.regions_body = json.dumps(self.regions_data)
        self.countries_body = json.dumps(self.countries_data)

        self.client = WindyWebcamsClient(api_key="dummy_api_key")

    def test_single_webcam(self):
        with responses.RequestsMock(assert_all_requests_are_fired=True) as rsps:
            rsps.add(
                responses.GET,
                f"{WindyWebcamsClient.api_root}/webcams/{self.dummy_webcam_id}",
                body=self.webcam_body,
                status=200,
            )
            data = self.client.webcam(webcam_id=self.dummy_webcam_id)

        self.assertEqual(data, self.webcam_data)

    def test_single_webcam_features(self):
        expected_include = f"{WebcamFeature.urls},{WebcamFeature.images}"
        with responses.RequestsMock(assert_all_requests_are_fired=True) as rsps:
            rsps.add(
                responses.GET,
                f"{WindyWebcamsClient.api_root}/webcams/{self.dummy_webcam_id}?include={expected_include}",
                body=self.webcam_body,
                status=200,
            )
            data = self.client.webcam(
                webcam_id=self.dummy_webcam_id,
                features=[WebcamFeature.urls, WebcamFeature.images],
            )

        self.assertEqual(data, self.webcam_data)

    def test_response_not_okay(self):
        with responses.RequestsMock(assert_all_requests_are_fired=True) as rsps:
            rsps.add(
                responses.GET,
                f"{WindyWebcamsClient.api_root}/webcams/{self.dummy_webcam_id}",
                status=500,
            )
            with self.assertRaises(WindyWebcamsClient.ResponseNotOkay):
                self.client.webcam(webcam_id=self.dummy_webcam_id)

    def test_regions(self):
        with responses.RequestsMock(assert_all_requests_are_fired=True) as rsps:
            rsps.add(
                responses.GET,
                f"{WindyWebcamsClient.api_root}/regions",
                body=self.regions_body,
                status=200,
            )
            data = self.client.regions()

        self.assertEqual(data, self.regions_data)

    def test_countries(self):
        with responses.RequestsMock(assert_all_requests_are_fired=True) as rsps:
            rsps.add(
                responses.GET,
                f"{WindyWebcamsClient.api_root}/countries",
                body=self.countries_body,
                status=200,
            )
            data = self.client.countries()

        self.assertEqual(data, self.countries_data)

    def test_webcam_list(self):
        expected_query_params = f"limit=1&offset=10&regions=AT.04&continents={Continent.EU}&webcamIds=1249044448&categories={Category.city}&include={WebcamFeature.location}"
        with responses.RequestsMock(assert_all_requests_are_fired=True) as rsps:
            rsps.add(
                responses.GET,
                f"{WindyWebcamsClient.api_root}/webcams?{expected_query_params}",
                body=self.webcam_list_body,
                status=200,
            )
            data = self.client.webcams(
                limit=1,
                offset=10,
                regions=["AT.04"],
                webcam_ids=["1249044448"],
                categories=[Category.city],
                features=[WebcamFeature.location],
                continents=[Continent.EU],
            )
        self.assertEqual(data, self.webcam_list_data)
