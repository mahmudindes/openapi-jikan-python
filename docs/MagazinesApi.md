# jikan_openapi.MagazinesApi

All URIs are relative to *https://api.jikan.moe/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_magazines**](MagazinesApi.md#get_magazines) | **GET** /magazines | 


# **get_magazines**
> Magazines get_magazines(page=page, limit=limit, q=q, order_by=order_by, sort=sort, letter=letter)



### Example


```python
import jikan_openapi
from jikan_openapi.models.magazines import Magazines
from jikan_openapi.models.magazines_query_orderby import MagazinesQueryOrderby
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
    api_instance = jikan_openapi.MagazinesApi(api_client)
    page = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    q = 'q_example' # str |  (optional)
    order_by = jikan_openapi.MagazinesQueryOrderby() # MagazinesQueryOrderby |  (optional)
    sort = jikan_openapi.SearchQuerySort() # SearchQuerySort |  (optional)
    letter = 'letter_example' # str | Return entries starting with the given letter (optional)

    try:
        api_response = api_instance.get_magazines(page=page, limit=limit, q=q, order_by=order_by, sort=sort, letter=letter)
        print("The response of MagazinesApi->get_magazines:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MagazinesApi->get_magazines: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **q** | **str**|  | [optional] 
 **order_by** | [**MagazinesQueryOrderby**](.md)|  | [optional] 
 **sort** | [**SearchQuerySort**](.md)|  | [optional] 
 **letter** | **str**| Return entries starting with the given letter | [optional] 

### Return type

[**Magazines**](Magazines.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns magazines collection |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

