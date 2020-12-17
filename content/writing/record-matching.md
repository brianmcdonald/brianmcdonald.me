Title: Record matching in humanitarian data
Date: 2020-09-20 14:29
Modified: 2020-09-20 14:29
Category: How-to
Tags: python, information management
Authors: Brian Mc Donald
Summary: Using approaches such as 'probilistic record linkage' to join humanitarian datasets.

A reoccurring scenario in information management in humanitarian response is one where you have to compile messy data from a number of disparate sources within a very short time window. This post is an attempt to summarise some of the tools and approaches I use to tackle this problem.

## Excel: VLOOKUP, XLOOKUP and INDEXMATCH
While I wont cover them here, using [VLOOKUP][1], [INDEX MATCH][2] and the newer [XLOOKUP][3] in Excel are really useful formula when trying to combine different datasets in Excel. Learning these for the first time really feels like unlocking an analysis superpower. 

```
=XLOOKUP (lookup, lookup_array, return_array)
```

When using VLOOKUP or XLOOKUP you can shoose to use 'FALSE" at the end of the formula or 'TRUE' to find an approximate match. 'TRUE(exact match)' uses a linear search algorithm to step through the values looking for an exact match using a linear search algorithm. 'FALSE(approximate match)' is perhaps somewhat misleading, as it doesnt match the closest textual match, but rather, returns the second highest value. It uses a binary search algoritms to continually search at the mid-point value. While this may be faster, it only works on sorted numerical data and if an exact match isnt found it returns the second largest value.

## Excel fuzzy matching
This is not terribly useful. What we are looking for is something more powerful, which can help match text with slight spelling discrepencies or can search for matches acrosss multiple columns. The tool we need is called Fuzzy Matching, or more boardly speaking [Probabilistic record linkage][4]. This works by assigning a a probability score that the text in one cell matches another, based on a chosen method. Recently  Microsoft released a tool to [merge tables using fuzzy matching][5] (windows only). This allows you to set the following matching options:

1. Similarity Threshold – This option indicates how similar two values need to be in order to match. The minimum value of 0.00 will cause all values to match each other, and the maximum value of 1.00 will only allow exact matches. The default is 0.80.

2. Ignore case – This option indicates whether text values should be compared in a case sensitive or insensitive setting. The default behavior is case insensitive, which ignores casing.

3. Maximum number of matches – This option controls the maximum number of matching rows that will be returned for each input row. For example, if you only want to find one matching row for each input row, specify a value of 1. The default behavior is to return all matches.

4. Transformation table – This option allows users to specify another query that holds a mapping table, so that some values can be auto-mapped as part of the matching logic. For example, defining a two-column table with a “From” and “To” text columns with values “Microsoft” and “MSFT” will make these two values be considered the same (similarity score of 1.00) by the matching logic.

## Record matching using Python
If you want more options for your record linkages, you use macOS, or if you want more control over your workflow, Python is a good option, especially using the [fuzzymatcher][6] or [Python Record Linkage Toolkit][7] libraries.

#### fuzzymatcher examples
Here is a basic example from the fuzzymatcher docs linking two tables.

Table A 

id | ons_name
-----|---------
   0  | Darlington
   1  | Monmouthshire
   2  | Havering
   3  | Knowsley
   4  | Charnwood

and Table B

  id  | os_name
  ---|---
   0  | Darlington (B)
   1  | Havering London Boro
   2  | Sir Fynwy - Monmouthshire
   3  | Knowsley District (B)
   4  | Charnwood District (B)

Writing the following
```python
import fuzzymatcher  
fuzzymatcher.fuzzy_left_join(df_left, df_right, left_on = "ons_name", right_on = "os_name")  
```
  gives you:

  best_match_score | ons_name   |    os_name
-------------------|------------|-----
          0.178449 | Darlington |    Darlington (B)
          0.133371 | Monmouthshire | Sir Fynwy - Monmouthshire
          0.102473 | Havering   |    Havering London Boro
          0.155775 | Knowsley    |   Knowsley District (B)
          0.155775 | Charnwood    |  Charnwood District (B)







[1]: https://support.microsoft.com/en-us/office/vlookup-function-0bbc8083-26fe-4963-8ab8-93a18ad188a1
[2]: https://support.microsoft.com/en-us/office/look-up-values-with-vlookup-index-or-match-68297403-7c3c-4150-9e3c-4d348188976b
[3]: https://support.microsoft.com/en-us/office/xlookup-function-b7fd680e-6d10-43e6-84f9-88eae8bf5929
[4]: https://en.wikipedia.org/wiki/Record_linkage#Probabilistic_record_linkage
[5]: https://support.microsoft.com/en-us/office/fuzzy-match-support-for-get-transform-power-query-ffdd5082-c0c8-4c8e-a794-bd3962b90649
[6]: https://github.com/RobinL/fuzzymatcher
[7]: https://github.com/J535D165/recordlinkage

