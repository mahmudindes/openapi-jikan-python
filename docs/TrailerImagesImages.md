# TrailerImagesImages


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_url** | **str** | Default Image Size URL (120x90) | [optional] 
**small_image_url** | **str** | Small Image Size URL (640x480) | [optional] 
**medium_image_url** | **str** | Medium Image Size URL (320x180) | [optional] 
**large_image_url** | **str** | Large Image Size URL (480x360) | [optional] 
**maximum_image_url** | **str** | Maximum Image Size URL (1280x720) | [optional] 

## Example

```python
from jikan_openapi.models.trailer_images_images import TrailerImagesImages

# TODO update the JSON string below
json = "{}"
# create an instance of TrailerImagesImages from a JSON string
trailer_images_images_instance = TrailerImagesImages.from_json(json)
# print the JSON string representation of the object
print(TrailerImagesImages.to_json())

# convert the object into a dict
trailer_images_images_dict = trailer_images_images_instance.to_dict()
# create an instance of TrailerImagesImages from a dict
trailer_images_images_form_dict = trailer_images_images.from_dict(trailer_images_images_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


