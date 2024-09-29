# GetProducerById200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Producer**](Producer.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.get_producer_by_id200_response import GetProducerById200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetProducerById200Response from a JSON string
get_producer_by_id200_response_instance = GetProducerById200Response.from_json(json)
# print the JSON string representation of the object
print(GetProducerById200Response.to_json())

# convert the object into a dict
get_producer_by_id200_response_dict = get_producer_by_id200_response_instance.to_dict()
# create an instance of GetProducerById200Response from a dict
get_producer_by_id200_response_form_dict = get_producer_by_id200_response.from_dict(get_producer_by_id200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


