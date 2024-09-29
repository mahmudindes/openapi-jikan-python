# CharacterMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mal_id** | **int** | MyAnimeList ID | [optional] 
**url** | **str** | MyAnimeList URL | [optional] 
**images** | [**CharacterImages**](CharacterImages.md) |  | [optional] 
**name** | **str** | Entry name | [optional] 

## Example

```python
from jikan_openapi.models.character_meta import CharacterMeta

# TODO update the JSON string below
json = "{}"
# create an instance of CharacterMeta from a JSON string
character_meta_instance = CharacterMeta.from_json(json)
# print the JSON string representation of the object
print(CharacterMeta.to_json())

# convert the object into a dict
character_meta_dict = character_meta_instance.to_dict()
# create an instance of CharacterMeta from a dict
character_meta_form_dict = character_meta.from_dict(character_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


