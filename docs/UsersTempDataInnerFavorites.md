# UsersTempDataInnerFavorites

Favorite entries

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anime** | [**List[EntryMeta]**](EntryMeta.md) | Favorite Anime | [optional] 
**manga** | [**List[EntryMeta]**](EntryMeta.md) | Favorite Manga | [optional] 
**characters** | [**List[EntryMeta]**](EntryMeta.md) | Favorite Characters | [optional] 
**people** | [**List[EntryMeta]**](EntryMeta.md) | Favorite People | [optional] 

## Example

```python
from jikan_openapi.models.users_temp_data_inner_favorites import UsersTempDataInnerFavorites

# TODO update the JSON string below
json = "{}"
# create an instance of UsersTempDataInnerFavorites from a JSON string
users_temp_data_inner_favorites_instance = UsersTempDataInnerFavorites.from_json(json)
# print the JSON string representation of the object
print(UsersTempDataInnerFavorites.to_json())

# convert the object into a dict
users_temp_data_inner_favorites_dict = users_temp_data_inner_favorites_instance.to_dict()
# create an instance of UsersTempDataInnerFavorites from a dict
users_temp_data_inner_favorites_form_dict = users_temp_data_inner_favorites.from_dict(users_temp_data_inner_favorites_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


