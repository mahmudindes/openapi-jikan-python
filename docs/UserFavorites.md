# UserFavorites


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anime** | [**List[UserFavoritesAnimeInner]**](UserFavoritesAnimeInner.md) | Favorite Anime | [optional] 
**manga** | [**List[UserFavoritesMangaInner]**](UserFavoritesMangaInner.md) | Favorite Manga | [optional] 
**characters** | [**List[UserFavoritesCharactersInner]**](UserFavoritesCharactersInner.md) | Favorite Characters | [optional] 
**people** | [**List[CharacterMeta]**](CharacterMeta.md) | Favorite People | [optional] 

## Example

```python
from jikan_openapi.models.user_favorites import UserFavorites

# TODO update the JSON string below
json = "{}"
# create an instance of UserFavorites from a JSON string
user_favorites_instance = UserFavorites.from_json(json)
# print the JSON string representation of the object
print(UserFavorites.to_json())

# convert the object into a dict
user_favorites_dict = user_favorites_instance.to_dict()
# create an instance of UserFavorites from a dict
user_favorites_form_dict = user_favorites.from_dict(user_favorites_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


