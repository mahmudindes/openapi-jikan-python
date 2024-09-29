# jikan_openapi.AnimeApi

All URIs are relative to *https://api.jikan.moe/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_anime_by_id**](AnimeApi.md#get_anime_by_id) | **GET** /anime/{id} | 
[**get_anime_characters**](AnimeApi.md#get_anime_characters) | **GET** /anime/{id}/characters | 
[**get_anime_episode_by_id**](AnimeApi.md#get_anime_episode_by_id) | **GET** /anime/{id}/episodes/{episode} | 
[**get_anime_episodes**](AnimeApi.md#get_anime_episodes) | **GET** /anime/{id}/episodes | 
[**get_anime_external**](AnimeApi.md#get_anime_external) | **GET** /anime/{id}/external | 
[**get_anime_forum**](AnimeApi.md#get_anime_forum) | **GET** /anime/{id}/forum | 
[**get_anime_full_by_id**](AnimeApi.md#get_anime_full_by_id) | **GET** /anime/{id}/full | 
[**get_anime_more_info**](AnimeApi.md#get_anime_more_info) | **GET** /anime/{id}/moreinfo | 
[**get_anime_news**](AnimeApi.md#get_anime_news) | **GET** /anime/{id}/news | 
[**get_anime_pictures**](AnimeApi.md#get_anime_pictures) | **GET** /anime/{id}/pictures | 
[**get_anime_recommendations**](AnimeApi.md#get_anime_recommendations) | **GET** /anime/{id}/recommendations | 
[**get_anime_relations**](AnimeApi.md#get_anime_relations) | **GET** /anime/{id}/relations | 
[**get_anime_reviews**](AnimeApi.md#get_anime_reviews) | **GET** /anime/{id}/reviews | 
[**get_anime_search**](AnimeApi.md#get_anime_search) | **GET** /anime | 
[**get_anime_staff**](AnimeApi.md#get_anime_staff) | **GET** /anime/{id}/staff | 
[**get_anime_statistics**](AnimeApi.md#get_anime_statistics) | **GET** /anime/{id}/statistics | 
[**get_anime_streaming**](AnimeApi.md#get_anime_streaming) | **GET** /anime/{id}/streaming | 
[**get_anime_themes**](AnimeApi.md#get_anime_themes) | **GET** /anime/{id}/themes | 
[**get_anime_user_updates**](AnimeApi.md#get_anime_user_updates) | **GET** /anime/{id}/userupdates | 
[**get_anime_videos**](AnimeApi.md#get_anime_videos) | **GET** /anime/{id}/videos | 
[**get_anime_videos_episodes**](AnimeApi.md#get_anime_videos_episodes) | **GET** /anime/{id}/videos/episodes | 


# **get_anime_by_id**
> GetAnimeById200Response get_anime_by_id(id)



### Example


```python
import jikan_openapi
from jikan_openapi.models.get_anime_by_id200_response import GetAnimeById200Response
from jikan_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.jikan.moe/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = jikan_openapi.Configuration(
    host = "https://api.jikan.moe/v4"
)


# Enter a context with an instance of the API client
with jikan_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jikan_openapi.AnimeApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_anime_by_id(id)
        print("The response of AnimeApi->get_anime_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnimeApi->get_anime_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**GetAnimeById200Response**](GetAnimeById200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns anime resource |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_anime_characters**
> AnimeCharacters get_anime_characters(id)



### Example


```python
import jikan_openapi
from jikan_openapi.models.anime_characters import AnimeCharacters
from jikan_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.jikan.moe/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = jikan_openapi.Configuration(
    host = "https://api.jikan.moe/v4"
)


# Enter a context with an instance of the API client
with jikan_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jikan_openapi.AnimeApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_anime_characters(id)
        print("The response of AnimeApi->get_anime_characters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnimeApi->get_anime_characters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**AnimeCharacters**](AnimeCharacters.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns anime characters resource |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_anime_episode_by_id**
> GetAnimeEpisodeById200Response get_anime_episode_by_id(id, episode)



### Example


```python
import jikan_openapi
from jikan_openapi.models.get_anime_episode_by_id200_response import GetAnimeEpisodeById200Response
from jikan_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.jikan.moe/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = jikan_openapi.Configuration(
    host = "https://api.jikan.moe/v4"
)


# Enter a context with an instance of the API client
with jikan_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jikan_openapi.AnimeApi(api_client)
    id = 56 # int | 
    episode = 56 # int | 

    try:
        api_response = api_instance.get_anime_episode_by_id(id, episode)
        print("The response of AnimeApi->get_anime_episode_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnimeApi->get_anime_episode_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **episode** | **int**|  | 

### Return type

[**GetAnimeEpisodeById200Response**](GetAnimeEpisodeById200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single anime episode resource |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_anime_episodes**
> AnimeEpisodes get_anime_episodes(id, page=page)



### Example


```python
import jikan_openapi
from jikan_openapi.models.anime_episodes import AnimeEpisodes
from jikan_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.jikan.moe/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = jikan_openapi.Configuration(
    host = "https://api.jikan.moe/v4"
)


# Enter a context with an instance of the API client
with jikan_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jikan_openapi.AnimeApi(api_client)
    id = 56 # int | 
    page = 56 # int |  (optional)

    try:
        api_response = api_instance.get_anime_episodes(id, page=page)
        print("The response of AnimeApi->get_anime_episodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnimeApi->get_anime_episodes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **page** | **int**|  | [optional] 

### Return type

[**AnimeEpisodes**](AnimeEpisodes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of anime episodes |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_anime_external**
> ExternalLinks get_anime_external(id)



### Example


```python
import jikan_openapi
from jikan_openapi.models.external_links import ExternalLinks
from jikan_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.jikan.moe/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = jikan_openapi.Configuration(
    host = "https://api.jikan.moe/v4"
)


# Enter a context with an instance of the API client
with jikan_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jikan_openapi.AnimeApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_anime_external(id)
        print("The response of AnimeApi->get_anime_external:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnimeApi->get_anime_external: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ExternalLinks**](ExternalLinks.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns anime external links |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_anime_forum**
> Forum get_anime_forum(id, filter=filter)



### Example


```python
import jikan_openapi
from jikan_openapi.models.forum import Forum
from jikan_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.jikan.moe/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = jikan_openapi.Configuration(
    host = "https://api.jikan.moe/v4"
)


# Enter a context with an instance of the API client
with jikan_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jikan_openapi.AnimeApi(api_client)
    id = 56 # int | 
    filter = 'filter_example' # str | Filter topics (optional)

    try:
        api_response = api_instance.get_anime_forum(id, filter=filter)
        print("The response of AnimeApi->get_anime_forum:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnimeApi->get_anime_forum: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **filter** | **str**| Filter topics | [optional] 

### Return type

[**Forum**](Forum.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of forum topics related to the entry |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_anime_full_by_id**
> GetAnimeFullById200Response get_anime_full_by_id(id)



### Example


```python
import jikan_openapi
from jikan_openapi.models.get_anime_full_by_id200_response import GetAnimeFullById200Response
from jikan_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.jikan.moe/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = jikan_openapi.Configuration(
    host = "https://api.jikan.moe/v4"
)


# Enter a context with an instance of the API client
with jikan_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jikan_openapi.AnimeApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_anime_full_by_id(id)
        print("The response of AnimeApi->get_anime_full_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnimeApi->get_anime_full_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**GetAnimeFullById200Response**](GetAnimeFullById200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns complete anime resource data |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_anime_more_info**
> Moreinfo get_anime_more_info(id)



### Example


```python
import jikan_openapi
from jikan_openapi.models.moreinfo import Moreinfo
from jikan_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.jikan.moe/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = jikan_openapi.Configuration(
    host = "https://api.jikan.moe/v4"
)


# Enter a context with an instance of the API client
with jikan_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jikan_openapi.AnimeApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_anime_more_info(id)
        print("The response of AnimeApi->get_anime_more_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnimeApi->get_anime_more_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Moreinfo**](Moreinfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns anime statistics |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_anime_news**
> AnimeNews get_anime_news(id, page=page)



### Example


```python
import jikan_openapi
from jikan_openapi.models.anime_news import AnimeNews
from jikan_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.jikan.moe/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = jikan_openapi.Configuration(
    host = "https://api.jikan.moe/v4"
)


# Enter a context with an instance of the API client
with jikan_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jikan_openapi.AnimeApi(api_client)
    id = 56 # int | 
    page = 56 # int |  (optional)

    try:
        api_response = api_instance.get_anime_news(id, page=page)
        print("The response of AnimeApi->get_anime_news:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnimeApi->get_anime_news: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **page** | **int**|  | [optional] 

### Return type

[**AnimeNews**](AnimeNews.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of news articles related to the entry |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_anime_pictures**
> PicturesVariants get_anime_pictures(id)



### Example


```python
import jikan_openapi
from jikan_openapi.models.pictures_variants import PicturesVariants
from jikan_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.jikan.moe/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = jikan_openapi.Configuration(
    host = "https://api.jikan.moe/v4"
)


# Enter a context with an instance of the API client
with jikan_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jikan_openapi.AnimeApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_anime_pictures(id)
        print("The response of AnimeApi->get_anime_pictures:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnimeApi->get_anime_pictures: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**PicturesVariants**](PicturesVariants.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns pictures related to the entry |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_anime_recommendations**
> EntryRecommendations get_anime_recommendations(id)



### Example


```python
import jikan_openapi
from jikan_openapi.models.entry_recommendations import EntryRecommendations
from jikan_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.jikan.moe/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = jikan_openapi.Configuration(
    host = "https://api.jikan.moe/v4"
)


# Enter a context with an instance of the API client
with jikan_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jikan_openapi.AnimeApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_anime_recommendations(id)
        print("The response of AnimeApi->get_anime_recommendations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnimeApi->get_anime_recommendations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**EntryRecommendations**](EntryRecommendations.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns anime recommendations |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_anime_relations**
> GetAnimeRelations200Response get_anime_relations(id)



### Example


```python
import jikan_openapi
from jikan_openapi.models.get_anime_relations200_response import GetAnimeRelations200Response
from jikan_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.jikan.moe/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = jikan_openapi.Configuration(
    host = "https://api.jikan.moe/v4"
)


# Enter a context with an instance of the API client
with jikan_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jikan_openapi.AnimeApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_anime_relations(id)
        print("The response of AnimeApi->get_anime_relations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnimeApi->get_anime_relations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**GetAnimeRelations200Response**](GetAnimeRelations200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns anime relations |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_anime_reviews**
> AnimeReviews get_anime_reviews(id, page=page, preliminary=preliminary, spoilers=spoilers)



### Example


```python
import jikan_openapi
from jikan_openapi.models.anime_reviews import AnimeReviews
from jikan_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.jikan.moe/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = jikan_openapi.Configuration(
    host = "https://api.jikan.moe/v4"
)


# Enter a context with an instance of the API client
with jikan_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jikan_openapi.AnimeApi(api_client)
    id = 56 # int | 
    page = 56 # int |  (optional)
    preliminary = True # bool | Any reviews left during an ongoing anime/manga, those reviews are tagged as preliminary. NOTE: Preliminary reviews are not returned by default so if the entry is airing/publishing you need to add this otherwise you will get an empty list. e.g usage: `?preliminary=true` (optional)
    spoilers = True # bool | Any reviews that are tagged as a spoiler. Spoiler reviews are not returned by default. e.g usage: `?spoiler=true` (optional)

    try:
        api_response = api_instance.get_anime_reviews(id, page=page, preliminary=preliminary, spoilers=spoilers)
        print("The response of AnimeApi->get_anime_reviews:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnimeApi->get_anime_reviews: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **page** | **int**|  | [optional] 
 **preliminary** | **bool**| Any reviews left during an ongoing anime/manga, those reviews are tagged as preliminary. NOTE: Preliminary reviews are not returned by default so if the entry is airing/publishing you need to add this otherwise you will get an empty list. e.g usage: &#x60;?preliminary&#x3D;true&#x60; | [optional] 
 **spoilers** | **bool**| Any reviews that are tagged as a spoiler. Spoiler reviews are not returned by default. e.g usage: &#x60;?spoiler&#x3D;true&#x60; | [optional] 

### Return type

[**AnimeReviews**](AnimeReviews.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns anime reviews |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_anime_search**
> AnimeSearch get_anime_search(unapproved=unapproved, page=page, limit=limit, q=q, type=type, score=score, min_score=min_score, max_score=max_score, status=status, rating=rating, sfw=sfw, genres=genres, genres_exclude=genres_exclude, order_by=order_by, sort=sort, letter=letter, producers=producers, start_date=start_date, end_date=end_date)



### Example


```python
import jikan_openapi
from jikan_openapi.models.anime_search import AnimeSearch
from jikan_openapi.models.anime_search_query_orderby import AnimeSearchQueryOrderby
from jikan_openapi.models.anime_search_query_rating import AnimeSearchQueryRating
from jikan_openapi.models.anime_search_query_status import AnimeSearchQueryStatus
from jikan_openapi.models.anime_search_query_type import AnimeSearchQueryType
from jikan_openapi.models.search_query_sort import SearchQuerySort
from jikan_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.jikan.moe/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = jikan_openapi.Configuration(
    host = "https://api.jikan.moe/v4"
)


# Enter a context with an instance of the API client
with jikan_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jikan_openapi.AnimeApi(api_client)
    unapproved = True # bool | This is a flag. When supplied it will include entries which are unapproved. Unapproved entries on MyAnimeList are those that are user submitted and have not yet been approved by MAL to show up on other pages. They will have their own specifc pages and are often removed resulting in a 404 error. You do not need to pass a value to it. e.g usage: `?unapproved` (optional)
    page = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    q = 'q_example' # str |  (optional)
    type = jikan_openapi.AnimeSearchQueryType() # AnimeSearchQueryType |  (optional)
    score = 3.4 # float |  (optional)
    min_score = 3.4 # float | Set a minimum score for results. (optional)
    max_score = 3.4 # float | Set a maximum score for results (optional)
    status = jikan_openapi.AnimeSearchQueryStatus() # AnimeSearchQueryStatus |  (optional)
    rating = jikan_openapi.AnimeSearchQueryRating() # AnimeSearchQueryRating |  (optional)
    sfw = True # bool | Filter out Adult entries (optional)
    genres = 'genres_example' # str | Filter by genre(s) IDs. Can pass multiple with a comma as a delimiter. e.g 1,2,3 (optional)
    genres_exclude = 'genres_exclude_example' # str | Exclude genre(s) IDs. Can pass multiple with a comma as a delimiter. e.g 1,2,3 (optional)
    order_by = jikan_openapi.AnimeSearchQueryOrderby() # AnimeSearchQueryOrderby |  (optional)
    sort = jikan_openapi.SearchQuerySort() # SearchQuerySort |  (optional)
    letter = 'letter_example' # str | Return entries starting with the given letter (optional)
    producers = 'producers_example' # str | Filter by producer(s) IDs. Can pass multiple with a comma as a delimiter. e.g 1,2,3 (optional)
    start_date = 'start_date_example' # str | Filter by starting date. Format: YYYY-MM-DD. e.g `2022`, `2005-05`, `2005-01-01` (optional)
    end_date = 'end_date_example' # str | Filter by ending date. Format: YYYY-MM-DD. e.g `2022`, `2005-05`, `2005-01-01` (optional)

    try:
        api_response = api_instance.get_anime_search(unapproved=unapproved, page=page, limit=limit, q=q, type=type, score=score, min_score=min_score, max_score=max_score, status=status, rating=rating, sfw=sfw, genres=genres, genres_exclude=genres_exclude, order_by=order_by, sort=sort, letter=letter, producers=producers, start_date=start_date, end_date=end_date)
        print("The response of AnimeApi->get_anime_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnimeApi->get_anime_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unapproved** | **bool**| This is a flag. When supplied it will include entries which are unapproved. Unapproved entries on MyAnimeList are those that are user submitted and have not yet been approved by MAL to show up on other pages. They will have their own specifc pages and are often removed resulting in a 404 error. You do not need to pass a value to it. e.g usage: &#x60;?unapproved&#x60; | [optional] 
 **page** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **q** | **str**|  | [optional] 
 **type** | [**AnimeSearchQueryType**](.md)|  | [optional] 
 **score** | **float**|  | [optional] 
 **min_score** | **float**| Set a minimum score for results. | [optional] 
 **max_score** | **float**| Set a maximum score for results | [optional] 
 **status** | [**AnimeSearchQueryStatus**](.md)|  | [optional] 
 **rating** | [**AnimeSearchQueryRating**](.md)|  | [optional] 
 **sfw** | **bool**| Filter out Adult entries | [optional] 
 **genres** | **str**| Filter by genre(s) IDs. Can pass multiple with a comma as a delimiter. e.g 1,2,3 | [optional] 
 **genres_exclude** | **str**| Exclude genre(s) IDs. Can pass multiple with a comma as a delimiter. e.g 1,2,3 | [optional] 
 **order_by** | [**AnimeSearchQueryOrderby**](.md)|  | [optional] 
 **sort** | [**SearchQuerySort**](.md)|  | [optional] 
 **letter** | **str**| Return entries starting with the given letter | [optional] 
 **producers** | **str**| Filter by producer(s) IDs. Can pass multiple with a comma as a delimiter. e.g 1,2,3 | [optional] 
 **start_date** | **str**| Filter by starting date. Format: YYYY-MM-DD. e.g &#x60;2022&#x60;, &#x60;2005-05&#x60;, &#x60;2005-01-01&#x60; | [optional] 
 **end_date** | **str**| Filter by ending date. Format: YYYY-MM-DD. e.g &#x60;2022&#x60;, &#x60;2005-05&#x60;, &#x60;2005-01-01&#x60; | [optional] 

### Return type

[**AnimeSearch**](AnimeSearch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns search results for anime |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_anime_staff**
> AnimeStaff get_anime_staff(id)



### Example


```python
import jikan_openapi
from jikan_openapi.models.anime_staff import AnimeStaff
from jikan_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.jikan.moe/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = jikan_openapi.Configuration(
    host = "https://api.jikan.moe/v4"
)


# Enter a context with an instance of the API client
with jikan_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jikan_openapi.AnimeApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_anime_staff(id)
        print("The response of AnimeApi->get_anime_staff:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnimeApi->get_anime_staff: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**AnimeStaff**](AnimeStaff.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns anime staff resource |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_anime_statistics**
> AnimeStatistics get_anime_statistics(id)



### Example


```python
import jikan_openapi
from jikan_openapi.models.anime_statistics import AnimeStatistics
from jikan_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.jikan.moe/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = jikan_openapi.Configuration(
    host = "https://api.jikan.moe/v4"
)


# Enter a context with an instance of the API client
with jikan_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jikan_openapi.AnimeApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_anime_statistics(id)
        print("The response of AnimeApi->get_anime_statistics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnimeApi->get_anime_statistics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**AnimeStatistics**](AnimeStatistics.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns anime statistics |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_anime_streaming**
> ExternalLinks get_anime_streaming(id)



### Example


```python
import jikan_openapi
from jikan_openapi.models.external_links import ExternalLinks
from jikan_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.jikan.moe/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = jikan_openapi.Configuration(
    host = "https://api.jikan.moe/v4"
)


# Enter a context with an instance of the API client
with jikan_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jikan_openapi.AnimeApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_anime_streaming(id)
        print("The response of AnimeApi->get_anime_streaming:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnimeApi->get_anime_streaming: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ExternalLinks**](ExternalLinks.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns anime streaming links |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_anime_themes**
> AnimeThemes get_anime_themes(id)



### Example


```python
import jikan_openapi
from jikan_openapi.models.anime_themes import AnimeThemes
from jikan_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.jikan.moe/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = jikan_openapi.Configuration(
    host = "https://api.jikan.moe/v4"
)


# Enter a context with an instance of the API client
with jikan_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jikan_openapi.AnimeApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_anime_themes(id)
        print("The response of AnimeApi->get_anime_themes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnimeApi->get_anime_themes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**AnimeThemes**](AnimeThemes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns anime themes |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_anime_user_updates**
> AnimeUserupdates get_anime_user_updates(id, page=page)



### Example


```python
import jikan_openapi
from jikan_openapi.models.anime_userupdates import AnimeUserupdates
from jikan_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.jikan.moe/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = jikan_openapi.Configuration(
    host = "https://api.jikan.moe/v4"
)


# Enter a context with an instance of the API client
with jikan_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jikan_openapi.AnimeApi(api_client)
    id = 56 # int | 
    page = 56 # int |  (optional)

    try:
        api_response = api_instance.get_anime_user_updates(id, page=page)
        print("The response of AnimeApi->get_anime_user_updates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnimeApi->get_anime_user_updates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **page** | **int**|  | [optional] 

### Return type

[**AnimeUserupdates**](AnimeUserupdates.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of users who have added/updated/removed the entry on their list |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_anime_videos**
> AnimeVideos get_anime_videos(id)



### Example


```python
import jikan_openapi
from jikan_openapi.models.anime_videos import AnimeVideos
from jikan_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.jikan.moe/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = jikan_openapi.Configuration(
    host = "https://api.jikan.moe/v4"
)


# Enter a context with an instance of the API client
with jikan_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jikan_openapi.AnimeApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_anime_videos(id)
        print("The response of AnimeApi->get_anime_videos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnimeApi->get_anime_videos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**AnimeVideos**](AnimeVideos.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns videos related to the entry |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_anime_videos_episodes**
> AnimeVideosEpisodes get_anime_videos_episodes(id, page=page)



### Example


```python
import jikan_openapi
from jikan_openapi.models.anime_videos_episodes import AnimeVideosEpisodes
from jikan_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.jikan.moe/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = jikan_openapi.Configuration(
    host = "https://api.jikan.moe/v4"
)


# Enter a context with an instance of the API client
with jikan_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jikan_openapi.AnimeApi(api_client)
    id = 56 # int | 
    page = 56 # int |  (optional)

    try:
        api_response = api_instance.get_anime_videos_episodes(id, page=page)
        print("The response of AnimeApi->get_anime_videos_episodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnimeApi->get_anime_videos_episodes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **page** | **int**|  | [optional] 

### Return type

[**AnimeVideosEpisodes**](AnimeVideosEpisodes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns episode videos related to the entry |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

