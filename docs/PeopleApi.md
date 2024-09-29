# jikan_openapi.PeopleApi

All URIs are relative to *https://api.jikan.moe/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_people_search**](PeopleApi.md#get_people_search) | **GET** /people | 
[**get_person_anime**](PeopleApi.md#get_person_anime) | **GET** /people/{id}/anime | 
[**get_person_by_id**](PeopleApi.md#get_person_by_id) | **GET** /people/{id} | 
[**get_person_full_by_id**](PeopleApi.md#get_person_full_by_id) | **GET** /people/{id}/full | 
[**get_person_manga**](PeopleApi.md#get_person_manga) | **GET** /people/{id}/manga | 
[**get_person_pictures**](PeopleApi.md#get_person_pictures) | **GET** /people/{id}/pictures | 
[**get_person_voices**](PeopleApi.md#get_person_voices) | **GET** /people/{id}/voices | 


# **get_people_search**
> PeopleSearch get_people_search(page=page, limit=limit, q=q, order_by=order_by, sort=sort, letter=letter)



### Example


```python
import jikan_openapi
from jikan_openapi.models.people_search import PeopleSearch
from jikan_openapi.models.people_search_query_orderby import PeopleSearchQueryOrderby
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
    api_instance = jikan_openapi.PeopleApi(api_client)
    page = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    q = 'q_example' # str |  (optional)
    order_by = jikan_openapi.PeopleSearchQueryOrderby() # PeopleSearchQueryOrderby |  (optional)
    sort = jikan_openapi.SearchQuerySort() # SearchQuerySort |  (optional)
    letter = 'letter_example' # str | Return entries starting with the given letter (optional)

    try:
        api_response = api_instance.get_people_search(page=page, limit=limit, q=q, order_by=order_by, sort=sort, letter=letter)
        print("The response of PeopleApi->get_people_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PeopleApi->get_people_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **q** | **str**|  | [optional] 
 **order_by** | [**PeopleSearchQueryOrderby**](.md)|  | [optional] 
 **sort** | [**SearchQuerySort**](.md)|  | [optional] 
 **letter** | **str**| Return entries starting with the given letter | [optional] 

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
**200** | Returns search results for people |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_person_anime**
> PersonAnime get_person_anime(id)



### Example


```python
import jikan_openapi
from jikan_openapi.models.person_anime import PersonAnime
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
    api_instance = jikan_openapi.PeopleApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_person_anime(id)
        print("The response of PeopleApi->get_person_anime:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PeopleApi->get_person_anime: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**PersonAnime**](PersonAnime.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns person&#39;s anime staff positions |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_person_by_id**
> GetPersonById200Response get_person_by_id(id)



### Example


```python
import jikan_openapi
from jikan_openapi.models.get_person_by_id200_response import GetPersonById200Response
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
    api_instance = jikan_openapi.PeopleApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_person_by_id(id)
        print("The response of PeopleApi->get_person_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PeopleApi->get_person_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**GetPersonById200Response**](GetPersonById200Response.md)

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

# **get_person_full_by_id**
> GetPersonFullById200Response get_person_full_by_id(id)



### Example


```python
import jikan_openapi
from jikan_openapi.models.get_person_full_by_id200_response import GetPersonFullById200Response
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
    api_instance = jikan_openapi.PeopleApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_person_full_by_id(id)
        print("The response of PeopleApi->get_person_full_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PeopleApi->get_person_full_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**GetPersonFullById200Response**](GetPersonFullById200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns complete character resource data |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_person_manga**
> PersonManga get_person_manga(id)



### Example


```python
import jikan_openapi
from jikan_openapi.models.person_manga import PersonManga
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
    api_instance = jikan_openapi.PeopleApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_person_manga(id)
        print("The response of PeopleApi->get_person_manga:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PeopleApi->get_person_manga: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**PersonManga**](PersonManga.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns person&#39;s published manga works |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_person_pictures**
> PersonPictures get_person_pictures(id)



### Example


```python
import jikan_openapi
from jikan_openapi.models.person_pictures import PersonPictures
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
    api_instance = jikan_openapi.PeopleApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_person_pictures(id)
        print("The response of PeopleApi->get_person_pictures:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PeopleApi->get_person_pictures: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**PersonPictures**](PersonPictures.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of pictures of the person |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_person_voices**
> PersonVoiceActingRoles get_person_voices(id)



### Example


```python
import jikan_openapi
from jikan_openapi.models.person_voice_acting_roles import PersonVoiceActingRoles
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
    api_instance = jikan_openapi.PeopleApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_person_voices(id)
        print("The response of PeopleApi->get_person_voices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PeopleApi->get_person_voices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**PersonVoiceActingRoles**](PersonVoiceActingRoles.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns person&#39;s voice acting roles |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

