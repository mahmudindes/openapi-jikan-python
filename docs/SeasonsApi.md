# jikan_openapi.SeasonsApi

All URIs are relative to *https://api.jikan.moe/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_season**](SeasonsApi.md#get_season) | **GET** /seasons/{year}/{season} | 
[**get_season_now**](SeasonsApi.md#get_season_now) | **GET** /seasons/now | 
[**get_season_upcoming**](SeasonsApi.md#get_season_upcoming) | **GET** /seasons/upcoming | 
[**get_seasons_list**](SeasonsApi.md#get_seasons_list) | **GET** /seasons | 


# **get_season**
> AnimeSearch get_season(year, season, filter=filter, sfw=sfw, unapproved=unapproved, continuing=continuing, page=page, limit=limit)



### Example


```python
import jikan_openapi
from jikan_openapi.models.anime_search import AnimeSearch
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
    api_instance = jikan_openapi.SeasonsApi(api_client)
    year = 56 # int | 
    season = 'season_example' # str | 
    filter = 'filter_example' # str | Entry types (optional)
    sfw = True # bool | 'Safe For Work'. This is a flag. When supplied it will filter out entries according to the SFW Policy. You do not need to pass a value to it. e.g usage: `?sfw` (optional)
    unapproved = True # bool | This is a flag. When supplied it will include entries which are unapproved. Unapproved entries on MyAnimeList are those that are user submitted and have not yet been approved by MAL to show up on other pages. They will have their own specifc pages and are often removed resulting in a 404 error. You do not need to pass a value to it. e.g usage: `?unapproved` (optional)
    continuing = True # bool | This is a flag. When supplied it will include entries which are continuing from previous seasons. MAL includes these items on the seasons view in the &#8243;TV (continuing)&#8243; section. (Example: https://myanimelist.net/anime/season/2024/winter) <br />Example usage: `?continuing` (optional)
    page = 56 # int |  (optional)
    limit = 56 # int |  (optional)

    try:
        api_response = api_instance.get_season(year, season, filter=filter, sfw=sfw, unapproved=unapproved, continuing=continuing, page=page, limit=limit)
        print("The response of SeasonsApi->get_season:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SeasonsApi->get_season: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**|  | 
 **season** | **str**|  | 
 **filter** | **str**| Entry types | [optional] 
 **sfw** | **bool**| &#39;Safe For Work&#39;. This is a flag. When supplied it will filter out entries according to the SFW Policy. You do not need to pass a value to it. e.g usage: &#x60;?sfw&#x60; | [optional] 
 **unapproved** | **bool**| This is a flag. When supplied it will include entries which are unapproved. Unapproved entries on MyAnimeList are those that are user submitted and have not yet been approved by MAL to show up on other pages. They will have their own specifc pages and are often removed resulting in a 404 error. You do not need to pass a value to it. e.g usage: &#x60;?unapproved&#x60; | [optional] 
 **continuing** | **bool**| This is a flag. When supplied it will include entries which are continuing from previous seasons. MAL includes these items on the seasons view in the &amp;#8243;TV (continuing)&amp;#8243; section. (Example: https://myanimelist.net/anime/season/2024/winter) &lt;br /&gt;Example usage: &#x60;?continuing&#x60; | [optional] 
 **page** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 

### Return type

[**AnimeSearch**](AnimeSearch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns seasonal anime |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_season_now**
> AnimeSearch get_season_now(filter=filter, sfw=sfw, unapproved=unapproved, continuing=continuing, page=page, limit=limit)



### Example


```python
import jikan_openapi
from jikan_openapi.models.anime_search import AnimeSearch
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
    api_instance = jikan_openapi.SeasonsApi(api_client)
    filter = 'filter_example' # str | Entry types (optional)
    sfw = True # bool | 'Safe For Work'. This is a flag. When supplied it will filter out entries according to the SFW Policy. You do not need to pass a value to it. e.g usage: `?sfw` (optional)
    unapproved = True # bool | This is a flag. When supplied it will include entries which are unapproved. Unapproved entries on MyAnimeList are those that are user submitted and have not yet been approved by MAL to show up on other pages. They will have their own specifc pages and are often removed resulting in a 404 error. You do not need to pass a value to it. e.g usage: `?unapproved` (optional)
    continuing = True # bool | This is a flag. When supplied it will include entries which are continuing from previous seasons. MAL includes these items on the seasons view in the &#8243;TV (continuing)&#8243; section. (Example: https://myanimelist.net/anime/season/2024/winter) <br />Example usage: `?continuing` (optional)
    page = 56 # int |  (optional)
    limit = 56 # int |  (optional)

    try:
        api_response = api_instance.get_season_now(filter=filter, sfw=sfw, unapproved=unapproved, continuing=continuing, page=page, limit=limit)
        print("The response of SeasonsApi->get_season_now:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SeasonsApi->get_season_now: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Entry types | [optional] 
 **sfw** | **bool**| &#39;Safe For Work&#39;. This is a flag. When supplied it will filter out entries according to the SFW Policy. You do not need to pass a value to it. e.g usage: &#x60;?sfw&#x60; | [optional] 
 **unapproved** | **bool**| This is a flag. When supplied it will include entries which are unapproved. Unapproved entries on MyAnimeList are those that are user submitted and have not yet been approved by MAL to show up on other pages. They will have their own specifc pages and are often removed resulting in a 404 error. You do not need to pass a value to it. e.g usage: &#x60;?unapproved&#x60; | [optional] 
 **continuing** | **bool**| This is a flag. When supplied it will include entries which are continuing from previous seasons. MAL includes these items on the seasons view in the &amp;#8243;TV (continuing)&amp;#8243; section. (Example: https://myanimelist.net/anime/season/2024/winter) &lt;br /&gt;Example usage: &#x60;?continuing&#x60; | [optional] 
 **page** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 

### Return type

[**AnimeSearch**](AnimeSearch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns current seasonal anime |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_season_upcoming**
> AnimeSearch get_season_upcoming(filter=filter, sfw=sfw, unapproved=unapproved, continuing=continuing, page=page, limit=limit)



### Example


```python
import jikan_openapi
from jikan_openapi.models.anime_search import AnimeSearch
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
    api_instance = jikan_openapi.SeasonsApi(api_client)
    filter = 'filter_example' # str | Entry types (optional)
    sfw = True # bool | 'Safe For Work'. This is a flag. When supplied it will filter out entries according to the SFW Policy. You do not need to pass a value to it. e.g usage: `?sfw` (optional)
    unapproved = True # bool | This is a flag. When supplied it will include entries which are unapproved. Unapproved entries on MyAnimeList are those that are user submitted and have not yet been approved by MAL to show up on other pages. They will have their own specifc pages and are often removed resulting in a 404 error. You do not need to pass a value to it. e.g usage: `?unapproved` (optional)
    continuing = True # bool | This is a flag. When supplied it will include entries which are continuing from previous seasons. MAL includes these items on the seasons view in the &#8243;TV (continuing)&#8243; section. (Example: https://myanimelist.net/anime/season/2024/winter) <br />Example usage: `?continuing` (optional)
    page = 56 # int |  (optional)
    limit = 56 # int |  (optional)

    try:
        api_response = api_instance.get_season_upcoming(filter=filter, sfw=sfw, unapproved=unapproved, continuing=continuing, page=page, limit=limit)
        print("The response of SeasonsApi->get_season_upcoming:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SeasonsApi->get_season_upcoming: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Entry types | [optional] 
 **sfw** | **bool**| &#39;Safe For Work&#39;. This is a flag. When supplied it will filter out entries according to the SFW Policy. You do not need to pass a value to it. e.g usage: &#x60;?sfw&#x60; | [optional] 
 **unapproved** | **bool**| This is a flag. When supplied it will include entries which are unapproved. Unapproved entries on MyAnimeList are those that are user submitted and have not yet been approved by MAL to show up on other pages. They will have their own specifc pages and are often removed resulting in a 404 error. You do not need to pass a value to it. e.g usage: &#x60;?unapproved&#x60; | [optional] 
 **continuing** | **bool**| This is a flag. When supplied it will include entries which are continuing from previous seasons. MAL includes these items on the seasons view in the &amp;#8243;TV (continuing)&amp;#8243; section. (Example: https://myanimelist.net/anime/season/2024/winter) &lt;br /&gt;Example usage: &#x60;?continuing&#x60; | [optional] 
 **page** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 

### Return type

[**AnimeSearch**](AnimeSearch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns upcoming season&#39;s anime |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_seasons_list**
> Seasons get_seasons_list()



### Example


```python
import jikan_openapi
from jikan_openapi.models.seasons import Seasons
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
    api_instance = jikan_openapi.SeasonsApi(api_client)

    try:
        api_response = api_instance.get_seasons_list()
        print("The response of SeasonsApi->get_seasons_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SeasonsApi->get_seasons_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Seasons**](Seasons.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns available list of seasons |  -  |
**400** | Error: Bad request. When required parameters were not supplied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

