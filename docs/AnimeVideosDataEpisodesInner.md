# AnimeVideosDataEpisodesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mal_id** | **int** | MyAnimeList ID | [optional] 
**url** | **str** | MyAnimeList URL | [optional] 
**title** | **str** | Title | [optional] 
**episode** | **str** | Episode | [optional] 
**images** | [**CommonImages**](CommonImages.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.anime_videos_data_episodes_inner import AnimeVideosDataEpisodesInner

# TODO update the JSON string below
json = "{}"
# create an instance of AnimeVideosDataEpisodesInner from a JSON string
anime_videos_data_episodes_inner_instance = AnimeVideosDataEpisodesInner.from_json(json)
# print the JSON string representation of the object
print(AnimeVideosDataEpisodesInner.to_json())

# convert the object into a dict
anime_videos_data_episodes_inner_dict = anime_videos_data_episodes_inner_instance.to_dict()
# create an instance of AnimeVideosDataEpisodesInner from a dict
anime_videos_data_episodes_inner_form_dict = anime_videos_data_episodes_inner.from_dict(anime_videos_data_episodes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


