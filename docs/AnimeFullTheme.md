# AnimeFullTheme


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**openings** | **List[str]** |  | [optional] 
**endings** | **List[str]** |  | [optional] 

## Example

```python
from jikan_openapi.models.anime_full_theme import AnimeFullTheme

# TODO update the JSON string below
json = "{}"
# create an instance of AnimeFullTheme from a JSON string
anime_full_theme_instance = AnimeFullTheme.from_json(json)
# print the JSON string representation of the object
print(AnimeFullTheme.to_json())

# convert the object into a dict
anime_full_theme_dict = anime_full_theme_instance.to_dict()
# create an instance of AnimeFullTheme from a dict
anime_full_theme_form_dict = anime_full_theme.from_dict(anime_full_theme_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


