# jikan_openapi.ClubsApi

All URIs are relative to *https://api.jikan.moe/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_club_members**](ClubsApi.md#get_club_members) | **GET** /clubs/{id}/members | 
[**get_club_relations**](ClubsApi.md#get_club_relations) | **GET** /clubs/{id}/relations | 
[**get_club_staff**](ClubsApi.md#get_club_staff) | **GET** /clubs/{id}/staff | 
[**get_clubs_by_id**](ClubsApi.md#get_clubs_by_id) | **GET** /clubs/{id} | 
[**get_clubs_search**](ClubsApi.md#get_clubs_search) | **GET** /clubs | 


# **get_club_members**
> GetClubMembers200Response get_club_members(id, page=page)



### Example


```python
import jikan_openapi
from jikan_openapi.models.get_club_members200_response import GetClubMembers200Response
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
    api_instance = jikan_openapi.ClubsApi(api_client)
    id = 56 # int | 
    page = 56 # int |  (optional)

    try:
        api_response = api_instance.get_club_members(id, page=page)
        print("The response of ClubsApi->get_club_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubsApi->get_club_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **page** | **int**|  | [optional] 

### Return type

[**GetClubMembers200Response**](GetClubMembers200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns Club Members Resource |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_club_relations**
> ClubRelations get_club_relations(id)



### Example


```python
import jikan_openapi
from jikan_openapi.models.club_relations import ClubRelations
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
    api_instance = jikan_openapi.ClubsApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_club_relations(id)
        print("The response of ClubsApi->get_club_relations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubsApi->get_club_relations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ClubRelations**](ClubRelations.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns Club Relations |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_club_staff**
> ClubStaff get_club_staff(id)



### Example


```python
import jikan_openapi
from jikan_openapi.models.club_staff import ClubStaff
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
    api_instance = jikan_openapi.ClubsApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_club_staff(id)
        print("The response of ClubsApi->get_club_staff:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubsApi->get_club_staff: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ClubStaff**](ClubStaff.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns Club Staff |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clubs_by_id**
> GetClubsById200Response get_clubs_by_id(id)



### Example


```python
import jikan_openapi
from jikan_openapi.models.get_clubs_by_id200_response import GetClubsById200Response
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
    api_instance = jikan_openapi.ClubsApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_clubs_by_id(id)
        print("The response of ClubsApi->get_clubs_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubsApi->get_clubs_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**GetClubsById200Response**](GetClubsById200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns Club Resource |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clubs_search**
> ClubsSearch get_clubs_search(page=page, limit=limit, q=q, type=type, category=category, order_by=order_by, sort=sort, letter=letter)



### Example


```python
import jikan_openapi
from jikan_openapi.models.club_search_query_category import ClubSearchQueryCategory
from jikan_openapi.models.club_search_query_orderby import ClubSearchQueryOrderby
from jikan_openapi.models.club_search_query_type import ClubSearchQueryType
from jikan_openapi.models.clubs_search import ClubsSearch
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
    api_instance = jikan_openapi.ClubsApi(api_client)
    page = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    q = 'q_example' # str |  (optional)
    type = jikan_openapi.ClubSearchQueryType() # ClubSearchQueryType |  (optional)
    category = jikan_openapi.ClubSearchQueryCategory() # ClubSearchQueryCategory |  (optional)
    order_by = jikan_openapi.ClubSearchQueryOrderby() # ClubSearchQueryOrderby |  (optional)
    sort = jikan_openapi.SearchQuerySort() # SearchQuerySort |  (optional)
    letter = 'letter_example' # str | Return entries starting with the given letter (optional)

    try:
        api_response = api_instance.get_clubs_search(page=page, limit=limit, q=q, type=type, category=category, order_by=order_by, sort=sort, letter=letter)
        print("The response of ClubsApi->get_clubs_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubsApi->get_clubs_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **q** | **str**|  | [optional] 
 **type** | [**ClubSearchQueryType**](.md)|  | [optional] 
 **category** | [**ClubSearchQueryCategory**](.md)|  | [optional] 
 **order_by** | [**ClubSearchQueryOrderby**](.md)|  | [optional] 
 **sort** | [**SearchQuerySort**](.md)|  | [optional] 
 **letter** | **str**| Return entries starting with the given letter | [optional] 

### Return type

[**ClubsSearch**](ClubsSearch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns search results for clubs |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

