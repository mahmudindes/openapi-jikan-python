# coding: utf-8

# flake8: noqa
"""
    Jikan API

    [Jikan](https://jikan.moe) is an **Unofficial** MyAnimeList API. It scrapes the website to satisfy the need for a complete API - which MyAnimeList lacks.  # Information  ⚡ Jikan is powered by its awesome backers - 🙏 [Become a backer](https://www.patreon.com/jikan)  ## Rate Limiting  | Duration | Requests | |----|----| | Daily | **Unlimited** | | Per Minute | 60 requests | | Per Second | 3 requests |  Note: It's still possible to get rate limited from MyAnimeList.net instead.   ## JSON Notes - Any property (except arrays or objects) whose value does not exist or is undetermined, will be `null`. - Any array or object property whose value does not exist or is undetermined, will be empty. - Any `score` property whose value does not exist or is undetermined, will be `0`. - All dates and timestamps are returned in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) format and in UTC timezone  ## Caching By **CACHING**, we refer to the data parsed from MyAnimeList which is stored temporarily on our servers to provide better API performance.  All requests are cached for **24 hours**.  The following response headers will detail cache information.  | Header | Remarks | | ---- | ---- | | `Expires` | Cache expiry date | | `Last-Modified` | Cache set date | | `X-Request-Fingerprint` | Unique request fingerprint (only for cachable requests, not queries) |   Note: `X-Request-Fingerprint` will only be available on single resource requests and their child endpoints. e.g `/anime/1`, `/anime/1/relations`. They won't be available on pages which perform queries, like /anime, or /top/anime, etc.  ## Allowed HTTP(s) requests  **Jikan REST API does not provide authenticated requests for MyAnimeList.** This means you can not use it to update your anime/manga list. Only GET requests are supported which return READ-ONLY data.  ## HTTP Responses  All error responses are accompanied by a JSON Error response.  | Exception | HTTP Status | Remarks | | ---- | ---- | ---- | | N/A | `200 - OK` | The request was successful | | N/A | `304 - Not Modified` | You have the latest data (Cache Validation response) | | `BadRequestException`,`ValidationException` | `400 - Bad Request` | You've made an invalid request. Recheck documentation | | `BadResponseException` | `404 - Not Found` | The resource was not found or MyAnimeList responded with a `404` | | `BadRequestException` | `405 - Method Not Allowed` | Requested Method is not supported for resource. Only `GET` requests are allowed | | `RateLimitException` | `429 - Too Many Request` | You are being rate limited by Jikan or MyAnimeList is rate-limiting our servers (specified in the error response) | | `UpstreamException`,`ParserException`,etc. | `500 - Internal Server Error` | Something didn't work. Try again later. If you see an error response with a `report_url` URL, please click on it to open an auto-generated GitHub issue | | `ServiceUnavailableException` | `503 - Service Unavailable` | In most cases this is intentionally done if the service is down for maintenance. |  ## JSON Error Response  ```json  {      \"status\": 500,      \"type\": \"InternalException\",      \"message\": \"Exception Message\",      \"error\": \"Exception Trace\",      \"report_url\": \"https://github.com...\"   } ```  | Property | Remarks | | ---- | ---- | | `status` | Returned HTTP Status Code | | `type` | Thrown Exception | | `message` | Human-readable error message | | `error` | Error response and trace from the API | | `report_url` | Clicking this would redirect you to a generated GitHub issue |   ## Cache Validation  - All requests return a `ETag` header which is an MD5 hash of the response - You can use this hash to verify if there's new or updated content by suppliying it as the value for the `If-None-Match` in your next request header - You will get a HTTP `304 - Not Modified` response if the content has not changed - If the content has changed, you'll get a HTTP `200 - OK` response with the updated JSON response  ![Cache Validation](https://i.imgur.com/925ozVn.png 'Cache Validation')  ## Disclaimer  - Jikan is not affiliated with MyAnimeList.net. - Jikan is a free, open-source API. Please use it responsibly.  ----  By using the API, you are agreeing to Jikan's [terms of use](https://jikan.moe/terms) policy.  [v3 Documentation](https://jikan.docs.apiary.io/) - [Wrappers/SDKs](https://github.com/jikan-me/jikan#wrappers) - [Report an issue](https://github.com/jikan-me/jikan-rest/issues/new) - [Host your own server](https://github.com/jikan-me/jikan-rest)

    The version of the OpenAPI document: 4.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from jikan_openapi.models.anime import Anime
from jikan_openapi.models.anime_characters import AnimeCharacters
from jikan_openapi.models.anime_characters_data_inner import AnimeCharactersDataInner
from jikan_openapi.models.anime_characters_data_inner_character import AnimeCharactersDataInnerCharacter
from jikan_openapi.models.anime_characters_data_inner_voice_actors_inner import AnimeCharactersDataInnerVoiceActorsInner
from jikan_openapi.models.anime_characters_data_inner_voice_actors_inner_person import AnimeCharactersDataInnerVoiceActorsInnerPerson
from jikan_openapi.models.anime_episode import AnimeEpisode
from jikan_openapi.models.anime_episodes import AnimeEpisodes
from jikan_openapi.models.anime_episodes_all_of_data import AnimeEpisodesAllOfData
from jikan_openapi.models.anime_full import AnimeFull
from jikan_openapi.models.anime_full_external_inner import AnimeFullExternalInner
from jikan_openapi.models.anime_full_relations_inner import AnimeFullRelationsInner
from jikan_openapi.models.anime_full_theme import AnimeFullTheme
from jikan_openapi.models.anime_images import AnimeImages
from jikan_openapi.models.anime_images_jpg import AnimeImagesJpg
from jikan_openapi.models.anime_images_webp import AnimeImagesWebp
from jikan_openapi.models.anime_meta import AnimeMeta
from jikan_openapi.models.anime_news import AnimeNews
from jikan_openapi.models.anime_relations import AnimeRelations
from jikan_openapi.models.anime_review import AnimeReview
from jikan_openapi.models.anime_reviews import AnimeReviews
from jikan_openapi.models.anime_reviews_all_of_data import AnimeReviewsAllOfData
from jikan_openapi.models.anime_search import AnimeSearch
from jikan_openapi.models.anime_search_query_orderby import AnimeSearchQueryOrderby
from jikan_openapi.models.anime_search_query_rating import AnimeSearchQueryRating
from jikan_openapi.models.anime_search_query_status import AnimeSearchQueryStatus
from jikan_openapi.models.anime_search_query_type import AnimeSearchQueryType
from jikan_openapi.models.anime_staff import AnimeStaff
from jikan_openapi.models.anime_staff_data_inner import AnimeStaffDataInner
from jikan_openapi.models.anime_staff_data_inner_person import AnimeStaffDataInnerPerson
from jikan_openapi.models.anime_statistics import AnimeStatistics
from jikan_openapi.models.anime_statistics_data import AnimeStatisticsData
from jikan_openapi.models.anime_statistics_data_scores_inner import AnimeStatisticsDataScoresInner
from jikan_openapi.models.anime_themes import AnimeThemes
from jikan_openapi.models.anime_userupdates import AnimeUserupdates
from jikan_openapi.models.anime_userupdates_all_of_data import AnimeUserupdatesAllOfData
from jikan_openapi.models.anime_videos import AnimeVideos
from jikan_openapi.models.anime_videos_data import AnimeVideosData
from jikan_openapi.models.anime_videos_data_episodes_inner import AnimeVideosDataEpisodesInner
from jikan_openapi.models.anime_videos_data_music_videos_inner import AnimeVideosDataMusicVideosInner
from jikan_openapi.models.anime_videos_data_music_videos_inner_meta import AnimeVideosDataMusicVideosInnerMeta
from jikan_openapi.models.anime_videos_data_promo_inner import AnimeVideosDataPromoInner
from jikan_openapi.models.anime_videos_episodes import AnimeVideosEpisodes
from jikan_openapi.models.anime_videos_episodes_all_of_data import AnimeVideosEpisodesAllOfData
from jikan_openapi.models.broadcast import Broadcast
from jikan_openapi.models.character import Character
from jikan_openapi.models.character_anime import CharacterAnime
from jikan_openapi.models.character_anime_data_inner import CharacterAnimeDataInner
from jikan_openapi.models.character_full import CharacterFull
from jikan_openapi.models.character_full_manga_inner import CharacterFullMangaInner
from jikan_openapi.models.character_full_voices_inner import CharacterFullVoicesInner
from jikan_openapi.models.character_images import CharacterImages
from jikan_openapi.models.character_images_jpg import CharacterImagesJpg
from jikan_openapi.models.character_images_webp import CharacterImagesWebp
from jikan_openapi.models.character_manga import CharacterManga
from jikan_openapi.models.character_meta import CharacterMeta
from jikan_openapi.models.character_pictures import CharacterPictures
from jikan_openapi.models.character_pictures_data_inner import CharacterPicturesDataInner
from jikan_openapi.models.character_voice_actors import CharacterVoiceActors
from jikan_openapi.models.characters_search import CharactersSearch
from jikan_openapi.models.characters_search_query_orderby import CharactersSearchQueryOrderby
from jikan_openapi.models.club import Club
from jikan_openapi.models.club_member import ClubMember
from jikan_openapi.models.club_member_data_inner import ClubMemberDataInner
from jikan_openapi.models.club_relations import ClubRelations
from jikan_openapi.models.club_relations_data import ClubRelationsData
from jikan_openapi.models.club_search_query_category import ClubSearchQueryCategory
from jikan_openapi.models.club_search_query_orderby import ClubSearchQueryOrderby
from jikan_openapi.models.club_search_query_type import ClubSearchQueryType
from jikan_openapi.models.club_staff import ClubStaff
from jikan_openapi.models.club_staff_data_inner import ClubStaffDataInner
from jikan_openapi.models.clubs_search import ClubsSearch
from jikan_openapi.models.common_images import CommonImages
from jikan_openapi.models.daterange import Daterange
from jikan_openapi.models.daterange_prop import DaterangeProp
from jikan_openapi.models.daterange_prop_from import DaterangePropFrom
from jikan_openapi.models.daterange_prop_to import DaterangePropTo
from jikan_openapi.models.entry_meta import EntryMeta
from jikan_openapi.models.entry_recommendations import EntryRecommendations
from jikan_openapi.models.external_links import ExternalLinks
from jikan_openapi.models.forum import Forum
from jikan_openapi.models.forum_data_inner import ForumDataInner
from jikan_openapi.models.forum_data_inner_last_comment import ForumDataInnerLastComment
from jikan_openapi.models.genre import Genre
from jikan_openapi.models.genre_query_filter import GenreQueryFilter
from jikan_openapi.models.genres import Genres
from jikan_openapi.models.get_anime_by_id200_response import GetAnimeById200Response
from jikan_openapi.models.get_anime_episode_by_id200_response import GetAnimeEpisodeById200Response
from jikan_openapi.models.get_anime_full_by_id200_response import GetAnimeFullById200Response
from jikan_openapi.models.get_anime_relations200_response import GetAnimeRelations200Response
from jikan_openapi.models.get_character_by_id200_response import GetCharacterById200Response
from jikan_openapi.models.get_character_full_by_id200_response import GetCharacterFullById200Response
from jikan_openapi.models.get_club_members200_response import GetClubMembers200Response
from jikan_openapi.models.get_clubs_by_id200_response import GetClubsById200Response
from jikan_openapi.models.get_manga_by_id200_response import GetMangaById200Response
from jikan_openapi.models.get_manga_full_by_id200_response import GetMangaFullById200Response
from jikan_openapi.models.get_person_by_id200_response import GetPersonById200Response
from jikan_openapi.models.get_person_full_by_id200_response import GetPersonFullById200Response
from jikan_openapi.models.get_producer_by_id200_response import GetProducerById200Response
from jikan_openapi.models.get_producer_full_by_id200_response import GetProducerFullById200Response
from jikan_openapi.models.get_random_users200_response import GetRandomUsers200Response
from jikan_openapi.models.get_top_reviews200_response import GetTopReviews200Response
from jikan_openapi.models.get_top_reviews200_response_data import GetTopReviews200ResponseData
from jikan_openapi.models.get_top_reviews200_response_data_all_of_data_inner import GetTopReviews200ResponseDataAllOfDataInner
from jikan_openapi.models.get_top_reviews200_response_data_all_of_data_inner_any_of import GetTopReviews200ResponseDataAllOfDataInnerAnyOf
from jikan_openapi.models.get_top_reviews200_response_data_all_of_data_inner_any_of1 import GetTopReviews200ResponseDataAllOfDataInnerAnyOf1
from jikan_openapi.models.get_user_by_id200_response import GetUserById200Response
from jikan_openapi.models.get_user_favorites200_response import GetUserFavorites200Response
from jikan_openapi.models.get_user_full_profile200_response import GetUserFullProfile200Response
from jikan_openapi.models.history import History
from jikan_openapi.models.magazine import Magazine
from jikan_openapi.models.magazines import Magazines
from jikan_openapi.models.magazines_query_orderby import MagazinesQueryOrderby
from jikan_openapi.models.mal_url import MalUrl
from jikan_openapi.models.mal_url2 import MalUrl2
from jikan_openapi.models.manga import Manga
from jikan_openapi.models.manga_characters import MangaCharacters
from jikan_openapi.models.manga_characters_data_inner import MangaCharactersDataInner
from jikan_openapi.models.manga_full import MangaFull
from jikan_openapi.models.manga_images import MangaImages
from jikan_openapi.models.manga_meta import MangaMeta
from jikan_openapi.models.manga_news import MangaNews
from jikan_openapi.models.manga_pictures import MangaPictures
from jikan_openapi.models.manga_review import MangaReview
from jikan_openapi.models.manga_review_reactions import MangaReviewReactions
from jikan_openapi.models.manga_reviews import MangaReviews
from jikan_openapi.models.manga_reviews_all_of_data import MangaReviewsAllOfData
from jikan_openapi.models.manga_search import MangaSearch
from jikan_openapi.models.manga_search_query_orderby import MangaSearchQueryOrderby
from jikan_openapi.models.manga_search_query_status import MangaSearchQueryStatus
from jikan_openapi.models.manga_search_query_type import MangaSearchQueryType
from jikan_openapi.models.manga_statistics import MangaStatistics
from jikan_openapi.models.manga_statistics_data import MangaStatisticsData
from jikan_openapi.models.manga_userupdates import MangaUserupdates
from jikan_openapi.models.manga_userupdates_all_of_data import MangaUserupdatesAllOfData
from jikan_openapi.models.moreinfo import Moreinfo
from jikan_openapi.models.moreinfo_data import MoreinfoData
from jikan_openapi.models.news import News
from jikan_openapi.models.news_data_inner import NewsDataInner
from jikan_openapi.models.pagination import Pagination
from jikan_openapi.models.pagination_pagination import PaginationPagination
from jikan_openapi.models.pagination_plus import PaginationPlus
from jikan_openapi.models.pagination_plus_pagination import PaginationPlusPagination
from jikan_openapi.models.pagination_plus_pagination_items import PaginationPlusPaginationItems
from jikan_openapi.models.people_images import PeopleImages
from jikan_openapi.models.people_search import PeopleSearch
from jikan_openapi.models.people_search_all_of_data import PeopleSearchAllOfData
from jikan_openapi.models.people_search_query_orderby import PeopleSearchQueryOrderby
from jikan_openapi.models.person import Person
from jikan_openapi.models.person_anime import PersonAnime
from jikan_openapi.models.person_anime_data_inner import PersonAnimeDataInner
from jikan_openapi.models.person_full import PersonFull
from jikan_openapi.models.person_full_manga_inner import PersonFullMangaInner
from jikan_openapi.models.person_full_voices_inner import PersonFullVoicesInner
from jikan_openapi.models.person_manga import PersonManga
from jikan_openapi.models.person_meta import PersonMeta
from jikan_openapi.models.person_pictures import PersonPictures
from jikan_openapi.models.person_voice_acting_roles import PersonVoiceActingRoles
from jikan_openapi.models.pictures import Pictures
from jikan_openapi.models.pictures_data_inner import PicturesDataInner
from jikan_openapi.models.pictures_variants import PicturesVariants
from jikan_openapi.models.pictures_variants_data_inner import PicturesVariantsDataInner
from jikan_openapi.models.producer import Producer
from jikan_openapi.models.producer_full import ProducerFull
from jikan_openapi.models.producers import Producers
from jikan_openapi.models.producers_query_orderby import ProducersQueryOrderby
from jikan_openapi.models.random import Random
from jikan_openapi.models.random_data_inner import RandomDataInner
from jikan_openapi.models.recommendations import Recommendations
from jikan_openapi.models.recommendations_all_of_data import RecommendationsAllOfData
from jikan_openapi.models.recommendations_all_of_entry import RecommendationsAllOfEntry
from jikan_openapi.models.relation import Relation
from jikan_openapi.models.reviews_collection import ReviewsCollection
from jikan_openapi.models.reviews_collection_data_inner import ReviewsCollectionDataInner
from jikan_openapi.models.schedules import Schedules
from jikan_openapi.models.search_query_sort import SearchQuerySort
from jikan_openapi.models.seasons import Seasons
from jikan_openapi.models.seasons_data_inner import SeasonsDataInner
from jikan_openapi.models.streaming_links import StreamingLinks
from jikan_openapi.models.title import Title
from jikan_openapi.models.top_anime_filter import TopAnimeFilter
from jikan_openapi.models.top_manga_filter import TopMangaFilter
from jikan_openapi.models.top_reviews_type_enum import TopReviewsTypeEnum
from jikan_openapi.models.trailer import Trailer
from jikan_openapi.models.trailer_base import TrailerBase
from jikan_openapi.models.trailer_images import TrailerImages
from jikan_openapi.models.trailer_images_images import TrailerImagesImages
from jikan_openapi.models.user_about import UserAbout
from jikan_openapi.models.user_about_data_inner import UserAboutDataInner
from jikan_openapi.models.user_anime_list_status_filter import UserAnimeListStatusFilter
from jikan_openapi.models.user_by_id import UserById
from jikan_openapi.models.user_clubs import UserClubs
from jikan_openapi.models.user_clubs_all_of_data import UserClubsAllOfData
from jikan_openapi.models.user_favorites import UserFavorites
from jikan_openapi.models.user_favorites_anime_inner import UserFavoritesAnimeInner
from jikan_openapi.models.user_favorites_characters_inner import UserFavoritesCharactersInner
from jikan_openapi.models.user_favorites_manga_inner import UserFavoritesMangaInner
from jikan_openapi.models.user_friends import UserFriends
from jikan_openapi.models.user_friends_all_of_data import UserFriendsAllOfData
from jikan_openapi.models.user_history import UserHistory
from jikan_openapi.models.user_images import UserImages
from jikan_openapi.models.user_images_jpg import UserImagesJpg
from jikan_openapi.models.user_images_webp import UserImagesWebp
from jikan_openapi.models.user_manga_list_status_filter import UserMangaListStatusFilter
from jikan_openapi.models.user_meta import UserMeta
from jikan_openapi.models.user_profile import UserProfile
from jikan_openapi.models.user_profile_full import UserProfileFull
from jikan_openapi.models.user_profile_full_statistics import UserProfileFullStatistics
from jikan_openapi.models.user_profile_full_statistics_anime import UserProfileFullStatisticsAnime
from jikan_openapi.models.user_profile_full_statistics_manga import UserProfileFullStatisticsManga
from jikan_openapi.models.user_statistics import UserStatistics
from jikan_openapi.models.user_updates import UserUpdates
from jikan_openapi.models.user_updates_data import UserUpdatesData
from jikan_openapi.models.user_updates_data_anime_inner import UserUpdatesDataAnimeInner
from jikan_openapi.models.user_updates_data_manga_inner import UserUpdatesDataMangaInner
from jikan_openapi.models.users_search import UsersSearch
from jikan_openapi.models.users_search_all_of_data import UsersSearchAllOfData
from jikan_openapi.models.users_search_query_gender import UsersSearchQueryGender
from jikan_openapi.models.users_temp import UsersTemp
from jikan_openapi.models.users_temp_data_inner import UsersTempDataInner
from jikan_openapi.models.users_temp_data_inner_anime_stats import UsersTempDataInnerAnimeStats
from jikan_openapi.models.users_temp_data_inner_favorites import UsersTempDataInnerFavorites
from jikan_openapi.models.users_temp_data_inner_images import UsersTempDataInnerImages
from jikan_openapi.models.users_temp_data_inner_images_jpg import UsersTempDataInnerImagesJpg
from jikan_openapi.models.users_temp_data_inner_images_webp import UsersTempDataInnerImagesWebp
from jikan_openapi.models.users_temp_data_inner_manga_stats import UsersTempDataInnerMangaStats
from jikan_openapi.models.watch_episodes import WatchEpisodes
from jikan_openapi.models.watch_episodes_all_of_data import WatchEpisodesAllOfData
from jikan_openapi.models.watch_episodes_all_of_episodes import WatchEpisodesAllOfEpisodes
from jikan_openapi.models.watch_promos import WatchPromos
