# jikan_openapi.ReviewsApi

All URIs are relative to *https://api.jikan.moe/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_recent_anime_reviews**](ReviewsApi.md#get_recent_anime_reviews) | **GET** /reviews/anime | 
[**get_recent_manga_reviews**](ReviewsApi.md#get_recent_manga_reviews) | **GET** /reviews/manga | 


# **get_recent_anime_reviews**
> object get_recent_anime_reviews(page=page, preliminary=preliminary, spoilers=spoilers)



### Example


```python
import jikan_openapi
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
    api_instance = jikan_openapi.ReviewsApi(api_client)
    page = 56 # int |  (optional)
    preliminary = True # bool | Any reviews left during an ongoing anime/manga, those reviews are tagged as preliminary. NOTE: Preliminary reviews are not returned by default so if the entry is airing/publishing you need to add this otherwise you will get an empty list. e.g usage: `?preliminary=true` (optional)
    spoilers = True # bool | Any reviews that are tagged as a spoiler. Spoiler reviews are not returned by default. e.g usage: `?spoiler=true` (optional)

    try:
        api_response = api_instance.get_recent_anime_reviews(page=page, preliminary=preliminary, spoilers=spoilers)
        print("The response of ReviewsApi->get_recent_anime_reviews:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReviewsApi->get_recent_anime_reviews: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **preliminary** | **bool**| Any reviews left during an ongoing anime/manga, those reviews are tagged as preliminary. NOTE: Preliminary reviews are not returned by default so if the entry is airing/publishing you need to add this otherwise you will get an empty list. e.g usage: &#x60;?preliminary&#x3D;true&#x60; | [optional] 
 **spoilers** | **bool**| Any reviews that are tagged as a spoiler. Spoiler reviews are not returned by default. e.g usage: &#x60;?spoiler&#x3D;true&#x60; | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns recent anime reviews |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recent_manga_reviews**
> object get_recent_manga_reviews(page=page, preliminary=preliminary, spoilers=spoilers)



### Example


```python
import jikan_openapi
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
    api_instance = jikan_openapi.ReviewsApi(api_client)
    page = 56 # int |  (optional)
    preliminary = True # bool | Any reviews left during an ongoing anime/manga, those reviews are tagged as preliminary. NOTE: Preliminary reviews are not returned by default so if the entry is airing/publishing you need to add this otherwise you will get an empty list. e.g usage: `?preliminary=true` (optional)
    spoilers = True # bool | Any reviews that are tagged as a spoiler. Spoiler reviews are not returned by default. e.g usage: `?spoiler=true` (optional)

    try:
        api_response = api_instance.get_recent_manga_reviews(page=page, preliminary=preliminary, spoilers=spoilers)
        print("The response of ReviewsApi->get_recent_manga_reviews:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReviewsApi->get_recent_manga_reviews: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **preliminary** | **bool**| Any reviews left during an ongoing anime/manga, those reviews are tagged as preliminary. NOTE: Preliminary reviews are not returned by default so if the entry is airing/publishing you need to add this otherwise you will get an empty list. e.g usage: &#x60;?preliminary&#x3D;true&#x60; | [optional] 
 **spoilers** | **bool**| Any reviews that are tagged as a spoiler. Spoiler reviews are not returned by default. e.g usage: &#x60;?spoiler&#x3D;true&#x60; | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns recent manga reviews |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

