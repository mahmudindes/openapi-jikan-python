# CharacterFullVoicesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | **str** | Character&#39;s Role | [optional] 
**person** | [**PersonMeta**](PersonMeta.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.character_full_voices_inner import CharacterFullVoicesInner

# TODO update the JSON string below
json = "{}"
# create an instance of CharacterFullVoicesInner from a JSON string
character_full_voices_inner_instance = CharacterFullVoicesInner.from_json(json)
# print the JSON string representation of the object
print(CharacterFullVoicesInner.to_json())

# convert the object into a dict
character_full_voices_inner_dict = character_full_voices_inner_instance.to_dict()
# create an instance of CharacterFullVoicesInner from a dict
character_full_voices_inner_form_dict = character_full_voices_inner.from_dict(character_full_voices_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


