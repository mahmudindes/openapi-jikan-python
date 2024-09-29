# AnimeVideosEpisodesAllOfData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mal_id** | **int** | MyAnimeList ID or Episode Number | [optional] 
**title** | **str** | Episode Title | [optional] 
**episode** | **str** | Episode Subtitle | [optional] 
**url** | **str** | Episode Page URL | [optional] 
**images** | [**CommonImages**](CommonImages.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.anime_videos_episodes_all_of_data import AnimeVideosEpisodesAllOfData

# TODO update the JSON string below
json = "{}"
# create an instance of AnimeVideosEpisodesAllOfData from a JSON string
anime_videos_episodes_all_of_data_instance = AnimeVideosEpisodesAllOfData.from_json(json)
# print the JSON string representation of the object
print(AnimeVideosEpisodesAllOfData.to_json())

# convert the object into a dict
anime_videos_episodes_all_of_data_dict = anime_videos_episodes_all_of_data_instance.to_dict()
# create an instance of AnimeVideosEpisodesAllOfData from a dict
anime_videos_episodes_all_of_data_form_dict = anime_videos_episodes_all_of_data.from_dict(anime_videos_episodes_all_of_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


