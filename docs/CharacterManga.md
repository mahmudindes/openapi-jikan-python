# CharacterManga

Character casted in manga

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CharacterFullMangaInner]**](CharacterFullMangaInner.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.character_manga import CharacterManga

# TODO update the JSON string below
json = "{}"
# create an instance of CharacterManga from a JSON string
character_manga_instance = CharacterManga.from_json(json)
# print the JSON string representation of the object
print(CharacterManga.to_json())

# convert the object into a dict
character_manga_dict = character_manga_instance.to_dict()
# create an instance of CharacterManga from a dict
character_manga_form_dict = character_manga.from_dict(character_manga_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


