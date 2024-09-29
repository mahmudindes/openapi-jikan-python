# CharacterImages


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jpg** | [**CharacterImagesJpg**](CharacterImagesJpg.md) |  | [optional] 
**webp** | [**CharacterImagesWebp**](CharacterImagesWebp.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.character_images import CharacterImages

# TODO update the JSON string below
json = "{}"
# create an instance of CharacterImages from a JSON string
character_images_instance = CharacterImages.from_json(json)
# print the JSON string representation of the object
print(CharacterImages.to_json())

# convert the object into a dict
character_images_dict = character_images_instance.to_dict()
# create an instance of CharacterImages from a dict
character_images_form_dict = character_images.from_dict(character_images_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


