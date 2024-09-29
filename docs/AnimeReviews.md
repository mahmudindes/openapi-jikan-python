# AnimeReviews

Anime Reviews Resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationPagination**](PaginationPagination.md) |  | [optional] 
**data** | [**List[AnimeReviewsAllOfData]**](AnimeReviewsAllOfData.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.anime_reviews import AnimeReviews

# TODO update the JSON string below
json = "{}"
# create an instance of AnimeReviews from a JSON string
anime_reviews_instance = AnimeReviews.from_json(json)
# print the JSON string representation of the object
print(AnimeReviews.to_json())

# convert the object into a dict
anime_reviews_dict = anime_reviews_instance.to_dict()
# create an instance of AnimeReviews from a dict
anime_reviews_form_dict = anime_reviews.from_dict(anime_reviews_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


