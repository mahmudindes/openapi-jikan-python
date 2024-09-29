# WatchEpisodesAllOfEpisodes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mal_id** | **str** | MyAnimeList ID | [optional] 
**url** | **str** | MyAnimeList URL | [optional] 
**title** | **str** | Episode Title | [optional] 
**premium** | **bool** | For MyAnimeList Premium Users | [optional] 

## Example

```python
from jikan_openapi.models.watch_episodes_all_of_episodes import WatchEpisodesAllOfEpisodes

# TODO update the JSON string below
json = "{}"
# create an instance of WatchEpisodesAllOfEpisodes from a JSON string
watch_episodes_all_of_episodes_instance = WatchEpisodesAllOfEpisodes.from_json(json)
# print the JSON string representation of the object
print(WatchEpisodesAllOfEpisodes.to_json())

# convert the object into a dict
watch_episodes_all_of_episodes_dict = watch_episodes_all_of_episodes_instance.to_dict()
# create an instance of WatchEpisodesAllOfEpisodes from a dict
watch_episodes_all_of_episodes_form_dict = watch_episodes_all_of_episodes.from_dict(watch_episodes_all_of_episodes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


