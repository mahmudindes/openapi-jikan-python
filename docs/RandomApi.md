# jikan_openapi.RandomApi

All URIs are relative to *https://api.jikan.moe/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_random_anime**](RandomApi.md#get_random_anime) | **GET** /random/anime | 
[**get_random_characters**](RandomApi.md#get_random_characters) | **GET** /random/characters | 
[**get_random_manga**](RandomApi.md#get_random_manga) | **GET** /random/manga | 
[**get_random_people**](RandomApi.md#get_random_people) | **GET** /random/people | 
[**get_random_users**](RandomApi.md#get_random_users) | **GET** /random/users | 


# **get_random_anime**
> GetAnimeById200Response get_random_anime()



### Example


```python
import jikan_openapi
from jikan_openapi.models.get_anime_by_id200_response import GetAnimeById200Response
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
    api_instance = jikan_openapi.RandomApi(api_client)

    try:
        api_response = api_instance.get_random_anime()
        print("The response of RandomApi->get_random_anime:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RandomApi->get_random_anime: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetAnimeById200Response**](GetAnimeById200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a random anime resource |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_random_characters**
> GetCharacterById200Response get_random_characters()



### Example


```python
import jikan_openapi
from jikan_openapi.models.get_character_by_id200_response import GetCharacterById200Response
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
    api_instance = jikan_openapi.RandomApi(api_client)

    try:
        api_response = api_instance.get_random_characters()
        print("The response of RandomApi->get_random_characters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RandomApi->get_random_characters: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetCharacterById200Response**](GetCharacterById200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a random character resource |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_random_manga**
> GetMangaById200Response get_random_manga()



### Example


```python
import jikan_openapi
from jikan_openapi.models.get_manga_by_id200_response import GetMangaById200Response
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
    api_instance = jikan_openapi.RandomApi(api_client)

    try:
        api_response = api_instance.get_random_manga()
        print("The response of RandomApi->get_random_manga:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RandomApi->get_random_manga: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetMangaById200Response**](GetMangaById200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a random manga resource |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_random_people**
> GetPersonById200Response get_random_people()



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
    api_instance = jikan_openapi.RandomApi(api_client)

    try:
        api_response = api_instance.get_random_people()
        print("The response of RandomApi->get_random_people:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RandomApi->get_random_people: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**200** | Returns a random person resource |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_random_users**
> GetRandomUsers200Response get_random_users()



### Example


```python
import jikan_openapi
from jikan_openapi.models.get_random_users200_response import GetRandomUsers200Response
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
    api_instance = jikan_openapi.RandomApi(api_client)

    try:
        api_response = api_instance.get_random_users()
        print("The response of RandomApi->get_random_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RandomApi->get_random_users: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetRandomUsers200Response**](GetRandomUsers200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a random user profile resource |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

