# jikan_openapi.WatchApi

All URIs are relative to *https://api.jikan.moe/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_watch_popular_episodes**](WatchApi.md#get_watch_popular_episodes) | **GET** /watch/episodes/popular | 
[**get_watch_popular_promos**](WatchApi.md#get_watch_popular_promos) | **GET** /watch/promos/popular | 
[**get_watch_recent_episodes**](WatchApi.md#get_watch_recent_episodes) | **GET** /watch/episodes | 
[**get_watch_recent_promos**](WatchApi.md#get_watch_recent_promos) | **GET** /watch/promos | 


# **get_watch_popular_episodes**
> WatchEpisodes get_watch_popular_episodes()



### Example


```python
import jikan_openapi
from jikan_openapi.models.watch_episodes import WatchEpisodes
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
    api_instance = jikan_openapi.WatchApi(api_client)

    try:
        api_response = api_instance.get_watch_popular_episodes()
        print("The response of WatchApi->get_watch_popular_episodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WatchApi->get_watch_popular_episodes: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**WatchEpisodes**](WatchEpisodes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns Popular Episodes |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_watch_popular_promos**
> WatchPromos get_watch_popular_promos()



### Example


```python
import jikan_openapi
from jikan_openapi.models.watch_promos import WatchPromos
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
    api_instance = jikan_openapi.WatchApi(api_client)

    try:
        api_response = api_instance.get_watch_popular_promos()
        print("The response of WatchApi->get_watch_popular_promos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WatchApi->get_watch_popular_promos: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**WatchPromos**](WatchPromos.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns Popular Promotional Videos |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_watch_recent_episodes**
> WatchEpisodes get_watch_recent_episodes()



### Example


```python
import jikan_openapi
from jikan_openapi.models.watch_episodes import WatchEpisodes
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
    api_instance = jikan_openapi.WatchApi(api_client)

    try:
        api_response = api_instance.get_watch_recent_episodes()
        print("The response of WatchApi->get_watch_recent_episodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WatchApi->get_watch_recent_episodes: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**WatchEpisodes**](WatchEpisodes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns Recently Added Episodes |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_watch_recent_promos**
> WatchPromos get_watch_recent_promos(page=page)



### Example


```python
import jikan_openapi
from jikan_openapi.models.watch_promos import WatchPromos
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
    api_instance = jikan_openapi.WatchApi(api_client)
    page = 56 # int |  (optional)

    try:
        api_response = api_instance.get_watch_recent_promos(page=page)
        print("The response of WatchApi->get_watch_recent_promos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WatchApi->get_watch_recent_promos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 

### Return type

[**WatchPromos**](WatchPromos.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns Recently Added Promotional Videos |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

