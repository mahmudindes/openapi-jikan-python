# GetPersonById200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Person**](Person.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.get_person_by_id200_response import GetPersonById200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetPersonById200Response from a JSON string
get_person_by_id200_response_instance = GetPersonById200Response.from_json(json)
# print the JSON string representation of the object
print(GetPersonById200Response.to_json())

# convert the object into a dict
get_person_by_id200_response_dict = get_person_by_id200_response_instance.to_dict()
# create an instance of GetPersonById200Response from a dict
get_person_by_id200_response_form_dict = get_person_by_id200_response.from_dict(get_person_by_id200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


