# AnimeCharacters

Anime Characters Resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AnimeCharactersDataInner]**](AnimeCharactersDataInner.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.anime_characters import AnimeCharacters

# TODO update the JSON string below
json = "{}"
# create an instance of AnimeCharacters from a JSON string
anime_characters_instance = AnimeCharacters.from_json(json)
# print the JSON string representation of the object
print(AnimeCharacters.to_json())

# convert the object into a dict
anime_characters_dict = anime_characters_instance.to_dict()
# create an instance of AnimeCharacters from a dict
anime_characters_form_dict = anime_characters.from_dict(anime_characters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


