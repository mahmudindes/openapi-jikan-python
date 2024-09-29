# AnimeEpisodes

Anime Episodes Resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationPagination**](PaginationPagination.md) |  | [optional] 
**data** | [**List[AnimeEpisodesAllOfData]**](AnimeEpisodesAllOfData.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.anime_episodes import AnimeEpisodes

# TODO update the JSON string below
json = "{}"
# create an instance of AnimeEpisodes from a JSON string
anime_episodes_instance = AnimeEpisodes.from_json(json)
# print the JSON string representation of the object
print(AnimeEpisodes.to_json())

# convert the object into a dict
anime_episodes_dict = anime_episodes_instance.to_dict()
# create an instance of AnimeEpisodes from a dict
anime_episodes_form_dict = anime_episodes.from_dict(anime_episodes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


