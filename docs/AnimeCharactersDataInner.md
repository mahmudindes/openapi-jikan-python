# AnimeCharactersDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**character** | [**AnimeCharactersDataInnerCharacter**](AnimeCharactersDataInnerCharacter.md) |  | [optional] 
**role** | **str** | Character&#39;s Role | [optional] 
**voice_actors** | [**List[AnimeCharactersDataInnerVoiceActorsInner]**](AnimeCharactersDataInnerVoiceActorsInner.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.anime_characters_data_inner import AnimeCharactersDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of AnimeCharactersDataInner from a JSON string
anime_characters_data_inner_instance = AnimeCharactersDataInner.from_json(json)
# print the JSON string representation of the object
print(AnimeCharactersDataInner.to_json())

# convert the object into a dict
anime_characters_data_inner_dict = anime_characters_data_inner_instance.to_dict()
# create an instance of AnimeCharactersDataInner from a dict
anime_characters_data_inner_form_dict = anime_characters_data_inner.from_dict(anime_characters_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


