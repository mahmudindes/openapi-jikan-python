# MangaReviews

Manga Reviews Resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationPagination**](PaginationPagination.md) |  | [optional] 
**data** | [**List[MangaReviewsAllOfData]**](MangaReviewsAllOfData.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.manga_reviews import MangaReviews

# TODO update the JSON string below
json = "{}"
# create an instance of MangaReviews from a JSON string
manga_reviews_instance = MangaReviews.from_json(json)
# print the JSON string representation of the object
print(MangaReviews.to_json())

# convert the object into a dict
manga_reviews_dict = manga_reviews_instance.to_dict()
# create an instance of MangaReviews from a dict
manga_reviews_form_dict = manga_reviews.from_dict(manga_reviews_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


