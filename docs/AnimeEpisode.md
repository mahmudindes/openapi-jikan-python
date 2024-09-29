# AnimeEpisode

Anime Episode Resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mal_id** | **int** | MyAnimeList ID | [optional] 
**url** | **str** | MyAnimeList URL | [optional] 
**title** | **str** | Title | [optional] 
**title_japanese** | **str** | Title Japanese | [optional] 
**title_romanji** | **str** | title_romanji | [optional] 
**duration** | **int** | Episode duration in seconds | [optional] 
**aired** | **str** | Aired Date ISO8601 | [optional] 
**filler** | **bool** | Filler episode | [optional] 
**recap** | **bool** | Recap episode | [optional] 
**synopsis** | **str** | Episode Synopsis | [optional] 

## Example

```python
from jikan_openapi.models.anime_episode import AnimeEpisode

# TODO update the JSON string below
json = "{}"
# create an instance of AnimeEpisode from a JSON string
anime_episode_instance = AnimeEpisode.from_json(json)
# print the JSON string representation of the object
print(AnimeEpisode.to_json())

# convert the object into a dict
anime_episode_dict = anime_episode_instance.to_dict()
# create an instance of AnimeEpisode from a dict
anime_episode_form_dict = anime_episode.from_dict(anime_episode_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


