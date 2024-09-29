# AnimeImagesWebp

Available images in WEBP

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_url** | **str** | Image URL WEBP | [optional] 
**small_image_url** | **str** | Small Image URL WEBP | [optional] 
**large_image_url** | **str** | Image URL WEBP | [optional] 

## Example

```python
from jikan_openapi.models.anime_images_webp import AnimeImagesWebp

# TODO update the JSON string below
json = "{}"
# create an instance of AnimeImagesWebp from a JSON string
anime_images_webp_instance = AnimeImagesWebp.from_json(json)
# print the JSON string representation of the object
print(AnimeImagesWebp.to_json())

# convert the object into a dict
anime_images_webp_dict = anime_images_webp_instance.to_dict()
# create an instance of AnimeImagesWebp from a dict
anime_images_webp_form_dict = anime_images_webp.from_dict(anime_images_webp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


