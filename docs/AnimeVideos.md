# AnimeVideos

Anime Videos Resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AnimeVideosData**](AnimeVideosData.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.anime_videos import AnimeVideos

# TODO update the JSON string below
json = "{}"
# create an instance of AnimeVideos from a JSON string
anime_videos_instance = AnimeVideos.from_json(json)
# print the JSON string representation of the object
print(AnimeVideos.to_json())

# convert the object into a dict
anime_videos_dict = anime_videos_instance.to_dict()
# create an instance of AnimeVideos from a dict
anime_videos_form_dict = anime_videos.from_dict(anime_videos_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


