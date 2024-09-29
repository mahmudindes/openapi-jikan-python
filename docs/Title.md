# Title


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Title type | [optional] 
**title** | **str** | Title value | [optional] 

## Example

```python
from jikan_openapi.models.title import Title

# TODO update the JSON string below
json = "{}"
# create an instance of Title from a JSON string
title_instance = Title.from_json(json)
# print the JSON string representation of the object
print(Title.to_json())

# convert the object into a dict
title_dict = title_instance.to_dict()
# create an instance of Title from a dict
title_form_dict = title.from_dict(title_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


