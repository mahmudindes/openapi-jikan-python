# UserUpdatesDataAnimeInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry** | [**AnimeMeta**](AnimeMeta.md) |  | [optional] 
**score** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**episodes_seen** | **int** |  | [optional] 
**episodes_total** | **int** |  | [optional] 
**var_date** | **str** | ISO8601 format | [optional] 

## Example

```python
from jikan_openapi.models.user_updates_data_anime_inner import UserUpdatesDataAnimeInner

# TODO update the JSON string below
json = "{}"
# create an instance of UserUpdatesDataAnimeInner from a JSON string
user_updates_data_anime_inner_instance = UserUpdatesDataAnimeInner.from_json(json)
# print the JSON string representation of the object
print(UserUpdatesDataAnimeInner.to_json())

# convert the object into a dict
user_updates_data_anime_inner_dict = user_updates_data_anime_inner_instance.to_dict()
# create an instance of UserUpdatesDataAnimeInner from a dict
user_updates_data_anime_inner_form_dict = user_updates_data_anime_inner.from_dict(user_updates_data_anime_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


