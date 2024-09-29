# MangaStatistics

Manga Statistics Resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**MangaStatisticsData**](MangaStatisticsData.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.manga_statistics import MangaStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of MangaStatistics from a JSON string
manga_statistics_instance = MangaStatistics.from_json(json)
# print the JSON string representation of the object
print(MangaStatistics.to_json())

# convert the object into a dict
manga_statistics_dict = manga_statistics_instance.to_dict()
# create an instance of MangaStatistics from a dict
manga_statistics_form_dict = manga_statistics.from_dict(manga_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


