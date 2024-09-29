# Schedules

Anime resources currently airing

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationPlusPagination**](PaginationPlusPagination.md) |  | [optional] 
**data** | [**List[Anime]**](Anime.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.schedules import Schedules

# TODO update the JSON string below
json = "{}"
# create an instance of Schedules from a JSON string
schedules_instance = Schedules.from_json(json)
# print the JSON string representation of the object
print(Schedules.to_json())

# convert the object into a dict
schedules_dict = schedules_instance.to_dict()
# create an instance of Schedules from a dict
schedules_form_dict = schedules.from_dict(schedules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


