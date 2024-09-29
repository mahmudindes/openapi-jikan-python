# AnimeMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mal_id** | **int** | MyAnimeList ID | [optional] 
**url** | **str** | MyAnimeList URL | [optional] 
**images** | [**AnimeImages**](AnimeImages.md) |  | [optional] 
**title** | **str** | Entry title | [optional] 

## Example

```python
from jikan_openapi.models.anime_meta import AnimeMeta

# TODO update the JSON string below
json = "{}"
# create an instance of AnimeMeta from a JSON string
anime_meta_instance = AnimeMeta.from_json(json)
# print the JSON string representation of the object
print(AnimeMeta.to_json())

# convert the object into a dict
anime_meta_dict = anime_meta_instance.to_dict()
# create an instance of AnimeMeta from a dict
anime_meta_form_dict = anime_meta.from_dict(anime_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


