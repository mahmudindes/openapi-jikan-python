# WatchPromos

Watch Promos

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationPagination**](PaginationPagination.md) |  | [optional] 
**title** | **str** | Promo Title | [optional] 
**data** | **List[object]** |  | [optional] 

## Example

```python
from jikan_openapi.models.watch_promos import WatchPromos

# TODO update the JSON string below
json = "{}"
# create an instance of WatchPromos from a JSON string
watch_promos_instance = WatchPromos.from_json(json)
# print the JSON string representation of the object
print(WatchPromos.to_json())

# convert the object into a dict
watch_promos_dict = watch_promos_instance.to_dict()
# create an instance of WatchPromos from a dict
watch_promos_form_dict = watch_promos.from_dict(watch_promos_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


