# UsersTempDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mal_id** | **int** | MyAnimeList ID | [optional] 
**username** | **str** | MyAnimeList Username | [optional] 
**url** | **str** | MyAnimeList URL | [optional] 
**images** | [**UsersTempDataInnerImages**](UsersTempDataInnerImages.md) |  | [optional] 
**last_online** | **str** | Last Online Date ISO8601 | [optional] 
**gender** | **str** | User Gender | [optional] 
**birthday** | **str** | Birthday Date ISO8601 | [optional] 
**location** | **str** | Location | [optional] 
**joined** | **str** | Joined Date ISO8601 | [optional] 
**anime_stats** | [**UsersTempDataInnerAnimeStats**](UsersTempDataInnerAnimeStats.md) |  | [optional] 
**manga_stats** | [**UsersTempDataInnerMangaStats**](UsersTempDataInnerMangaStats.md) |  | [optional] 
**favorites** | [**UsersTempDataInnerFavorites**](UsersTempDataInnerFavorites.md) |  | [optional] 
**about** | **str** | User About. NOTE: About information is customizable by users through BBCode on MyAnimeList. This means users can add multimedia content, different text sizes, etc. Due to this freeform, Jikan returns parsed HTML. Validate on your end! | [optional] 

## Example

```python
from jikan_openapi.models.users_temp_data_inner import UsersTempDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of UsersTempDataInner from a JSON string
users_temp_data_inner_instance = UsersTempDataInner.from_json(json)
# print the JSON string representation of the object
print(UsersTempDataInner.to_json())

# convert the object into a dict
users_temp_data_inner_dict = users_temp_data_inner_instance.to_dict()
# create an instance of UsersTempDataInner from a dict
users_temp_data_inner_form_dict = users_temp_data_inner.from_dict(users_temp_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


