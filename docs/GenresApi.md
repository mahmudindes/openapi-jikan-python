# jikan_openapi.GenresApi

All URIs are relative to *https://api.jikan.moe/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_anime_genres**](GenresApi.md#get_anime_genres) | **GET** /genres/anime | 
[**get_manga_genres**](GenresApi.md#get_manga_genres) | **GET** /genres/manga | 


# **get_anime_genres**
> Genres get_anime_genres(filter=filter)



### Example


```python
import jikan_openapi
from jikan_openapi.models.genre_query_filter import GenreQueryFilter
from jikan_openapi.models.genres import Genres
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
    api_instance = jikan_openapi.GenresApi(api_client)
    filter = jikan_openapi.GenreQueryFilter() # GenreQueryFilter |  (optional)

    try:
        api_response = api_instance.get_anime_genres(filter=filter)
        print("The response of GenresApi->get_anime_genres:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenresApi->get_anime_genres: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**GenreQueryFilter**](.md)|  | [optional] 

### Return type

[**Genres**](Genres.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns entry genres, explicit_genres, themes and demographics |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_manga_genres**
> Genres get_manga_genres(filter=filter)



### Example


```python
import jikan_openapi
from jikan_openapi.models.genre_query_filter import GenreQueryFilter
from jikan_openapi.models.genres import Genres
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
    api_instance = jikan_openapi.GenresApi(api_client)
    filter = jikan_openapi.GenreQueryFilter() # GenreQueryFilter |  (optional)

    try:
        api_response = api_instance.get_manga_genres(filter=filter)
        print("The response of GenresApi->get_manga_genres:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenresApi->get_manga_genres: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**GenreQueryFilter**](.md)|  | [optional] 

### Return type

[**Genres**](Genres.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns entry genres, explicit_genres, themes and demographics |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

