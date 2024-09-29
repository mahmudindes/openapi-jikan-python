# jikan_openapi.CharactersApi

All URIs are relative to *https://api.jikan.moe/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_character_anime**](CharactersApi.md#get_character_anime) | **GET** /characters/{id}/anime | 
[**get_character_by_id**](CharactersApi.md#get_character_by_id) | **GET** /characters/{id} | 
[**get_character_full_by_id**](CharactersApi.md#get_character_full_by_id) | **GET** /characters/{id}/full | 
[**get_character_manga**](CharactersApi.md#get_character_manga) | **GET** /characters/{id}/manga | 
[**get_character_pictures**](CharactersApi.md#get_character_pictures) | **GET** /characters/{id}/pictures | 
[**get_character_voice_actors**](CharactersApi.md#get_character_voice_actors) | **GET** /characters/{id}/voices | 
[**get_characters_search**](CharactersApi.md#get_characters_search) | **GET** /characters | 


# **get_character_anime**
> CharacterAnime get_character_anime(id)



### Example


```python
import jikan_openapi
from jikan_openapi.models.character_anime import CharacterAnime
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
    api_instance = jikan_openapi.CharactersApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_character_anime(id)
        print("The response of CharactersApi->get_character_anime:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CharactersApi->get_character_anime: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**CharacterAnime**](CharacterAnime.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns anime that character is in |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_character_by_id**
> GetCharacterById200Response get_character_by_id(id)



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
    api_instance = jikan_openapi.CharactersApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_character_by_id(id)
        print("The response of CharactersApi->get_character_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CharactersApi->get_character_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

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
**200** | Returns character resource |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_character_full_by_id**
> GetCharacterFullById200Response get_character_full_by_id(id)



### Example


```python
import jikan_openapi
from jikan_openapi.models.get_character_full_by_id200_response import GetCharacterFullById200Response
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
    api_instance = jikan_openapi.CharactersApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_character_full_by_id(id)
        print("The response of CharactersApi->get_character_full_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CharactersApi->get_character_full_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**GetCharacterFullById200Response**](GetCharacterFullById200Response.md)

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

# **get_character_manga**
> CharacterManga get_character_manga(id)



### Example


```python
import jikan_openapi
from jikan_openapi.models.character_manga import CharacterManga
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
    api_instance = jikan_openapi.CharactersApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_character_manga(id)
        print("The response of CharactersApi->get_character_manga:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CharactersApi->get_character_manga: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**CharacterManga**](CharacterManga.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns manga that character is in |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_character_pictures**
> CharacterPictures get_character_pictures(id)



### Example


```python
import jikan_openapi
from jikan_openapi.models.character_pictures import CharacterPictures
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
    api_instance = jikan_openapi.CharactersApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_character_pictures(id)
        print("The response of CharactersApi->get_character_pictures:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CharactersApi->get_character_pictures: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**CharacterPictures**](CharacterPictures.md)

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

# **get_character_voice_actors**
> CharacterVoiceActors get_character_voice_actors(id)



### Example


```python
import jikan_openapi
from jikan_openapi.models.character_voice_actors import CharacterVoiceActors
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
    api_instance = jikan_openapi.CharactersApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_character_voice_actors(id)
        print("The response of CharactersApi->get_character_voice_actors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CharactersApi->get_character_voice_actors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**CharacterVoiceActors**](CharacterVoiceActors.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the character&#39;s voice actors |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_characters_search**
> CharactersSearch get_characters_search(page=page, limit=limit, q=q, order_by=order_by, sort=sort, letter=letter)



### Example


```python
import jikan_openapi
from jikan_openapi.models.characters_search import CharactersSearch
from jikan_openapi.models.characters_search_query_orderby import CharactersSearchQueryOrderby
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
    api_instance = jikan_openapi.CharactersApi(api_client)
    page = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    q = 'q_example' # str |  (optional)
    order_by = jikan_openapi.CharactersSearchQueryOrderby() # CharactersSearchQueryOrderby |  (optional)
    sort = jikan_openapi.SearchQuerySort() # SearchQuerySort |  (optional)
    letter = 'letter_example' # str | Return entries starting with the given letter (optional)

    try:
        api_response = api_instance.get_characters_search(page=page, limit=limit, q=q, order_by=order_by, sort=sort, letter=letter)
        print("The response of CharactersApi->get_characters_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CharactersApi->get_characters_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **q** | **str**|  | [optional] 
 **order_by** | [**CharactersSearchQueryOrderby**](.md)|  | [optional] 
 **sort** | [**SearchQuerySort**](.md)|  | [optional] 
 **letter** | **str**| Return entries starting with the given letter | [optional] 

### Return type

[**CharactersSearch**](CharactersSearch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns search results for characters |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

