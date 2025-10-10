# WatchPromosAllOfData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Promo Title | [optional] 
**entry** | [**AnimeMeta**](AnimeMeta.md) |  | [optional] 
**trailer** | [**Trailer**](Trailer.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.watch_promos_all_of_data import WatchPromosAllOfData

# TODO update the JSON string below
json = "{}"
# create an instance of WatchPromosAllOfData from a JSON string
watch_promos_all_of_data_instance = WatchPromosAllOfData.from_json(json)
# print the JSON string representation of the object
print(WatchPromosAllOfData.to_json())

# convert the object into a dict
watch_promos_all_of_data_dict = watch_promos_all_of_data_instance.to_dict()
# create an instance of WatchPromosAllOfData from a dict
watch_promos_all_of_data_form_dict = watch_promos_all_of_data.from_dict(watch_promos_all_of_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


