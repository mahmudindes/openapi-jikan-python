# AnimeCharactersDataInnerVoiceActorsInnerPerson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mal_id** | **int** |  | [optional] 
**url** | **str** |  | [optional] 
**images** | [**PeopleImages**](PeopleImages.md) |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from jikan_openapi.models.anime_characters_data_inner_voice_actors_inner_person import AnimeCharactersDataInnerVoiceActorsInnerPerson

# TODO update the JSON string below
json = "{}"
# create an instance of AnimeCharactersDataInnerVoiceActorsInnerPerson from a JSON string
anime_characters_data_inner_voice_actors_inner_person_instance = AnimeCharactersDataInnerVoiceActorsInnerPerson.from_json(json)
# print the JSON string representation of the object
print(AnimeCharactersDataInnerVoiceActorsInnerPerson.to_json())

# convert the object into a dict
anime_characters_data_inner_voice_actors_inner_person_dict = anime_characters_data_inner_voice_actors_inner_person_instance.to_dict()
# create an instance of AnimeCharactersDataInnerVoiceActorsInnerPerson from a dict
anime_characters_data_inner_voice_actors_inner_person_form_dict = anime_characters_data_inner_voice_actors_inner_person.from_dict(anime_characters_data_inner_voice_actors_inner_person_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


