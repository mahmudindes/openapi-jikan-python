# jikan_openapi.SchedulesApi

All URIs are relative to *https://api.jikan.moe/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_schedules**](SchedulesApi.md#get_schedules) | **GET** /schedules | 


# **get_schedules**
> Schedules get_schedules(filter=filter, kids=kids, sfw=sfw, unapproved=unapproved, page=page, limit=limit)



### Example


```python
import jikan_openapi
from jikan_openapi.models.schedules import Schedules
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
    api_instance = jikan_openapi.SchedulesApi(api_client)
    filter = 'filter_example' # str | Filter by day (optional)
    kids = 'kids_example' # str | When supplied, it will filter entries with the `Kids` Genre Demographic. When supplied as `kids=true`, it will return only Kid entries and when supplied as `kids=false`, it will filter out any Kid entries. Defaults to `false`. (optional)
    sfw = 'sfw_example' # str | 'Safe For Work'. When supplied, it will filter entries with the `Hentai` Genre. When supplied as `sfw=true`, it will return only SFW entries and when supplied as `sfw=false`, it will filter out any Hentai entries. Defaults to `false`. (optional)
    unapproved = True # bool | This is a flag. When supplied it will include entries which are unapproved. Unapproved entries on MyAnimeList are those that are user submitted and have not yet been approved by MAL to show up on other pages. They will have their own specifc pages and are often removed resulting in a 404 error. You do not need to pass a value to it. e.g usage: `?unapproved` (optional)
    page = 56 # int |  (optional)
    limit = 56 # int |  (optional)

    try:
        api_response = api_instance.get_schedules(filter=filter, kids=kids, sfw=sfw, unapproved=unapproved, page=page, limit=limit)
        print("The response of SchedulesApi->get_schedules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulesApi->get_schedules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter by day | [optional] 
 **kids** | **str**| When supplied, it will filter entries with the &#x60;Kids&#x60; Genre Demographic. When supplied as &#x60;kids&#x3D;true&#x60;, it will return only Kid entries and when supplied as &#x60;kids&#x3D;false&#x60;, it will filter out any Kid entries. Defaults to &#x60;false&#x60;. | [optional] 
 **sfw** | **str**| &#39;Safe For Work&#39;. When supplied, it will filter entries with the &#x60;Hentai&#x60; Genre. When supplied as &#x60;sfw&#x3D;true&#x60;, it will return only SFW entries and when supplied as &#x60;sfw&#x3D;false&#x60;, it will filter out any Hentai entries. Defaults to &#x60;false&#x60;. | [optional] 
 **unapproved** | **bool**| This is a flag. When supplied it will include entries which are unapproved. Unapproved entries on MyAnimeList are those that are user submitted and have not yet been approved by MAL to show up on other pages. They will have their own specifc pages and are often removed resulting in a 404 error. You do not need to pass a value to it. e.g usage: &#x60;?unapproved&#x60; | [optional] 
 **page** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 

### Return type

[**Schedules**](Schedules.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns weekly schedule |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

