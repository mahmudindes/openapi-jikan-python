# PersonVoiceActingRoles

Person's voice acting roles

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PersonFullVoicesInner]**](PersonFullVoicesInner.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.person_voice_acting_roles import PersonVoiceActingRoles

# TODO update the JSON string below
json = "{}"
# create an instance of PersonVoiceActingRoles from a JSON string
person_voice_acting_roles_instance = PersonVoiceActingRoles.from_json(json)
# print the JSON string representation of the object
print(PersonVoiceActingRoles.to_json())

# convert the object into a dict
person_voice_acting_roles_dict = person_voice_acting_roles_instance.to_dict()
# create an instance of PersonVoiceActingRoles from a dict
person_voice_acting_roles_form_dict = person_voice_acting_roles.from_dict(person_voice_acting_roles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


