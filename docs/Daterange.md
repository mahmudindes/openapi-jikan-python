# Daterange

Date range

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** | Date ISO8601 | [optional] 
**to** | **str** | Date ISO8601 | [optional] 
**prop** | [**DaterangeProp**](DaterangeProp.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.daterange import Daterange

# TODO update the JSON string below
json = "{}"
# create an instance of Daterange from a JSON string
daterange_instance = Daterange.from_json(json)
# print the JSON string representation of the object
print(Daterange.to_json())

# convert the object into a dict
daterange_dict = daterange_instance.to_dict()
# create an instance of Daterange from a dict
daterange_form_dict = daterange.from_dict(daterange_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


