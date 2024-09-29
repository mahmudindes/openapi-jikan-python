# UserFavoritesCharactersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mal_id** | **int** | MyAnimeList ID | [optional] 
**url** | **str** | MyAnimeList URL | [optional] 
**images** | [**CharacterImages**](CharacterImages.md) |  | [optional] 
**name** | **str** | Entry name | [optional] 
**type** | **str** | Type of resource | [optional] 
**title** | **str** | Resource Name/Title | [optional] 

## Example

```python
from jikan_openapi.models.user_favorites_characters_inner import UserFavoritesCharactersInner

# TODO update the JSON string below
json = "{}"
# create an instance of UserFavoritesCharactersInner from a JSON string
user_favorites_characters_inner_instance = UserFavoritesCharactersInner.from_json(json)
# print the JSON string representation of the object
print(UserFavoritesCharactersInner.to_json())

# convert the object into a dict
user_favorites_characters_inner_dict = user_favorites_characters_inner_instance.to_dict()
# create an instance of UserFavoritesCharactersInner from a dict
user_favorites_characters_inner_form_dict = user_favorites_characters_inner.from_dict(user_favorites_characters_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


