# CharacterFull

Character Resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mal_id** | **int** | MyAnimeList ID | [optional] 
**url** | **str** | MyAnimeList URL | [optional] 
**images** | [**CharacterImages**](CharacterImages.md) |  | [optional] 
**name** | **str** | Name | [optional] 
**name_kanji** | **str** | Name | [optional] 
**nicknames** | **List[str]** | Other Names | [optional] 
**favorites** | **int** | Number of users who have favorited this entry | [optional] 
**about** | **str** | Biography | [optional] 
**anime** | [**List[CharacterAnimeDataInner]**](CharacterAnimeDataInner.md) |  | [optional] 
**manga** | [**List[CharacterFullMangaInner]**](CharacterFullMangaInner.md) |  | [optional] 
**voices** | [**List[CharacterFullVoicesInner]**](CharacterFullVoicesInner.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.character_full import CharacterFull

# TODO update the JSON string below
json = "{}"
# create an instance of CharacterFull from a JSON string
character_full_instance = CharacterFull.from_json(json)
# print the JSON string representation of the object
print(CharacterFull.to_json())

# convert the object into a dict
character_full_dict = character_full_instance.to_dict()
# create an instance of CharacterFull from a dict
character_full_form_dict = character_full.from_dict(character_full_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


