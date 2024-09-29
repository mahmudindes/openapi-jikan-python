# jikan_openapi.UsersApi

All URIs are relative to *https://api.jikan.moe/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_about**](UsersApi.md#get_user_about) | **GET** /users/{username}/about | 
[**get_user_animelist**](UsersApi.md#get_user_animelist) | **GET** /users/{username}/animelist | 
[**get_user_by_id**](UsersApi.md#get_user_by_id) | **GET** /users/userbyid/{id} | 
[**get_user_clubs**](UsersApi.md#get_user_clubs) | **GET** /users/{username}/clubs | 
[**get_user_external**](UsersApi.md#get_user_external) | **GET** /users/{username}/external | 
[**get_user_favorites**](UsersApi.md#get_user_favorites) | **GET** /users/{username}/favorites | 
[**get_user_friends**](UsersApi.md#get_user_friends) | **GET** /users/{username}/friends | 
[**get_user_full_profile**](UsersApi.md#get_user_full_profile) | **GET** /users/{username}/full | 
[**get_user_history**](UsersApi.md#get_user_history) | **GET** /users/{username}/history | 
[**get_user_manga_list**](UsersApi.md#get_user_manga_list) | **GET** /users/{username}/mangalist | 
[**get_user_profile**](UsersApi.md#get_user_profile) | **GET** /users/{username} | 
[**get_user_recommendations**](UsersApi.md#get_user_recommendations) | **GET** /users/{username}/recommendations | 
[**get_user_reviews**](UsersApi.md#get_user_reviews) | **GET** /users/{username}/reviews | 
[**get_user_statistics**](UsersApi.md#get_user_statistics) | **GET** /users/{username}/statistics | 
[**get_user_updates**](UsersApi.md#get_user_updates) | **GET** /users/{username}/userupdates | 
[**get_users_search**](UsersApi.md#get_users_search) | **GET** /users | 


# **get_user_about**
> UserAbout get_user_about(username)



### Example


```python
import jikan_openapi
from jikan_openapi.models.user_about import UserAbout
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
    api_instance = jikan_openapi.UsersApi(api_client)
    username = 'username_example' # str | 

    try:
        api_response = api_instance.get_user_about(username)
        print("The response of UsersApi->get_user_about:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_about: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 

### Return type

[**UserAbout**](UserAbout.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns user about in raw HTML |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_animelist**
> object get_user_animelist(username, status=status)



User Anime lists have been discontinued since May 1st, 2022. <a href='https://docs.google.com/document/d/1-6H-agSnqa8Mfmw802UYfGQrceIEnAaEh4uCXAPiX5A'>Read more</a>

### Example


```python
import jikan_openapi
from jikan_openapi.models.user_anime_list_status_filter import UserAnimeListStatusFilter
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
    api_instance = jikan_openapi.UsersApi(api_client)
    username = 'username_example' # str | 
    status = jikan_openapi.UserAnimeListStatusFilter() # UserAnimeListStatusFilter |  (optional)

    try:
        api_response = api_instance.get_user_animelist(username, status=status)
        print("The response of UsersApi->get_user_animelist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_animelist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **status** | [**UserAnimeListStatusFilter**](.md)|  | [optional] 

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
**200** | Returns user anime list |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_by_id**
> GetUserById200Response get_user_by_id(id)



### Example


```python
import jikan_openapi
from jikan_openapi.models.get_user_by_id200_response import GetUserById200Response
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
    api_instance = jikan_openapi.UsersApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_user_by_id(id)
        print("The response of UsersApi->get_user_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**GetUserById200Response**](GetUserById200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns username by ID search |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_clubs**
> UserClubs get_user_clubs(username, page=page)



### Example


```python
import jikan_openapi
from jikan_openapi.models.user_clubs import UserClubs
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
    api_instance = jikan_openapi.UsersApi(api_client)
    username = 'username_example' # str | 
    page = 56 # int |  (optional)

    try:
        api_response = api_instance.get_user_clubs(username, page=page)
        print("The response of UsersApi->get_user_clubs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_clubs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **page** | **int**|  | [optional] 

### Return type

[**UserClubs**](UserClubs.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns user clubs |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_external**
> ExternalLinks get_user_external(username)



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
    api_instance = jikan_openapi.UsersApi(api_client)
    username = 'username_example' # str | 

    try:
        api_response = api_instance.get_user_external(username)
        print("The response of UsersApi->get_user_external:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_external: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 

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
**200** | Returns user&#39;s external links |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_favorites**
> GetUserFavorites200Response get_user_favorites(username)



### Example


```python
import jikan_openapi
from jikan_openapi.models.get_user_favorites200_response import GetUserFavorites200Response
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
    api_instance = jikan_openapi.UsersApi(api_client)
    username = 'username_example' # str | 

    try:
        api_response = api_instance.get_user_favorites(username)
        print("The response of UsersApi->get_user_favorites:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_favorites: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 

### Return type

[**GetUserFavorites200Response**](GetUserFavorites200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns user favorites |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_friends**
> UserFriends get_user_friends(username, page=page)



### Example


```python
import jikan_openapi
from jikan_openapi.models.user_friends import UserFriends
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
    api_instance = jikan_openapi.UsersApi(api_client)
    username = 'username_example' # str | 
    page = 56 # int |  (optional)

    try:
        api_response = api_instance.get_user_friends(username, page=page)
        print("The response of UsersApi->get_user_friends:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_friends: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **page** | **int**|  | [optional] 

### Return type

[**UserFriends**](UserFriends.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns user friends |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_full_profile**
> GetUserFullProfile200Response get_user_full_profile(username)



### Example


```python
import jikan_openapi
from jikan_openapi.models.get_user_full_profile200_response import GetUserFullProfile200Response
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
    api_instance = jikan_openapi.UsersApi(api_client)
    username = 'username_example' # str | 

    try:
        api_response = api_instance.get_user_full_profile(username)
        print("The response of UsersApi->get_user_full_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_full_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 

### Return type

[**GetUserFullProfile200Response**](GetUserFullProfile200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns complete user resource data |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_history**
> UserHistory get_user_history(username, type=type)



### Example


```python
import jikan_openapi
from jikan_openapi.models.user_history import UserHistory
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
    api_instance = jikan_openapi.UsersApi(api_client)
    username = 'username_example' # str | 
    type = 'type_example' # str |  (optional)

    try:
        api_response = api_instance.get_user_history(username, type=type)
        print("The response of UsersApi->get_user_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **type** | **str**|  | [optional] 

### Return type

[**UserHistory**](UserHistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns user history (past 30 days) |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_manga_list**
> object get_user_manga_list(username, status=status)



User Manga lists have been discontinued since May 1st, 2022. <a href='https://docs.google.com/document/d/1-6H-agSnqa8Mfmw802UYfGQrceIEnAaEh4uCXAPiX5A'>Read more</a>

### Example


```python
import jikan_openapi
from jikan_openapi.models.user_manga_list_status_filter import UserMangaListStatusFilter
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
    api_instance = jikan_openapi.UsersApi(api_client)
    username = 'username_example' # str | 
    status = jikan_openapi.UserMangaListStatusFilter() # UserMangaListStatusFilter |  (optional)

    try:
        api_response = api_instance.get_user_manga_list(username, status=status)
        print("The response of UsersApi->get_user_manga_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_manga_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **status** | [**UserMangaListStatusFilter**](.md)|  | [optional] 

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
**200** | Returns user manga list |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_profile**
> GetRandomUsers200Response get_user_profile(username)



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
    api_instance = jikan_openapi.UsersApi(api_client)
    username = 'username_example' # str | 

    try:
        api_response = api_instance.get_user_profile(username)
        print("The response of UsersApi->get_user_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 

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
**200** | Returns user profile |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_recommendations**
> Recommendations get_user_recommendations(username, page=page)



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
    api_instance = jikan_openapi.UsersApi(api_client)
    username = 'username_example' # str | 
    page = 56 # int |  (optional)

    try:
        api_response = api_instance.get_user_recommendations(username, page=page)
        print("The response of UsersApi->get_user_recommendations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_recommendations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
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
**200** | Returns Recent Anime Recommendations |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_reviews**
> GetTopReviews200Response get_user_reviews(username, page=page)



### Example


```python
import jikan_openapi
from jikan_openapi.models.get_top_reviews200_response import GetTopReviews200Response
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
    api_instance = jikan_openapi.UsersApi(api_client)
    username = 'username_example' # str | 
    page = 56 # int |  (optional)

    try:
        api_response = api_instance.get_user_reviews(username, page=page)
        print("The response of UsersApi->get_user_reviews:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_reviews: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **page** | **int**|  | [optional] 

### Return type

[**GetTopReviews200Response**](GetTopReviews200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns user reviews |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_statistics**
> UserStatistics get_user_statistics(username)



### Example


```python
import jikan_openapi
from jikan_openapi.models.user_statistics import UserStatistics
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
    api_instance = jikan_openapi.UsersApi(api_client)
    username = 'username_example' # str | 

    try:
        api_response = api_instance.get_user_statistics(username)
        print("The response of UsersApi->get_user_statistics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_statistics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 

### Return type

[**UserStatistics**](UserStatistics.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns user statistics |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_updates**
> UserUpdates get_user_updates(username)



### Example


```python
import jikan_openapi
from jikan_openapi.models.user_updates import UserUpdates
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
    api_instance = jikan_openapi.UsersApi(api_client)
    username = 'username_example' # str | 

    try:
        api_response = api_instance.get_user_updates(username)
        print("The response of UsersApi->get_user_updates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_updates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 

### Return type

[**UserUpdates**](UserUpdates.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns user updates |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_search**
> UsersSearch get_users_search(page=page, limit=limit, q=q, gender=gender, location=location, max_age=max_age, min_age=min_age)



### Example


```python
import jikan_openapi
from jikan_openapi.models.users_search import UsersSearch
from jikan_openapi.models.users_search_query_gender import UsersSearchQueryGender
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
    api_instance = jikan_openapi.UsersApi(api_client)
    page = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    q = 'q_example' # str |  (optional)
    gender = jikan_openapi.UsersSearchQueryGender() # UsersSearchQueryGender |  (optional)
    location = 'location_example' # str |  (optional)
    max_age = 56 # int |  (optional)
    min_age = 56 # int |  (optional)

    try:
        api_response = api_instance.get_users_search(page=page, limit=limit, q=q, gender=gender, location=location, max_age=max_age, min_age=min_age)
        print("The response of UsersApi->get_users_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_users_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **q** | **str**|  | [optional] 
 **gender** | [**UsersSearchQueryGender**](.md)|  | [optional] 
 **location** | **str**|  | [optional] 
 **max_age** | **int**|  | [optional] 
 **min_age** | **int**|  | [optional] 

### Return type

[**UsersSearch**](UsersSearch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns search results for users |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

