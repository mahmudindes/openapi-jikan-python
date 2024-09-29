# UserProfileFull

Transform the resource into an array.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mal_id** | **int** | MyAnimeList ID | [optional] 
**username** | **str** | MyAnimeList Username | [optional] 
**url** | **str** | MyAnimeList URL | [optional] 
**images** | [**UserImages**](UserImages.md) |  | [optional] 
**last_online** | **str** | Last Online Date ISO8601 | [optional] 
**gender** | **str** | User Gender | [optional] 
**birthday** | **str** | Birthday Date ISO8601 | [optional] 
**location** | **str** | Location | [optional] 
**joined** | **str** | Joined Date ISO8601 | [optional] 
**statistics** | [**UserProfileFullStatistics**](UserProfileFullStatistics.md) |  | [optional] 
**external** | [**List[AnimeFullExternalInner]**](AnimeFullExternalInner.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.user_profile_full import UserProfileFull

# TODO update the JSON string below
json = "{}"
# create an instance of UserProfileFull from a JSON string
user_profile_full_instance = UserProfileFull.from_json(json)
# print the JSON string representation of the object
print(UserProfileFull.to_json())

# convert the object into a dict
user_profile_full_dict = user_profile_full_instance.to_dict()
# create an instance of UserProfileFull from a dict
user_profile_full_form_dict = user_profile_full.from_dict(user_profile_full_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


