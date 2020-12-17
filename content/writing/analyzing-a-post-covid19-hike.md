Title: Analyzing a post lockdown hike 
Date: 2020-05-17 10:20
Modified: 2020-03-04 18:40
Tags: hiking, analysis, nature 
Category: General
Slug: analyzing-a-post-covid19-hike
Author: Brian Mc Donald
Summary: The end of the this COVID-19 lockdown was a chance to to go hiking in the mountains again and to examine some of the quirks of GPS.

Going without something for a long time can sharpen your sense of appreciation for it. Since France announced lockdown measures on 17th March, my experiences with the physical world outside of my apartment have been limited to trips to buy groceries and short walks around the outside of [Chateau Voltaire][1]. Yesterday, as the restriction began to ease, I was finally able to go for a short hike in [Sommand][2] in [Haute-Savoie][3].

The hike itself only took a couple of hours and was not difficult - although my lockdown conditioned muscles argue differently with me this morning. Below are a static 3D map and dynamic map of the hike along with some pictures of the views and local wildlife.

![Chamois][5]   
*A Chamois (Credit: [Wikipedia][6] Manfred Werner)*

## The route
We parked in the small parking area past La Matafan, You can see it in the map below, the section where the loop doesnt quite join up.
![Route][7]   
*3D render of the route using QGIS*

[![Vis][8]](/Map1.html)  
*Click to see the full interactive map*


You'll notice we took a long route on the way back to the car. That was to get ice-cream :)

## Elevation profiles
The trails in the above maps are from our recorded route, logged in the wonderful [OsmAnd][4] Android app. The GPS in my basic android phone supposedly uses [A-GPS][9], [GLOSNASS][10] and [BDS][11] (but interestingly not [Galileo][12]) to log coordinates, so should be reasonably accurate.

I was curious as to how the elevation readings of my phone compare to other methods, such as calculating it from position on a DEM (Digital Elevation Model) such as the SRTM.

![Elevation][13]

Comparing the two elevation sources shows some interesting results. While the tracks are quite well aligned for the section of trip where we descend on the eastern, south-eastern slope of the mountain, there is a big discrepancy in the section leading up to the highest point of our hike.

[1]: http://www.chateau-ferney-voltaire.fr/en
[2]: https://www.openstreetmap.org/search?query=sommand#map=14/46.1612/6.5524
[3]: https://en.wikipedia.org/wiki/Haute-Savoie
[4]: https://osmand.net/
[5]: files/images/chamois.jpg
[6]: https://en.wikipedia.org/wiki/Chamois
[7]: files/images/Sommand-hike.jpg
[8]: files/images/Sommand-trail.webp
[9]: https://en.wikipedia.org/wiki/Assisted_GPS
[10]: https://en.wikipedia.org/wiki/GLONASS
[11]: https://en.wikipedia.org/wiki/BeiDou
[12]: https://en.wikipedia.org/wiki/Galileo_(satellite_navigation) 
[13]: files/images/elev.webp
