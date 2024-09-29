# AnimeImagesJpg

Available images in JPG

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_url** | **str** | Image URL JPG | [optional] 
**small_image_url** | **str** | Small Image URL JPG | [optional] 
**large_image_url** | **str** | Image URL JPG | [optional] 

## Example

```python
from jikan_openapi.models.anime_images_jpg import AnimeImagesJpg

# TODO update the JSON string below
json = "{}"
# create an instance of AnimeImagesJpg from a JSON string
anime_images_jpg_instance = AnimeImagesJpg.from_json(json)
# print the JSON string representation of the object
print(AnimeImagesJpg.to_json())

# convert the object into a dict
anime_images_jpg_dict = anime_images_jpg_instance.to_dict()
# create an instance of AnimeImagesJpg from a dict
anime_images_jpg_form_dict = anime_images_jpg.from_dict(anime_images_jpg_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


