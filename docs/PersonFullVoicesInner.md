# PersonFullVoicesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** | Person&#39;s Character&#39;s role in the anime | [optional] 
**anime** | [**AnimeMeta**](AnimeMeta.md) |  | [optional] 
**character** | [**CharacterMeta**](CharacterMeta.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.person_full_voices_inner import PersonFullVoicesInner

# TODO update the JSON string below
json = "{}"
# create an instance of PersonFullVoicesInner from a JSON string
person_full_voices_inner_instance = PersonFullVoicesInner.from_json(json)
# print the JSON string representation of the object
print(PersonFullVoicesInner.to_json())

# convert the object into a dict
person_full_voices_inner_dict = person_full_voices_inner_instance.to_dict()
# create an instance of PersonFullVoicesInner from a dict
person_full_voices_inner_form_dict = person_full_voices_inner.from_dict(person_full_voices_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


