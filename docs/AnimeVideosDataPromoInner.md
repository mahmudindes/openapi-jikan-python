# AnimeVideosDataPromoInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Title | [optional] 
**trailer** | [**Trailer**](Trailer.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.anime_videos_data_promo_inner import AnimeVideosDataPromoInner

# TODO update the JSON string below
json = "{}"
# create an instance of AnimeVideosDataPromoInner from a JSON string
anime_videos_data_promo_inner_instance = AnimeVideosDataPromoInner.from_json(json)
# print the JSON string representation of the object
print(AnimeVideosDataPromoInner.to_json())

# convert the object into a dict
anime_videos_data_promo_inner_dict = anime_videos_data_promo_inner_instance.to_dict()
# create an instance of AnimeVideosDataPromoInner from a dict
anime_videos_data_promo_inner_form_dict = anime_videos_data_promo_inner.from_dict(anime_videos_data_promo_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


