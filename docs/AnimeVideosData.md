# AnimeVideosData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**promo** | [**List[AnimeVideosDataPromoInner]**](AnimeVideosDataPromoInner.md) |  | [optional] 
**episodes** | [**List[AnimeVideosDataEpisodesInner]**](AnimeVideosDataEpisodesInner.md) |  | [optional] 
**music_videos** | [**List[AnimeVideosDataMusicVideosInner]**](AnimeVideosDataMusicVideosInner.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.anime_videos_data import AnimeVideosData

# TODO update the JSON string below
json = "{}"
# create an instance of AnimeVideosData from a JSON string
anime_videos_data_instance = AnimeVideosData.from_json(json)
# print the JSON string representation of the object
print(AnimeVideosData.to_json())

# convert the object into a dict
anime_videos_data_dict = anime_videos_data_instance.to_dict()
# create an instance of AnimeVideosData from a dict
anime_videos_data_form_dict = anime_videos_data.from_dict(anime_videos_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


