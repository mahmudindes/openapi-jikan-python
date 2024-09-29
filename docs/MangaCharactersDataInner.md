# MangaCharactersDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**character** | [**CharacterMeta**](CharacterMeta.md) |  | [optional] 
**role** | **str** | Character&#39;s Role | [optional] 

## Example

```python
from jikan_openapi.models.manga_characters_data_inner import MangaCharactersDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of MangaCharactersDataInner from a JSON string
manga_characters_data_inner_instance = MangaCharactersDataInner.from_json(json)
# print the JSON string representation of the object
print(MangaCharactersDataInner.to_json())

# convert the object into a dict
manga_characters_data_inner_dict = manga_characters_data_inner_instance.to_dict()
# create an instance of MangaCharactersDataInner from a dict
manga_characters_data_inner_form_dict = manga_characters_data_inner.from_dict(manga_characters_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


