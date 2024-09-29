# coding: utf-8

"""
    Jikan API

    [Jikan](https://jikan.moe) is an **Unofficial** MyAnimeList API. It scrapes the website to satisfy the need for a complete API - which MyAnimeList lacks.  # Information  ⚡ Jikan is powered by its awesome backers - 🙏 [Become a backer](https://www.patreon.com/jikan)  ## Rate Limiting  | Duration | Requests | |----|----| | Daily | **Unlimited** | | Per Minute | 60 requests | | Per Second | 3 requests |  Note: It's still possible to get rate limited from MyAnimeList.net instead.   ## JSON Notes - Any property (except arrays or objects) whose value does not exist or is undetermined, will be `null`. - Any array or object property whose value does not exist or is undetermined, will be empty. - Any `score` property whose value does not exist or is undetermined, will be `0`. - All dates and timestamps are returned in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) format and in UTC timezone  ## Caching By **CACHING**, we refer to the data parsed from MyAnimeList which is stored temporarily on our servers to provide better API performance.  All requests are cached for **24 hours**.  The following response headers will detail cache information.  | Header | Remarks | | ---- | ---- | | `Expires` | Cache expiry date | | `Last-Modified` | Cache set date | | `X-Request-Fingerprint` | Unique request fingerprint (only for cachable requests, not queries) |   Note: `X-Request-Fingerprint` will only be available on single resource requests and their child endpoints. e.g `/anime/1`, `/anime/1/relations`. They won't be available on pages which perform queries, like /anime, or /top/anime, etc.  ## Allowed HTTP(s) requests  **Jikan REST API does not provide authenticated requests for MyAnimeList.** This means you can not use it to update your anime/manga list. Only GET requests are supported which return READ-ONLY data.  ## HTTP Responses  All error responses are accompanied by a JSON Error response.  | Exception | HTTP Status | Remarks | | ---- | ---- | ---- | | N/A | `200 - OK` | The request was successful | | N/A | `304 - Not Modified` | You have the latest data (Cache Validation response) | | `BadRequestException`,`ValidationException` | `400 - Bad Request` | You've made an invalid request. Recheck documentation | | `BadResponseException` | `404 - Not Found` | The resource was not found or MyAnimeList responded with a `404` | | `BadRequestException` | `405 - Method Not Allowed` | Requested Method is not supported for resource. Only `GET` requests are allowed | | `RateLimitException` | `429 - Too Many Request` | You are being rate limited by Jikan or MyAnimeList is rate-limiting our servers (specified in the error response) | | `UpstreamException`,`ParserException`,etc. | `500 - Internal Server Error` | Something didn't work. Try again later. If you see an error response with a `report_url` URL, please click on it to open an auto-generated GitHub issue | | `ServiceUnavailableException` | `503 - Service Unavailable` | In most cases this is intentionally done if the service is down for maintenance. |  ## JSON Error Response  ```json  {      \"status\": 500,      \"type\": \"InternalException\",      \"message\": \"Exception Message\",      \"error\": \"Exception Trace\",      \"report_url\": \"https://github.com...\"   } ```  | Property | Remarks | | ---- | ---- | | `status` | Returned HTTP Status Code | | `type` | Thrown Exception | | `message` | Human-readable error message | | `error` | Error response and trace from the API | | `report_url` | Clicking this would redirect you to a generated GitHub issue |   ## Cache Validation  - All requests return a `ETag` header which is an MD5 hash of the response - You can use this hash to verify if there's new or updated content by suppliying it as the value for the `If-None-Match` in your next request header - You will get a HTTP `304 - Not Modified` response if the content has not changed - If the content has changed, you'll get a HTTP `200 - OK` response with the updated JSON response  ![Cache Validation](https://i.imgur.com/925ozVn.png 'Cache Validation')  ## Disclaimer  - Jikan is not affiliated with MyAnimeList.net. - Jikan is a free, open-source API. Please use it responsibly.  ----  By using the API, you are agreeing to Jikan's [terms of use](https://jikan.moe/terms) policy.  [v3 Documentation](https://jikan.docs.apiary.io/) - [Wrappers/SDKs](https://github.com/jikan-me/jikan#wrappers) - [Report an issue](https://github.com/jikan-me/jikan-rest/issues/new) - [Host your own server](https://github.com/jikan-me/jikan-rest)

    The version of the OpenAPI document: 4.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from jikan_openapi.models.anime_full_external_inner import AnimeFullExternalInner
from jikan_openapi.models.user_images import UserImages
from jikan_openapi.models.user_profile_full_statistics import UserProfileFullStatistics
from typing import Optional, Set
from typing_extensions import Self

class UserProfileFull(BaseModel):
    """
    Transform the resource into an array.
    """ # noqa: E501
    mal_id: Optional[StrictInt] = Field(default=None, description="MyAnimeList ID")
    username: Optional[StrictStr] = Field(default=None, description="MyAnimeList Username")
    url: Optional[StrictStr] = Field(default=None, description="MyAnimeList URL")
    images: Optional[UserImages] = None
    last_online: Optional[StrictStr] = Field(default=None, description="Last Online Date ISO8601")
    gender: Optional[StrictStr] = Field(default=None, description="User Gender")
    birthday: Optional[StrictStr] = Field(default=None, description="Birthday Date ISO8601")
    location: Optional[StrictStr] = Field(default=None, description="Location")
    joined: Optional[StrictStr] = Field(default=None, description="Joined Date ISO8601")
    statistics: Optional[UserProfileFullStatistics] = None
    external: Optional[List[AnimeFullExternalInner]] = None
    __properties: ClassVar[List[str]] = ["mal_id", "username", "url", "images", "last_online", "gender", "birthday", "location", "joined", "statistics", "external"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of UserProfileFull from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of images
        if self.images:
            _dict['images'] = self.images.to_dict()
        # override the default output from pydantic by calling `to_dict()` of statistics
        if self.statistics:
            _dict['statistics'] = self.statistics.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in external (list)
        _items = []
        if self.external:
            for _item in self.external:
                if _item:
                    _items.append(_item.to_dict())
            _dict['external'] = _items
        # set to None if mal_id (nullable) is None
        # and model_fields_set contains the field
        if self.mal_id is None and "mal_id" in self.model_fields_set:
            _dict['mal_id'] = None

        # set to None if last_online (nullable) is None
        # and model_fields_set contains the field
        if self.last_online is None and "last_online" in self.model_fields_set:
            _dict['last_online'] = None

        # set to None if gender (nullable) is None
        # and model_fields_set contains the field
        if self.gender is None and "gender" in self.model_fields_set:
            _dict['gender'] = None

        # set to None if birthday (nullable) is None
        # and model_fields_set contains the field
        if self.birthday is None and "birthday" in self.model_fields_set:
            _dict['birthday'] = None

        # set to None if location (nullable) is None
        # and model_fields_set contains the field
        if self.location is None and "location" in self.model_fields_set:
            _dict['location'] = None

        # set to None if joined (nullable) is None
        # and model_fields_set contains the field
        if self.joined is None and "joined" in self.model_fields_set:
            _dict['joined'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UserProfileFull from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "mal_id": obj.get("mal_id"),
            "username": obj.get("username"),
            "url": obj.get("url"),
            "images": UserImages.from_dict(obj["images"]) if obj.get("images") is not None else None,
            "last_online": obj.get("last_online"),
            "gender": obj.get("gender"),
            "birthday": obj.get("birthday"),
            "location": obj.get("location"),
            "joined": obj.get("joined"),
            "statistics": UserProfileFullStatistics.from_dict(obj["statistics"]) if obj.get("statistics") is not None else None,
            "external": [AnimeFullExternalInner.from_dict(_item) for _item in obj["external"]] if obj.get("external") is not None else None
        })
        return _obj


