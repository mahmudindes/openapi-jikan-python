# MoreinfoData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**moreinfo** | **str** | Additional information on the entry | [optional] 

## Example

```python
from jikan_openapi.models.moreinfo_data import MoreinfoData

# TODO update the JSON string below
json = "{}"
# create an instance of MoreinfoData from a JSON string
moreinfo_data_instance = MoreinfoData.from_json(json)
# print the JSON string representation of the object
print(MoreinfoData.to_json())

# convert the object into a dict
moreinfo_data_dict = moreinfo_data_instance.to_dict()
# create an instance of MoreinfoData from a dict
moreinfo_data_form_dict = moreinfo_data.from_dict(moreinfo_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


