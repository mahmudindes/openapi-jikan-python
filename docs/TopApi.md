# jikan_openapi.TopApi

All URIs are relative to *https://api.jikan.moe/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_top_anime**](TopApi.md#get_top_anime) | **GET** /top/anime | 
[**get_top_characters**](TopApi.md#get_top_characters) | **GET** /top/characters | 
[**get_top_manga**](TopApi.md#get_top_manga) | **GET** /top/manga | 
[**get_top_people**](TopApi.md#get_top_people) | **GET** /top/people | 
[**get_top_reviews**](TopApi.md#get_top_reviews) | **GET** /top/reviews | 


# **get_top_anime**
> AnimeSearch get_top_anime(type=type, filter=filter, rating=rating, sfw=sfw, page=page, limit=limit)



### Example


```python
import jikan_openapi
from jikan_openapi.models.anime_search import AnimeSearch
from jikan_openapi.models.anime_search_query_rating import AnimeSearchQueryRating
from jikan_openapi.models.anime_search_query_type import AnimeSearchQueryType
from jikan_openapi.models.top_anime_filter import TopAnimeFilter
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
    api_instance = jikan_openapi.TopApi(api_client)
    type = jikan_openapi.AnimeSearchQueryType() # AnimeSearchQueryType |  (optional)
    filter = jikan_openapi.TopAnimeFilter() # TopAnimeFilter |  (optional)
    rating = jikan_openapi.AnimeSearchQueryRating() # AnimeSearchQueryRating |  (optional)
    sfw = True # bool | Filter out Adult entries (optional)
    page = 56 # int |  (optional)
    limit = 56 # int |  (optional)

    try:
        api_response = api_instance.get_top_anime(type=type, filter=filter, rating=rating, sfw=sfw, page=page, limit=limit)
        print("The response of TopApi->get_top_anime:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TopApi->get_top_anime: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**AnimeSearchQueryType**](.md)|  | [optional] 
 **filter** | [**TopAnimeFilter**](.md)|  | [optional] 
 **rating** | [**AnimeSearchQueryRating**](.md)|  | [optional] 
 **sfw** | **bool**| Filter out Adult entries | [optional] 
 **page** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 

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
**200** | Returns top anime |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_top_characters**
> CharactersSearch get_top_characters(page=page, limit=limit)



### Example


```python
import jikan_openapi
from jikan_openapi.models.characters_search import CharactersSearch
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
    api_instance = jikan_openapi.TopApi(api_client)
    page = 56 # int |  (optional)
    limit = 56 # int |  (optional)

    try:
        api_response = api_instance.get_top_characters(page=page, limit=limit)
        print("The response of TopApi->get_top_characters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TopApi->get_top_characters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 

### Return type

[**CharactersSearch**](CharactersSearch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns top characters |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_top_manga**
> MangaSearch get_top_manga(type=type, filter=filter, page=page, limit=limit)



### Example


```python
import jikan_openapi
from jikan_openapi.models.manga_search import MangaSearch
from jikan_openapi.models.manga_search_query_type import MangaSearchQueryType
from jikan_openapi.models.top_manga_filter import TopMangaFilter
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
    api_instance = jikan_openapi.TopApi(api_client)
    type = jikan_openapi.MangaSearchQueryType() # MangaSearchQueryType |  (optional)
    filter = jikan_openapi.TopMangaFilter() # TopMangaFilter |  (optional)
    page = 56 # int |  (optional)
    limit = 56 # int |  (optional)

    try:
        api_response = api_instance.get_top_manga(type=type, filter=filter, page=page, limit=limit)
        print("The response of TopApi->get_top_manga:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TopApi->get_top_manga: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**MangaSearchQueryType**](.md)|  | [optional] 
 **filter** | [**TopMangaFilter**](.md)|  | [optional] 
 **page** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 

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
**200** | Returns top manga |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_top_people**
> PeopleSearch get_top_people(page=page, limit=limit)



### Example


```python
import jikan_openapi
from jikan_openapi.models.people_search import PeopleSearch
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
    api_instance = jikan_openapi.TopApi(api_client)
    page = 56 # int |  (optional)
    limit = 56 # int |  (optional)

    try:
        api_response = api_instance.get_top_people(page=page, limit=limit)
        print("The response of TopApi->get_top_people:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TopApi->get_top_people: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 

### Return type

[**PeopleSearch**](PeopleSearch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns top people |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_top_reviews**
> GetTopReviews200Response get_top_reviews(page=page, type=type, preliminary=preliminary, spoilers=spoilers)



### Example


```python
import jikan_openapi
from jikan_openapi.models.get_top_reviews200_response import GetTopReviews200Response
from jikan_openapi.models.top_reviews_type_enum import TopReviewsTypeEnum
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
    api_instance = jikan_openapi.TopApi(api_client)
    page = 56 # int |  (optional)
    type = jikan_openapi.TopReviewsTypeEnum() # TopReviewsTypeEnum |  (optional)
    preliminary = True # bool | Whether the results include preliminary reviews or not. Defaults to true. (optional)
    spoilers = True # bool | Whether the results include reviews with spoilers or not. Defaults to true. (optional)

    try:
        api_response = api_instance.get_top_reviews(page=page, type=type, preliminary=preliminary, spoilers=spoilers)
        print("The response of TopApi->get_top_reviews:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TopApi->get_top_reviews: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **type** | [**TopReviewsTypeEnum**](.md)|  | [optional] 
 **preliminary** | **bool**| Whether the results include preliminary reviews or not. Defaults to true. | [optional] 
 **spoilers** | **bool**| Whether the results include reviews with spoilers or not. Defaults to true. | [optional] 

### Return type

[**GetTopReviews200Response**](GetTopReviews200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns top reviews |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

