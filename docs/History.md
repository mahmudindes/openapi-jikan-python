# History

Transform the resource into an array.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry** | [**MalUrl**](MalUrl.md) |  | [optional] 
**increment** | **int** | Number of episodes/chapters watched/read | [optional] 
**var_date** | **str** | Date ISO8601 | [optional] 

## Example

```python
from jikan_openapi.models.history import History

# TODO update the JSON string below
json = "{}"
# create an instance of History from a JSON string
history_instance = History.from_json(json)
# print the JSON string representation of the object
print(History.to_json())

# convert the object into a dict
history_dict = history_instance.to_dict()
# create an instance of History from a dict
history_form_dict = history.from_dict(history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


