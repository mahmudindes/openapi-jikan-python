# AnimeEpisodesAllOfData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mal_id** | **int** | MyAnimeList ID | [optional] 
**url** | **str** | MyAnimeList URL. This is the URL of the episode&#39;s video. If there is no video url, this will be null. | [optional] 
**title** | **str** | Title | [optional] 
**title_japanese** | **str** | Title Japanese | [optional] 
**title_romanji** | **str** | title_romanji | [optional] 
**duration** | **int** | Episode duration in seconds | [optional] 
**aired** | **str** | Aired Date ISO8601 | [optional] 
**filler** | **bool** | Filler episode | [optional] 
**recap** | **bool** | Recap episode | [optional] 
**forum_url** | **str** | Episode discussion forum URL | [optional] 

## Example

```python
from jikan_openapi.models.anime_episodes_all_of_data import AnimeEpisodesAllOfData

# TODO update the JSON string below
json = "{}"
# create an instance of AnimeEpisodesAllOfData from a JSON string
anime_episodes_all_of_data_instance = AnimeEpisodesAllOfData.from_json(json)
# print the JSON string representation of the object
print(AnimeEpisodesAllOfData.to_json())

# convert the object into a dict
anime_episodes_all_of_data_dict = anime_episodes_all_of_data_instance.to_dict()
# create an instance of AnimeEpisodesAllOfData from a dict
anime_episodes_all_of_data_form_dict = anime_episodes_all_of_data.from_dict(anime_episodes_all_of_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


