# AnimeVideosEpisodes

Anime Videos Episodes Resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationPagination**](PaginationPagination.md) |  | [optional] 
**data** | [**List[AnimeVideosEpisodesAllOfData]**](AnimeVideosEpisodesAllOfData.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.anime_videos_episodes import AnimeVideosEpisodes

# TODO update the JSON string below
json = "{}"
# create an instance of AnimeVideosEpisodes from a JSON string
anime_videos_episodes_instance = AnimeVideosEpisodes.from_json(json)
# print the JSON string representation of the object
print(AnimeVideosEpisodes.to_json())

# convert the object into a dict
anime_videos_episodes_dict = anime_videos_episodes_instance.to_dict()
# create an instance of AnimeVideosEpisodes from a dict
anime_videos_episodes_form_dict = anime_videos_episodes.from_dict(anime_videos_episodes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


