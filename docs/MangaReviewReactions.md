# MangaReviewReactions

User reaction count on the review

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**overall** | **int** | Overall reaction count | [optional] 
**nice** | **int** | Nice reaction count | [optional] 
**love_it** | **int** | Love it reaction count | [optional] 
**funny** | **int** | Funny reaction count | [optional] 
**confusing** | **int** | Confusing reaction count | [optional] 
**informative** | **int** | Informative reaction count | [optional] 
**well_written** | **int** | Well written reaction count | [optional] 
**creative** | **int** | Creative reaction count | [optional] 

## Example

```python
from jikan_openapi.models.manga_review_reactions import MangaReviewReactions

# TODO update the JSON string below
json = "{}"
# create an instance of MangaReviewReactions from a JSON string
manga_review_reactions_instance = MangaReviewReactions.from_json(json)
# print the JSON string representation of the object
print(MangaReviewReactions.to_json())

# convert the object into a dict
manga_review_reactions_dict = manga_review_reactions_instance.to_dict()
# create an instance of MangaReviewReactions from a dict
manga_review_reactions_form_dict = manga_review_reactions.from_dict(manga_review_reactions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


