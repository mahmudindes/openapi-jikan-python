# MangaMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mal_id** | **int** | MyAnimeList ID | [optional] 
**url** | **str** | MyAnimeList URL | [optional] 
**images** | [**MangaImages**](MangaImages.md) |  | [optional] 
**title** | **str** | Entry title | [optional] 

## Example

```python
from jikan_openapi.models.manga_meta import MangaMeta

# TODO update the JSON string below
json = "{}"
# create an instance of MangaMeta from a JSON string
manga_meta_instance = MangaMeta.from_json(json)
# print the JSON string representation of the object
print(MangaMeta.to_json())

# convert the object into a dict
manga_meta_dict = manga_meta_instance.to_dict()
# create an instance of MangaMeta from a dict
manga_meta_form_dict = manga_meta.from_dict(manga_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


