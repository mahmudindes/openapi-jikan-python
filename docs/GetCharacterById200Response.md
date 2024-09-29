# GetCharacterById200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Character**](Character.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.get_character_by_id200_response import GetCharacterById200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetCharacterById200Response from a JSON string
get_character_by_id200_response_instance = GetCharacterById200Response.from_json(json)
# print the JSON string representation of the object
print(GetCharacterById200Response.to_json())

# convert the object into a dict
get_character_by_id200_response_dict = get_character_by_id200_response_instance.to_dict()
# create an instance of GetCharacterById200Response from a dict
get_character_by_id200_response_form_dict = get_character_by_id200_response.from_dict(get_character_by_id200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


