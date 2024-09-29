# RecommendationsAllOfData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mal_id** | **str** | MAL IDs of recommendations is both of the MAL ID&#39;s with a &#x60;-&#x60; delimiter | [optional] 
**entry** | [**List[RecommendationsAllOfEntry]**](RecommendationsAllOfEntry.md) | Array of 2 entries that are being recommended to each other | [optional] 
**content** | **str** | Recommendation context provided by the user | [optional] 
**user** | [**UserById**](UserById.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.recommendations_all_of_data import RecommendationsAllOfData

# TODO update the JSON string below
json = "{}"
# create an instance of RecommendationsAllOfData from a JSON string
recommendations_all_of_data_instance = RecommendationsAllOfData.from_json(json)
# print the JSON string representation of the object
print(RecommendationsAllOfData.to_json())

# convert the object into a dict
recommendations_all_of_data_dict = recommendations_all_of_data_instance.to_dict()
# create an instance of RecommendationsAllOfData from a dict
recommendations_all_of_data_form_dict = recommendations_all_of_data.from_dict(recommendations_all_of_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


