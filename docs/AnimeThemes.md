# AnimeThemes

Anime Opening and Ending Themes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AnimeFullTheme**](AnimeFullTheme.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.anime_themes import AnimeThemes

# TODO update the JSON string below
json = "{}"
# create an instance of AnimeThemes from a JSON string
anime_themes_instance = AnimeThemes.from_json(json)
# print the JSON string representation of the object
print(AnimeThemes.to_json())

# convert the object into a dict
anime_themes_dict = anime_themes_instance.to_dict()
# create an instance of AnimeThemes from a dict
anime_themes_form_dict = anime_themes.from_dict(anime_themes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


