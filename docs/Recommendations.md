# Recommendations

Recommendations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationPagination**](PaginationPagination.md) |  | [optional] 
**data** | [**List[RecommendationsAllOfData]**](RecommendationsAllOfData.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.recommendations import Recommendations

# TODO update the JSON string below
json = "{}"
# create an instance of Recommendations from a JSON string
recommendations_instance = Recommendations.from_json(json)
# print the JSON string representation of the object
print(Recommendations.to_json())

# convert the object into a dict
recommendations_dict = recommendations_instance.to_dict()
# create an instance of Recommendations from a dict
recommendations_form_dict = recommendations.from_dict(recommendations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


