# GetRandomUsers200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UserProfile**](UserProfile.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.get_random_users200_response import GetRandomUsers200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetRandomUsers200Response from a JSON string
get_random_users200_response_instance = GetRandomUsers200Response.from_json(json)
# print the JSON string representation of the object
print(GetRandomUsers200Response.to_json())

# convert the object into a dict
get_random_users200_response_dict = get_random_users200_response_instance.to_dict()
# create an instance of GetRandomUsers200Response from a dict
get_random_users200_response_form_dict = get_random_users200_response.from_dict(get_random_users200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


