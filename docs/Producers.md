# Producers

Producers Collection Resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationPagination**](PaginationPagination.md) |  | [optional] 
**data** | [**List[Producer]**](Producer.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.producers import Producers

# TODO update the JSON string below
json = "{}"
# create an instance of Producers from a JSON string
producers_instance = Producers.from_json(json)
# print the JSON string representation of the object
print(Producers.to_json())

# convert the object into a dict
producers_dict = producers_instance.to_dict()
# create an instance of Producers from a dict
producers_form_dict = producers.from_dict(producers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


