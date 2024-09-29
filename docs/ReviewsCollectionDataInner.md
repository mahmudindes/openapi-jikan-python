# ReviewsCollectionDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mal_id** | **int** | MyAnimeList ID | [optional] 
**url** | **str** | MyAnimeList review URL | [optional] 
**type** | **str** | Entry type | [optional] 
**reactions** | [**MangaReviewReactions**](MangaReviewReactions.md) |  | [optional] 
**var_date** | **str** | Review created date ISO8601 | [optional] 
**review** | **str** | Review content | [optional] 
**score** | **int** | Number of user votes on the Review | [optional] 
**tags** | **List[str]** | Review tags | [optional] 
**is_spoiler** | **bool** | The review contains spoiler | [optional] 
**is_preliminary** | **bool** | The review was made before the entry was completed | [optional] 
**episodes_watched** | **int** | Number of episodes watched | [optional] 

## Example

```python
from jikan_openapi.models.reviews_collection_data_inner import ReviewsCollectionDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewsCollectionDataInner from a JSON string
reviews_collection_data_inner_instance = ReviewsCollectionDataInner.from_json(json)
# print the JSON string representation of the object
print(ReviewsCollectionDataInner.to_json())

# convert the object into a dict
reviews_collection_data_inner_dict = reviews_collection_data_inner_instance.to_dict()
# create an instance of ReviewsCollectionDataInner from a dict
reviews_collection_data_inner_form_dict = reviews_collection_data_inner.from_dict(reviews_collection_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


