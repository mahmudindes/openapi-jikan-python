# jikan_openapi.MangaApi

All URIs are relative to *https://api.jikan.moe/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_manga_by_id**](MangaApi.md#get_manga_by_id) | **GET** /manga/{id} | 
[**get_manga_characters**](MangaApi.md#get_manga_characters) | **GET** /manga/{id}/characters | 
[**get_manga_external**](MangaApi.md#get_manga_external) | **GET** /manga/{id}/external | 
[**get_manga_full_by_id**](MangaApi.md#get_manga_full_by_id) | **GET** /manga/{id}/full | 
[**get_manga_more_info**](MangaApi.md#get_manga_more_info) | **GET** /manga/{id}/moreinfo | 
[**get_manga_news**](MangaApi.md#get_manga_news) | **GET** /manga/{id}/news | 
[**get_manga_pictures**](MangaApi.md#get_manga_pictures) | **GET** /manga/{id}/pictures | 
[**get_manga_recommendations**](MangaApi.md#get_manga_recommendations) | **GET** /manga/{id}/recommendations | 
[**get_manga_relations**](MangaApi.md#get_manga_relations) | **GET** /manga/{id}/relations | 
[**get_manga_reviews**](MangaApi.md#get_manga_reviews) | **GET** /manga/{id}/reviews | 
[**get_manga_search**](MangaApi.md#get_manga_search) | **GET** /manga | 
[**get_manga_statistics**](MangaApi.md#get_manga_statistics) | **GET** /manga/{id}/statistics | 
[**get_manga_topics**](MangaApi.md#get_manga_topics) | **GET** /manga/{id}/forum | 
[**get_manga_user_updates**](MangaApi.md#get_manga_user_updates) | **GET** /manga/{id}/userupdates | 


# **get_manga_by_id**
> GetMangaById200Response get_manga_by_id(id)



### Example


```python
import jikan_openapi
from jikan_openapi.models.get_manga_by_id200_response import GetMangaById200Response
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
    api_instance = jikan_openapi.MangaApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_manga_by_id(id)
        print("The response of MangaApi->get_manga_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MangaApi->get_manga_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**GetMangaById200Response**](GetMangaById200Response.md)

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

# **get_manga_characters**
> MangaCharacters get_manga_characters(id)



### Example


```python
import jikan_openapi
from jikan_openapi.models.manga_characters import MangaCharacters
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
    api_instance = jikan_openapi.MangaApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_manga_characters(id)
        print("The response of MangaApi->get_manga_characters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MangaApi->get_manga_characters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**MangaCharacters**](MangaCharacters.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns manga characters resource |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_manga_external**
> ExternalLinks get_manga_external(id)



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
    api_instance = jikan_openapi.MangaApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_manga_external(id)
        print("The response of MangaApi->get_manga_external:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MangaApi->get_manga_external: %s\n" % e)
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
**200** | Returns manga external links |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_manga_full_by_id**
> GetMangaFullById200Response get_manga_full_by_id(id)



### Example


```python
import jikan_openapi
from jikan_openapi.models.get_manga_full_by_id200_response import GetMangaFullById200Response
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
    api_instance = jikan_openapi.MangaApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_manga_full_by_id(id)
        print("The response of MangaApi->get_manga_full_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MangaApi->get_manga_full_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**GetMangaFullById200Response**](GetMangaFullById200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns complete manga resource data |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_manga_more_info**
> Moreinfo get_manga_more_info(id)



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
    api_instance = jikan_openapi.MangaApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_manga_more_info(id)
        print("The response of MangaApi->get_manga_more_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MangaApi->get_manga_more_info: %s\n" % e)
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
**200** | Returns manga moreinfo |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_manga_news**
> MangaNews get_manga_news(id, page=page)



### Example


```python
import jikan_openapi
from jikan_openapi.models.manga_news import MangaNews
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
    api_instance = jikan_openapi.MangaApi(api_client)
    id = 56 # int | 
    page = 56 # int |  (optional)

    try:
        api_response = api_instance.get_manga_news(id, page=page)
        print("The response of MangaApi->get_manga_news:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MangaApi->get_manga_news: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **page** | **int**|  | [optional] 

### Return type

[**MangaNews**](MangaNews.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of manga news topics |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_manga_pictures**
> MangaPictures get_manga_pictures(id)



### Example


```python
import jikan_openapi
from jikan_openapi.models.manga_pictures import MangaPictures
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
    api_instance = jikan_openapi.MangaApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_manga_pictures(id)
        print("The response of MangaApi->get_manga_pictures:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MangaApi->get_manga_pictures: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**MangaPictures**](MangaPictures.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of manga pictures |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_manga_recommendations**
> EntryRecommendations get_manga_recommendations(id)



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
    api_instance = jikan_openapi.MangaApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_manga_recommendations(id)
        print("The response of MangaApi->get_manga_recommendations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MangaApi->get_manga_recommendations: %s\n" % e)
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
**200** | Returns manga recommendations |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_manga_relations**
> GetAnimeRelations200Response get_manga_relations(id)



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
    api_instance = jikan_openapi.MangaApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_manga_relations(id)
        print("The response of MangaApi->get_manga_relations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MangaApi->get_manga_relations: %s\n" % e)
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
**200** | Returns manga relations |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_manga_reviews**
> MangaReviews get_manga_reviews(id, page=page, preliminary=preliminary, spoilers=spoilers)



### Example


```python
import jikan_openapi
from jikan_openapi.models.manga_reviews import MangaReviews
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
    api_instance = jikan_openapi.MangaApi(api_client)
    id = 56 # int | 
    page = 56 # int |  (optional)
    preliminary = True # bool | Any reviews left during an ongoing anime/manga, those reviews are tagged as preliminary. NOTE: Preliminary reviews are not returned by default so if the entry is airing/publishing you need to add this otherwise you will get an empty list. e.g usage: `?preliminary=true` (optional)
    spoilers = True # bool | Any reviews that are tagged as a spoiler. Spoiler reviews are not returned by default. e.g usage: `?spoiler=true` (optional)

    try:
        api_response = api_instance.get_manga_reviews(id, page=page, preliminary=preliminary, spoilers=spoilers)
        print("The response of MangaApi->get_manga_reviews:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MangaApi->get_manga_reviews: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **page** | **int**|  | [optional] 
 **preliminary** | **bool**| Any reviews left during an ongoing anime/manga, those reviews are tagged as preliminary. NOTE: Preliminary reviews are not returned by default so if the entry is airing/publishing you need to add this otherwise you will get an empty list. e.g usage: &#x60;?preliminary&#x3D;true&#x60; | [optional] 
 **spoilers** | **bool**| Any reviews that are tagged as a spoiler. Spoiler reviews are not returned by default. e.g usage: &#x60;?spoiler&#x3D;true&#x60; | [optional] 

### Return type

[**MangaReviews**](MangaReviews.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns manga reviews |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_manga_search**
> MangaSearch get_manga_search(unapproved=unapproved, page=page, limit=limit, q=q, type=type, score=score, min_score=min_score, max_score=max_score, status=status, sfw=sfw, genres=genres, genres_exclude=genres_exclude, order_by=order_by, sort=sort, letter=letter, magazines=magazines, start_date=start_date, end_date=end_date)



### Example


```python
import jikan_openapi
from jikan_openapi.models.manga_search import MangaSearch
from jikan_openapi.models.manga_search_query_orderby import MangaSearchQueryOrderby
from jikan_openapi.models.manga_search_query_status import MangaSearchQueryStatus
from jikan_openapi.models.manga_search_query_type import MangaSearchQueryType
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
    api_instance = jikan_openapi.MangaApi(api_client)
    unapproved = True # bool | This is a flag. When supplied it will include entries which are unapproved. Unapproved entries on MyAnimeList are those that are user submitted and have not yet been approved by MAL to show up on other pages. They will have their own specifc pages and are often removed resulting in a 404 error. You do not need to pass a value to it. e.g usage: `?unapproved` (optional)
    page = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    q = 'q_example' # str |  (optional)
    type = jikan_openapi.MangaSearchQueryType() # MangaSearchQueryType |  (optional)
    score = 3.4 # float |  (optional)
    min_score = 3.4 # float | Set a minimum score for results. (optional)
    max_score = 3.4 # float | Set a maximum score for results (optional)
    status = jikan_openapi.MangaSearchQueryStatus() # MangaSearchQueryStatus |  (optional)
    sfw = True # bool | Filter out Adult entries (optional)
    genres = 'genres_example' # str | Filter by genre(s) IDs. Can pass multiple with a comma as a delimiter. e.g 1,2,3 (optional)
    genres_exclude = 'genres_exclude_example' # str | Exclude genre(s) IDs. Can pass multiple with a comma as a delimiter. e.g 1,2,3 (optional)
    order_by = jikan_openapi.MangaSearchQueryOrderby() # MangaSearchQueryOrderby |  (optional)
    sort = jikan_openapi.SearchQuerySort() # SearchQuerySort |  (optional)
    letter = 'letter_example' # str | Return entries starting with the given letter (optional)
    magazines = 'magazines_example' # str | Filter by magazine(s) IDs. Can pass multiple with a comma as a delimiter. e.g 1,2,3 (optional)
    start_date = 'start_date_example' # str | Filter by starting date. Format: YYYY-MM-DD. e.g `2022`, `2005-05`, `2005-01-01` (optional)
    end_date = 'end_date_example' # str | Filter by ending date. Format: YYYY-MM-DD. e.g `2022`, `2005-05`, `2005-01-01` (optional)

    try:
        api_response = api_instance.get_manga_search(unapproved=unapproved, page=page, limit=limit, q=q, type=type, score=score, min_score=min_score, max_score=max_score, status=status, sfw=sfw, genres=genres, genres_exclude=genres_exclude, order_by=order_by, sort=sort, letter=letter, magazines=magazines, start_date=start_date, end_date=end_date)
        print("The response of MangaApi->get_manga_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MangaApi->get_manga_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unapproved** | **bool**| This is a flag. When supplied it will include entries which are unapproved. Unapproved entries on MyAnimeList are those that are user submitted and have not yet been approved by MAL to show up on other pages. They will have their own specifc pages and are often removed resulting in a 404 error. You do not need to pass a value to it. e.g usage: &#x60;?unapproved&#x60; | [optional] 
 **page** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **q** | **str**|  | [optional] 
 **type** | [**MangaSearchQueryType**](.md)|  | [optional] 
 **score** | **float**|  | [optional] 
 **min_score** | **float**| Set a minimum score for results. | [optional] 
 **max_score** | **float**| Set a maximum score for results | [optional] 
 **status** | [**MangaSearchQueryStatus**](.md)|  | [optional] 
 **sfw** | **bool**| Filter out Adult entries | [optional] 
 **genres** | **str**| Filter by genre(s) IDs. Can pass multiple with a comma as a delimiter. e.g 1,2,3 | [optional] 
 **genres_exclude** | **str**| Exclude genre(s) IDs. Can pass multiple with a comma as a delimiter. e.g 1,2,3 | [optional] 
 **order_by** | [**MangaSearchQueryOrderby**](.md)|  | [optional] 
 **sort** | [**SearchQuerySort**](.md)|  | [optional] 
 **letter** | **str**| Return entries starting with the given letter | [optional] 
 **magazines** | **str**| Filter by magazine(s) IDs. Can pass multiple with a comma as a delimiter. e.g 1,2,3 | [optional] 
 **start_date** | **str**| Filter by starting date. Format: YYYY-MM-DD. e.g &#x60;2022&#x60;, &#x60;2005-05&#x60;, &#x60;2005-01-01&#x60; | [optional] 
 **end_date** | **str**| Filter by ending date. Format: YYYY-MM-DD. e.g &#x60;2022&#x60;, &#x60;2005-05&#x60;, &#x60;2005-01-01&#x60; | [optional] 

### Return type

[**MangaSearch**](MangaSearch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns search results for manga |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_manga_statistics**
> MangaStatistics get_manga_statistics(id)



### Example


```python
import jikan_openapi
from jikan_openapi.models.manga_statistics import MangaStatistics
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
    api_instance = jikan_openapi.MangaApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_manga_statistics(id)
        print("The response of MangaApi->get_manga_statistics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MangaApi->get_manga_statistics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**MangaStatistics**](MangaStatistics.md)

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

# **get_manga_topics**
> Forum get_manga_topics(id, filter=filter)



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
    api_instance = jikan_openapi.MangaApi(api_client)
    id = 56 # int | 
    filter = 'filter_example' # str | Filter topics (optional)

    try:
        api_response = api_instance.get_manga_topics(id, filter=filter)
        print("The response of MangaApi->get_manga_topics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MangaApi->get_manga_topics: %s\n" % e)
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
**200** | Returns a list of manga forum topics |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_manga_user_updates**
> MangaUserupdates get_manga_user_updates(id, page=page)



### Example


```python
import jikan_openapi
from jikan_openapi.models.manga_userupdates import MangaUserupdates
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
    api_instance = jikan_openapi.MangaApi(api_client)
    id = 56 # int | 
    page = 56 # int |  (optional)

    try:
        api_response = api_instance.get_manga_user_updates(id, page=page)
        print("The response of MangaApi->get_manga_user_updates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MangaApi->get_manga_user_updates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **page** | **int**|  | [optional] 

### Return type

[**MangaUserupdates**](MangaUserupdates.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns manga user updates |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

