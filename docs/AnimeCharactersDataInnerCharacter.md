# AnimeCharactersDataInnerCharacter

Character details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mal_id** | **int** | MyAnimeList ID | [optional] 
**url** | **str** | MyAnimeList URL | [optional] 
**images** | [**CharacterImages**](CharacterImages.md) |  | [optional] 
**name** | **str** | Character Name | [optional] 

## Example

```python
from jikan_openapi.models.anime_characters_data_inner_character import AnimeCharactersDataInnerCharacter

# TODO update the JSON string below
json = "{}"
# create an instance of AnimeCharactersDataInnerCharacter from a JSON string
anime_characters_data_inner_character_instance = AnimeCharactersDataInnerCharacter.from_json(json)
# print the JSON string representation of the object
print(AnimeCharactersDataInnerCharacter.to_json())

# convert the object into a dict
anime_characters_data_inner_character_dict = anime_characters_data_inner_character_instance.to_dict()
# create an instance of AnimeCharactersDataInnerCharacter from a dict
anime_characters_data_inner_character_form_dict = anime_characters_data_inner_character.from_dict(anime_characters_data_inner_character_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


