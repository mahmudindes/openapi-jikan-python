# CharacterAnime

Character casted in anime

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CharacterAnimeDataInner]**](CharacterAnimeDataInner.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.character_anime import CharacterAnime

# TODO update the JSON string below
json = "{}"
# create an instance of CharacterAnime from a JSON string
character_anime_instance = CharacterAnime.from_json(json)
# print the JSON string representation of the object
print(CharacterAnime.to_json())

# convert the object into a dict
character_anime_dict = character_anime_instance.to_dict()
# create an instance of CharacterAnime from a dict
character_anime_form_dict = character_anime.from_dict(character_anime_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


