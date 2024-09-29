# DaterangeProp

Date Prop

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | [**DaterangePropFrom**](DaterangePropFrom.md) |  | [optional] 
**to** | [**DaterangePropTo**](DaterangePropTo.md) |  | [optional] 
**string** | **str** | Raw parsed string | [optional] 

## Example

```python
from jikan_openapi.models.daterange_prop import DaterangeProp

# TODO update the JSON string below
json = "{}"
# create an instance of DaterangeProp from a JSON string
daterange_prop_instance = DaterangeProp.from_json(json)
# print the JSON string representation of the object
print(DaterangeProp.to_json())

# convert the object into a dict
daterange_prop_dict = daterange_prop_instance.to_dict()
# create an instance of DaterangeProp from a dict
daterange_prop_form_dict = daterange_prop.from_dict(daterange_prop_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


