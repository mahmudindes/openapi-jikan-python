# MangaFull

Manga Resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mal_id** | **int** | MyAnimeList ID | [optional] 
**url** | **str** | MyAnimeList URL | [optional] 
**images** | [**MangaImages**](MangaImages.md) |  | [optional] 
**approved** | **bool** | Whether the entry is pending approval on MAL or not | [optional] 
**titles** | [**List[Title]**](Title.md) | All Titles | [optional] 
**title** | **str** | Title | [optional] 
**title_english** | **str** | English Title | [optional] 
**title_japanese** | **str** | Japanese Title | [optional] 
**title_synonyms** | **List[str]** | Other Titles | [optional] 
**type** | **str** | Manga Type | [optional] 
**chapters** | **int** | Chapter count | [optional] 
**volumes** | **int** | Volume count | [optional] 
**status** | **str** | Publishing status | [optional] 
**publishing** | **bool** | Publishing boolean | [optional] 
**published** | [**Daterange**](Daterange.md) |  | [optional] 
**score** | **float** | Score | [optional] 
**scored_by** | **int** | Number of users | [optional] 
**rank** | **int** | Ranking | [optional] 
**popularity** | **int** | Popularity | [optional] 
**members** | **int** | Number of users who have added this entry to their list | [optional] 
**favorites** | **int** | Number of users who have favorited this entry | [optional] 
**synopsis** | **str** | Synopsis | [optional] 
**background** | **str** | Background | [optional] 
**authors** | [**List[MalUrl]**](MalUrl.md) |  | [optional] 
**serializations** | [**List[MalUrl]**](MalUrl.md) |  | [optional] 
**genres** | [**List[MalUrl]**](MalUrl.md) |  | [optional] 
**explicit_genres** | [**List[MalUrl]**](MalUrl.md) |  | [optional] 
**themes** | [**List[MalUrl]**](MalUrl.md) |  | [optional] 
**demographics** | [**List[MalUrl]**](MalUrl.md) |  | [optional] 
**relations** | [**List[AnimeFullRelationsInner]**](AnimeFullRelationsInner.md) |  | [optional] 
**external** | [**List[AnimeFullExternalInner]**](AnimeFullExternalInner.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.manga_full import MangaFull

# TODO update the JSON string below
json = "{}"
# create an instance of MangaFull from a JSON string
manga_full_instance = MangaFull.from_json(json)
# print the JSON string representation of the object
print(MangaFull.to_json())

# convert the object into a dict
manga_full_dict = manga_full_instance.to_dict()
# create an instance of MangaFull from a dict
manga_full_form_dict = manga_full.from_dict(manga_full_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


