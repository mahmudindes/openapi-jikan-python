# UserFavoritesAnimeInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mal_id** | **int** | MyAnimeList ID | [optional] 
**url** | **str** | MyAnimeList URL | [optional] 
**images** | [**AnimeImages**](AnimeImages.md) |  | [optional] 
**title** | **str** | Entry title | [optional] 
**type** | **str** |  | [optional] 
**start_year** | **int** |  | [optional] 

## Example

```python
from jikan_openapi.models.user_favorites_anime_inner import UserFavoritesAnimeInner

# TODO update the JSON string below
json = "{}"
# create an instance of UserFavoritesAnimeInner from a JSON string
user_favorites_anime_inner_instance = UserFavoritesAnimeInner.from_json(json)
# print the JSON string representation of the object
print(UserFavoritesAnimeInner.to_json())

# convert the object into a dict
user_favorites_anime_inner_dict = user_favorites_anime_inner_instance.to_dict()
# create an instance of UserFavoritesAnimeInner from a dict
user_favorites_anime_inner_form_dict = user_favorites_anime_inner.from_dict(user_favorites_anime_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


