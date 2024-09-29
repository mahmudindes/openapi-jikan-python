# CharacterImagesJpg

Available images in JPG

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_url** | **str** | Image URL JPG | [optional] 
**small_image_url** | **str** | Small Image URL JPG | [optional] 

## Example

```python
from jikan_openapi.models.character_images_jpg import CharacterImagesJpg

# TODO update the JSON string below
json = "{}"
# create an instance of CharacterImagesJpg from a JSON string
character_images_jpg_instance = CharacterImagesJpg.from_json(json)
# print the JSON string representation of the object
print(CharacterImagesJpg.to_json())

# convert the object into a dict
character_images_jpg_dict = character_images_jpg_instance.to_dict()
# create an instance of CharacterImagesJpg from a dict
character_images_jpg_form_dict = character_images_jpg.from_dict(character_images_jpg_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


