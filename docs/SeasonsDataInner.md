# SeasonsDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **int** | Year | [optional] 
**seasons** | **List[str]** | List of available seasons | [optional] 

## Example

```python
from jikan_openapi.models.seasons_data_inner import SeasonsDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of SeasonsDataInner from a JSON string
seasons_data_inner_instance = SeasonsDataInner.from_json(json)
# print the JSON string representation of the object
print(SeasonsDataInner.to_json())

# convert the object into a dict
seasons_data_inner_dict = seasons_data_inner_instance.to_dict()
# create an instance of SeasonsDataInner from a dict
seasons_data_inner_form_dict = seasons_data_inner.from_dict(seasons_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


