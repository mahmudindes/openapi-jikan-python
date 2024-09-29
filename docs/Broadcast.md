# Broadcast

Broadcast Details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day** | **str** | Day of the week | [optional] 
**time** | **str** | Time in 24 hour format | [optional] 
**timezone** | **str** | Timezone (Tz Database format https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) | [optional] 
**string** | **str** | Raw parsed broadcast string | [optional] 

## Example

```python
from jikan_openapi.models.broadcast import Broadcast

# TODO update the JSON string below
json = "{}"
# create an instance of Broadcast from a JSON string
broadcast_instance = Broadcast.from_json(json)
# print the JSON string representation of the object
print(Broadcast.to_json())

# convert the object into a dict
broadcast_dict = broadcast_instance.to_dict()
# create an instance of Broadcast from a dict
broadcast_form_dict = broadcast.from_dict(broadcast_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


