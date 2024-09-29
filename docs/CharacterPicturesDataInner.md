# CharacterPicturesDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_url** | **str** | Default JPG Image Size URL | [optional] 
**large_image_url** | **str** | Large JPG Image Size URL | [optional] 

## Example

```python
from jikan_openapi.models.character_pictures_data_inner import CharacterPicturesDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of CharacterPicturesDataInner from a JSON string
character_pictures_data_inner_instance = CharacterPicturesDataInner.from_json(json)
# print the JSON string representation of the object
print(CharacterPicturesDataInner.to_json())

# convert the object into a dict
character_pictures_data_inner_dict = character_pictures_data_inner_instance.to_dict()
# create an instance of CharacterPicturesDataInner from a dict
character_pictures_data_inner_form_dict = character_pictures_data_inner.from_dict(character_pictures_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


