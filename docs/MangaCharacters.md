# MangaCharacters

Manga Characters Resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[MangaCharactersDataInner]**](MangaCharactersDataInner.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.manga_characters import MangaCharacters

# TODO update the JSON string below
json = "{}"
# create an instance of MangaCharacters from a JSON string
manga_characters_instance = MangaCharacters.from_json(json)
# print the JSON string representation of the object
print(MangaCharacters.to_json())

# convert the object into a dict
manga_characters_dict = manga_characters_instance.to_dict()
# create an instance of MangaCharacters from a dict
manga_characters_form_dict = manga_characters.from_dict(manga_characters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


