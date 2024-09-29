# CharacterVoiceActors

Character voice actors

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CharacterFullVoicesInner]**](CharacterFullVoicesInner.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.character_voice_actors import CharacterVoiceActors

# TODO update the JSON string below
json = "{}"
# create an instance of CharacterVoiceActors from a JSON string
character_voice_actors_instance = CharacterVoiceActors.from_json(json)
# print the JSON string representation of the object
print(CharacterVoiceActors.to_json())

# convert the object into a dict
character_voice_actors_dict = character_voice_actors_instance.to_dict()
# create an instance of CharacterVoiceActors from a dict
character_voice_actors_form_dict = character_voice_actors.from_dict(character_voice_actors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


