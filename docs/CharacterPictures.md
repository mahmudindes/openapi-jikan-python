# CharacterPictures

Character Pictures

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CharacterPicturesDataInner]**](CharacterPicturesDataInner.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.character_pictures import CharacterPictures

# TODO update the JSON string below
json = "{}"
# create an instance of CharacterPictures from a JSON string
character_pictures_instance = CharacterPictures.from_json(json)
# print the JSON string representation of the object
print(CharacterPictures.to_json())

# convert the object into a dict
character_pictures_dict = character_pictures_instance.to_dict()
# create an instance of CharacterPictures from a dict
character_pictures_form_dict = character_pictures.from_dict(character_pictures_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


