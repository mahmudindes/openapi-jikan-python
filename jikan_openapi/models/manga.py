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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from jikan_openapi.models.daterange import Daterange
from jikan_openapi.models.mal_url import MalUrl
from jikan_openapi.models.manga_images import MangaImages
from jikan_openapi.models.title import Title
from typing import Optional, Set
from typing_extensions import Self

class Manga(BaseModel):
    """
    Manga Resource
    """ # noqa: E501
    mal_id: Optional[StrictInt] = Field(default=None, description="MyAnimeList ID")
    url: Optional[StrictStr] = Field(default=None, description="MyAnimeList URL")
    images: Optional[MangaImages] = None
    approved: Optional[StrictBool] = Field(default=None, description="Whether the entry is pending approval on MAL or not")
    titles: Optional[List[Title]] = Field(default=None, description="All Titles")
    title: Optional[StrictStr] = Field(default=None, description="Title")
    title_english: Optional[StrictStr] = Field(default=None, description="English Title")
    title_japanese: Optional[StrictStr] = Field(default=None, description="Japanese Title")
    type: Optional[StrictStr] = Field(default=None, description="Manga Type")
    chapters: Optional[StrictInt] = Field(default=None, description="Chapter count")
    volumes: Optional[StrictInt] = Field(default=None, description="Volume count")
    status: Optional[StrictStr] = Field(default=None, description="Publishing status")
    publishing: Optional[StrictBool] = Field(default=None, description="Publishing boolean")
    published: Optional[Daterange] = None
    score: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Score")
    scored_by: Optional[StrictInt] = Field(default=None, description="Number of users")
    rank: Optional[StrictInt] = Field(default=None, description="Ranking")
    popularity: Optional[StrictInt] = Field(default=None, description="Popularity")
    members: Optional[StrictInt] = Field(default=None, description="Number of users who have added this entry to their list")
    favorites: Optional[StrictInt] = Field(default=None, description="Number of users who have favorited this entry")
    synopsis: Optional[StrictStr] = Field(default=None, description="Synopsis")
    background: Optional[StrictStr] = Field(default=None, description="Background")
    authors: Optional[List[MalUrl]] = None
    serializations: Optional[List[MalUrl]] = None
    genres: Optional[List[MalUrl]] = None
    explicit_genres: Optional[List[MalUrl]] = None
    themes: Optional[List[MalUrl]] = None
    demographics: Optional[List[MalUrl]] = None
    __properties: ClassVar[List[str]] = ["mal_id", "url", "images", "approved", "titles", "title", "title_english", "title_japanese", "type", "chapters", "volumes", "status", "publishing", "published", "score", "scored_by", "rank", "popularity", "members", "favorites", "synopsis", "background", "authors", "serializations", "genres", "explicit_genres", "themes", "demographics"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Manga', 'Novel', 'Light Novel', 'One-shot', 'Doujinshi', 'Manhua', 'Manhwa', 'OEL']):
            raise ValueError("must be one of enum values ('Manga', 'Novel', 'Light Novel', 'One-shot', 'Doujinshi', 'Manhua', 'Manhwa', 'OEL')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Finished', 'Publishing', 'On Hiatus', 'Discontinued', 'Not yet published']):
            raise ValueError("must be one of enum values ('Finished', 'Publishing', 'On Hiatus', 'Discontinued', 'Not yet published')")
        return value

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
        """Create an instance of Manga from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in titles (list)
        _items = []
        if self.titles:
            for _item in self.titles:
                if _item:
                    _items.append(_item.to_dict())
            _dict['titles'] = _items
        # override the default output from pydantic by calling `to_dict()` of published
        if self.published:
            _dict['published'] = self.published.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in authors (list)
        _items = []
        if self.authors:
            for _item in self.authors:
                if _item:
                    _items.append(_item.to_dict())
            _dict['authors'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in serializations (list)
        _items = []
        if self.serializations:
            for _item in self.serializations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['serializations'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in genres (list)
        _items = []
        if self.genres:
            for _item in self.genres:
                if _item:
                    _items.append(_item.to_dict())
            _dict['genres'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in explicit_genres (list)
        _items = []
        if self.explicit_genres:
            for _item in self.explicit_genres:
                if _item:
                    _items.append(_item.to_dict())
            _dict['explicit_genres'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in themes (list)
        _items = []
        if self.themes:
            for _item in self.themes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['themes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in demographics (list)
        _items = []
        if self.demographics:
            for _item in self.demographics:
                if _item:
                    _items.append(_item.to_dict())
            _dict['demographics'] = _items
        # set to None if title_english (nullable) is None
        # and model_fields_set contains the field
        if self.title_english is None and "title_english" in self.model_fields_set:
            _dict['title_english'] = None

        # set to None if title_japanese (nullable) is None
        # and model_fields_set contains the field
        if self.title_japanese is None and "title_japanese" in self.model_fields_set:
            _dict['title_japanese'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if chapters (nullable) is None
        # and model_fields_set contains the field
        if self.chapters is None and "chapters" in self.model_fields_set:
            _dict['chapters'] = None

        # set to None if volumes (nullable) is None
        # and model_fields_set contains the field
        if self.volumes is None and "volumes" in self.model_fields_set:
            _dict['volumes'] = None

        # set to None if score (nullable) is None
        # and model_fields_set contains the field
        if self.score is None and "score" in self.model_fields_set:
            _dict['score'] = None

        # set to None if scored_by (nullable) is None
        # and model_fields_set contains the field
        if self.scored_by is None and "scored_by" in self.model_fields_set:
            _dict['scored_by'] = None

        # set to None if rank (nullable) is None
        # and model_fields_set contains the field
        if self.rank is None and "rank" in self.model_fields_set:
            _dict['rank'] = None

        # set to None if popularity (nullable) is None
        # and model_fields_set contains the field
        if self.popularity is None and "popularity" in self.model_fields_set:
            _dict['popularity'] = None

        # set to None if members (nullable) is None
        # and model_fields_set contains the field
        if self.members is None and "members" in self.model_fields_set:
            _dict['members'] = None

        # set to None if favorites (nullable) is None
        # and model_fields_set contains the field
        if self.favorites is None and "favorites" in self.model_fields_set:
            _dict['favorites'] = None

        # set to None if synopsis (nullable) is None
        # and model_fields_set contains the field
        if self.synopsis is None and "synopsis" in self.model_fields_set:
            _dict['synopsis'] = None

        # set to None if background (nullable) is None
        # and model_fields_set contains the field
        if self.background is None and "background" in self.model_fields_set:
            _dict['background'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Manga from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "mal_id": obj.get("mal_id"),
            "url": obj.get("url"),
            "images": MangaImages.from_dict(obj["images"]) if obj.get("images") is not None else None,
            "approved": obj.get("approved"),
            "titles": [Title.from_dict(_item) for _item in obj["titles"]] if obj.get("titles") is not None else None,
            "title": obj.get("title"),
            "title_english": obj.get("title_english"),
            "title_japanese": obj.get("title_japanese"),
            "type": obj.get("type"),
            "chapters": obj.get("chapters"),
            "volumes": obj.get("volumes"),
            "status": obj.get("status"),
            "publishing": obj.get("publishing"),
            "published": Daterange.from_dict(obj["published"]) if obj.get("published") is not None else None,
            "score": obj.get("score"),
            "scored_by": obj.get("scored_by"),
            "rank": obj.get("rank"),
            "popularity": obj.get("popularity"),
            "members": obj.get("members"),
            "favorites": obj.get("favorites"),
            "synopsis": obj.get("synopsis"),
            "background": obj.get("background"),
            "authors": [MalUrl.from_dict(_item) for _item in obj["authors"]] if obj.get("authors") is not None else None,
            "serializations": [MalUrl.from_dict(_item) for _item in obj["serializations"]] if obj.get("serializations") is not None else None,
            "genres": [MalUrl.from_dict(_item) for _item in obj["genres"]] if obj.get("genres") is not None else None,
            "explicit_genres": [MalUrl.from_dict(_item) for _item in obj["explicit_genres"]] if obj.get("explicit_genres") is not None else None,
            "themes": [MalUrl.from_dict(_item) for _item in obj["themes"]] if obj.get("themes") is not None else None,
            "demographics": [MalUrl.from_dict(_item) for _item in obj["demographics"]] if obj.get("demographics") is not None else None
        })
        return _obj


