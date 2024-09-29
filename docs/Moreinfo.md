# Moreinfo

More Info Resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**MoreinfoData**](MoreinfoData.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.moreinfo import Moreinfo

# TODO update the JSON string below
json = "{}"
# create an instance of Moreinfo from a JSON string
moreinfo_instance = Moreinfo.from_json(json)
# print the JSON string representation of the object
print(Moreinfo.to_json())

# convert the object into a dict
moreinfo_dict = moreinfo_instance.to_dict()
# create an instance of Moreinfo from a dict
moreinfo_form_dict = moreinfo.from_dict(moreinfo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


