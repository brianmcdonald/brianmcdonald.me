Title: Towards a Unified Data Layer
Date: 2022-10-27 19:40
Modified: 2022-10-27 19:40
Tags: geospatial, deckgl, h3, quadkeys, analysis 
Category: General
Slug: unified-data-layers 
Author: Brian Mc Donald
Status: published
Summary: Common Operating Datasets in humanitarian analysis are amazing.... so lets replace them

![painting](../files/images/501450ldsdl.jpg)
*A Capriccio of Roman Ruins (1727-1729) by Marco Ricci*

*The opinions below, as always, are mine alone, and do not represent any of my employers, past or present.*

## Common Operating Datasets
The work done on Common Operating Datasets (CODs) has been one of the most important advances in information management in humanitarian response in the past 20 years.

Common Operating Datasets are typically country level administrative boundaries and population statistics. They are the basic building blocks of a response. In an a regency, where hundreds of organizations and government departments they provide a common point of reference for geographical areas within a country on the populations in those areas. In countries where there is a UNOCHA presence, they usually take the lead in the publishing of that country's CODs, in coordination with the relevant government statistics office and relevant partners, revising and updating as-mneeded. CODs are probably the most successful example example of coordination of information management. [footnote link to Andrew Verity recent publication]

but... the purpose of this post is not just to praise the work on CODs, it's to discuss emerging alternatives that overcomes many of the their shortcomings and could supplant them as the main building blocks of humanitarian response.

### The shortcomings of CODs

1. The CODs are not always available at a level of granularity sufficient for detailed analysis. While admin 0 (national-level), admin 1 (typically provincial-level or similar), and admin 2 (typically district-level or similar) can be expected to present in any response with a UNOCHA presence, there can be less of an assumption of availability for the more granular levels of admin 3, 4 or lower. This presents a challenge as analysis may then be presenting analysis at a coarser level of aggregation that may not effectively capture or show differences in needs, gaps or response that a more granular administrative and population would support.

2. Admin boundaries are often disputed. While many national boundaries are disputed, to varying degrees [ footnote of how many, from wikipedia] this generally isn't a huge issue in most humanitarian responses. in comparison to the challenge of different perspectives on sub-national boundaries within countries. This can lead to a situation where, depending of engagement at the national level, or with subnational authorities, different datasets may be needed, top relflect of the differing perspectives of what area or people that are being referred to. For compiling data this means the added complexity of needing to know the context of the data received, to understand the perspectives of the data and the asumptions behind it.

3. High variation in the area and population that a COD unit is referring to. As mentioned above, the number of admin levels in a country can vary, what varies even greater, is the geographic area that COD units represent across countries. An analysis that may be sufficentlty granular in one country, may need to be at admin 3 or 4 in another to provide a similar analysis. While a typical analysis product may have a geographical area that may be optimal for the type of analysis, quite often this has to first match the closest available admin boundaries and population, assuming all required data is also available for this. 

Within a single country this variation in admin unit size can lead to misinterpretation of data when visualizing data. A common example of this is with the use of chloropleth maps. Considering two aspect of visual perception - color and size, chloropleth's often mislead, showing comparatively larger admin areas more prominently,even though their value (colour) may be the same or less. This mis-use of choropleth graphics probably deserves an article by itself. [footnote showing the km2 area of the largest admin 3 and smallest admin2 from the CODs]

4. CODs are not just created once and are finalized, they are living datasets that often need updating to reflect administrative changes and population changes in a country. These administrative changes can mean that data from previous years may no longer be compatible to that which was gathered in different years [footnote Pakistan example of admin 1 changes] Currently the CODs dont have a process for version control, meaning that the changes of each iteration may not be known, meaning that datasets associated with previous COD versions may no longer be compatible, or may require significant data transformations or may contain a number of hiddden assumptions.
  
5. Demographics and administrative boundaries are intertwined with politics. Administrative boundaries are, as the name suggests reflect the administrative structure of a country. They are a cartographies manifestation much of our countries historic dynamics,current political dynamics especially in conflict situations can themselves be drivers, or at least contentious within the context. The close link of the geopgraphic and the political in-turn influences any analysis that use them. Even in non, or low-conflict contexts, this can still mean challenges, such as delays in publishing or updating datasets due to bureaucracy or otherwise. [ footnote Idai example]  

## Introducing H3 and Bing quadkeys
![quadkeys](../files/images/quadkeys.jpg)
- seperate political & administrative and geographic concerns and base our geographic units of analysis on something not vulnerable to the above limitations.

There are many ways other than CODs that can be used to seperate and represent different geographic units, it's far from a new concept [footnote mandala ] but in the past few years, with the growth in web-based mapping, large scale analytics and the explosion of geo-associated data, some interesting approaches have emegerged that map be of interest to humanitarians.

**Quadkeys** are ......

**H3** were 
   
- how they address the 5 problems.

## Unified data layer
- use when dealing with larger data.

- comparing to choropleth visual misleading

- example use in Pakistan - climate indicators, distributions, camps, old boundaries

- limitations - cells may not have desired homogeneity that other area classifications have and may not align with administrative structures or topography. 

- conclusion

- footnote explaining that the claims of the demise of CODs are premature, but they will likely live alongside each other. Hyperpole, but, need to be able to better run analysis across time and space. Climate research is approaching this by using the concept of a data cube, where phenomena can be easily analyzed on multiple dimensions, over geography and time.

- 
