# CharacterAnimeDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** | Character&#39;s Role | [optional] 
**anime** | [**AnimeMeta**](AnimeMeta.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.character_anime_data_inner import CharacterAnimeDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of CharacterAnimeDataInner from a JSON string
character_anime_data_inner_instance = CharacterAnimeDataInner.from_json(json)
# print the JSON string representation of the object
print(CharacterAnimeDataInner.to_json())

# convert the object into a dict
character_anime_data_inner_dict = character_anime_data_inner_instance.to_dict()
# create an instance of CharacterAnimeDataInner from a dict
character_anime_data_inner_form_dict = character_anime_data_inner.from_dict(character_anime_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


