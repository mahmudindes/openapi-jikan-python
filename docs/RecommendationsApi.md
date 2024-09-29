# jikan_openapi.RecommendationsApi

All URIs are relative to *https://api.jikan.moe/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_recent_anime_recommendations**](RecommendationsApi.md#get_recent_anime_recommendations) | **GET** /recommendations/anime | 
[**get_recent_manga_recommendations**](RecommendationsApi.md#get_recent_manga_recommendations) | **GET** /recommendations/manga | 


# **get_recent_anime_recommendations**
> Recommendations get_recent_anime_recommendations(page=page)



### Example


```python
import jikan_openapi
from jikan_openapi.models.recommendations import Recommendations
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
    api_instance = jikan_openapi.RecommendationsApi(api_client)
    page = 56 # int |  (optional)

    try:
        api_response = api_instance.get_recent_anime_recommendations(page=page)
        print("The response of RecommendationsApi->get_recent_anime_recommendations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecommendationsApi->get_recent_anime_recommendations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 

### Return type

[**Recommendations**](Recommendations.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns recent anime recommendations |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recent_manga_recommendations**
> Recommendations get_recent_manga_recommendations(page=page)



### Example


```python
import jikan_openapi
from jikan_openapi.models.recommendations import Recommendations
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
    api_instance = jikan_openapi.RecommendationsApi(api_client)
    page = 56 # int |  (optional)

    try:
        api_response = api_instance.get_recent_manga_recommendations(page=page)
        print("The response of RecommendationsApi->get_recent_manga_recommendations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecommendationsApi->get_recent_manga_recommendations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 

### Return type

[**Recommendations**](Recommendations.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns recent manga recommendations |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

