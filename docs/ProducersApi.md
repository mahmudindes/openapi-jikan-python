# jikan_openapi.ProducersApi

All URIs are relative to *https://api.jikan.moe/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_producer_by_id**](ProducersApi.md#get_producer_by_id) | **GET** /producers/{id} | 
[**get_producer_external**](ProducersApi.md#get_producer_external) | **GET** /producers/{id}/external | 
[**get_producer_full_by_id**](ProducersApi.md#get_producer_full_by_id) | **GET** /producers/{id}/full | 
[**get_producers**](ProducersApi.md#get_producers) | **GET** /producers | 


# **get_producer_by_id**
> GetProducerById200Response get_producer_by_id(id)



### Example


```python
import jikan_openapi
from jikan_openapi.models.get_producer_by_id200_response import GetProducerById200Response
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
    api_instance = jikan_openapi.ProducersApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_producer_by_id(id)
        print("The response of ProducersApi->get_producer_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProducersApi->get_producer_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**GetProducerById200Response**](GetProducerById200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns producer resource |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_producer_external**
> ExternalLinks get_producer_external(id)



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
    api_instance = jikan_openapi.ProducersApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_producer_external(id)
        print("The response of ProducersApi->get_producer_external:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProducersApi->get_producer_external: %s\n" % e)
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
**200** | Returns producer&#39;s external links |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_producer_full_by_id**
> GetProducerFullById200Response get_producer_full_by_id(id)



### Example


```python
import jikan_openapi
from jikan_openapi.models.get_producer_full_by_id200_response import GetProducerFullById200Response
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
    api_instance = jikan_openapi.ProducersApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_producer_full_by_id(id)
        print("The response of ProducersApi->get_producer_full_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProducersApi->get_producer_full_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**GetProducerFullById200Response**](GetProducerFullById200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns producer resource |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_producers**
> Producers get_producers(page=page, limit=limit, q=q, order_by=order_by, sort=sort, letter=letter)



### Example


```python
import jikan_openapi
from jikan_openapi.models.producers import Producers
from jikan_openapi.models.producers_query_orderby import ProducersQueryOrderby
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
    api_instance = jikan_openapi.ProducersApi(api_client)
    page = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    q = 'q_example' # str |  (optional)
    order_by = jikan_openapi.ProducersQueryOrderby() # ProducersQueryOrderby |  (optional)
    sort = jikan_openapi.SearchQuerySort() # SearchQuerySort |  (optional)
    letter = 'letter_example' # str | Return entries starting with the given letter (optional)

    try:
        api_response = api_instance.get_producers(page=page, limit=limit, q=q, order_by=order_by, sort=sort, letter=letter)
        print("The response of ProducersApi->get_producers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProducersApi->get_producers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **q** | **str**|  | [optional] 
 **order_by** | [**ProducersQueryOrderby**](.md)|  | [optional] 
 **sort** | [**SearchQuerySort**](.md)|  | [optional] 
 **letter** | **str**| Return entries starting with the given letter | [optional] 

### Return type

[**Producers**](Producers.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns producers collection |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

