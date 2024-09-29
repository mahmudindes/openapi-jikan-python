# CharacterImagesWebp

Available images in WEBP

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_url** | **str** | Image URL WEBP | [optional] 
**small_image_url** | **str** | Small Image URL WEBP | [optional] 

## Example

```python
from jikan_openapi.models.character_images_webp import CharacterImagesWebp

# TODO update the JSON string below
json = "{}"
# create an instance of CharacterImagesWebp from a JSON string
character_images_webp_instance = CharacterImagesWebp.from_json(json)
# print the JSON string representation of the object
print(CharacterImagesWebp.to_json())

# convert the object into a dict
character_images_webp_dict = character_images_webp_instance.to_dict()
# create an instance of CharacterImagesWebp from a dict
character_images_webp_form_dict = character_images_webp.from_dict(character_images_webp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


