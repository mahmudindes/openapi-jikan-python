# AnimeVideosDataMusicVideosInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Title | [optional] 
**video** | [**Trailer**](Trailer.md) |  | [optional] 
**meta** | [**AnimeVideosDataMusicVideosInnerMeta**](AnimeVideosDataMusicVideosInnerMeta.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.anime_videos_data_music_videos_inner import AnimeVideosDataMusicVideosInner

# TODO update the JSON string below
json = "{}"
# create an instance of AnimeVideosDataMusicVideosInner from a JSON string
anime_videos_data_music_videos_inner_instance = AnimeVideosDataMusicVideosInner.from_json(json)
# print the JSON string representation of the object
print(AnimeVideosDataMusicVideosInner.to_json())

# convert the object into a dict
anime_videos_data_music_videos_inner_dict = anime_videos_data_music_videos_inner_instance.to_dict()
# create an instance of AnimeVideosDataMusicVideosInner from a dict
anime_videos_data_music_videos_inner_form_dict = anime_videos_data_music_videos_inner.from_dict(anime_videos_data_music_videos_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


