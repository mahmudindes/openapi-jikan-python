# ReviewsCollection

Anime & Manga Reviews Resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ReviewsCollectionDataInner]**](ReviewsCollectionDataInner.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.reviews_collection import ReviewsCollection

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewsCollection from a JSON string
reviews_collection_instance = ReviewsCollection.from_json(json)
# print the JSON string representation of the object
print(ReviewsCollection.to_json())

# convert the object into a dict
reviews_collection_dict = reviews_collection_instance.to_dict()
# create an instance of ReviewsCollection from a dict
reviews_collection_form_dict = reviews_collection.from_dict(reviews_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


