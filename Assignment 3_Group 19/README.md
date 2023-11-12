# Assignment 3 - OpenBIM Change
_by Frida Kragh Nielsen and Nanna Daugaard Larsen_

Our last assignment focused on the sustainability/LCA use case and the prospect of using the IFC model, to get precise material amounts and therefore being able to create more accurate carbon footprint calculations. Here we saw great potential since we were able to get a hold of volumes from building components made of concrete and calculate an accumulated amount, desired to be used for a later carbon footprint calculation. Though there is great potential, we will not further investigate this use case.  

This assignment will focus on implementing external natural elements such as trees and shrubbery, to perform daylight analysis for the building, with the inclusion of shadows from non-building elements.  

### Analysis of the use case 

The goal of the tool is the following: 

The tool inputs trees into the IFC model, with specifications such as; coordinates chosen by the user, tree type, height, diameter for crown, diameter of tree trunk, evergreen or not, light transfer through crown, and information used to determine light transferred into the building.  

The tool is meant to be used by architects in the context of daylight assessment of the building. This is to be used later in the building.  

development since the final placement of the building, windows, and trees is needed to make use of the tool. It can also be used by landscape architects, in the context of parks, plazas, and other urban spaces. The trees can in addition, also be placed on green roofs, balconies, and other surfaces, where implementation of nature is wanted when it comes to daylight.  

### Tool/workflow design 

The IFC file, where trees are wanted to be added, is first imported into Python, whereafter the coordinates of the trees are inputted one by one and checked if they are within the building site. If they are, it is possible to choose which tree is in each position, from a pre-defined list. These pre-defined trees consist of information such as tree type, height, diameter for the crown, the diameter of the tree trunk, evergreen or not, light transfer through the crown, etc. From here it is possible to either export the new IFC files, with the trees placed, and use it to determine light transmittance through windows, now with shadows from the imported trees.  

For the tool to work, the model must use correct coordinates and elevations to be able to use it for later daylight analysis. Therefore, users of the tool rely on surveyors to create accurate elevation maps, for them to accurately represent their elevations and therefore tree heights, which will affect the amount of shadow each tree casts.  

There is a slight improvement in the level of detail in our model after the implementation, though not in the already existing model, but in the uses of the model for further analysis.  

The tool can be implemented in an iterative workflow, with the purpose of daylight optimization.  

### Potential improvements offered by this tool 

This tool can create business value in the context of more precise daylight assessment, which can change the need for heating/cooling in the winter/summer season since less light will emit through the window. It can also create value in the way of earlier adaption of the biodiversity index of the final building site.  

Societal value is created since it can help improve building design and sustainability, and daylight becomes a focus of building development. Better daylight (in compliance with the Danish building regulation), improves the health and overall, well-being of the building’s occupants. By using the tool to support decisions on tree planting, green spaces, and overall city aesthetics, the tool can help city planners and municipalities create healthy and sustainable cities.  

### Limitations and Potential Improvements 

Since our limited experience with IfcOpenshell, there are some parts of the handed-in script that don’t work as intended and something that is desired to be improved if more time had been available.  

First, the way that the geometry is added is through importing the IFC file into Python, then defining the project, site, building, and story, that we need to place our geometry, as well as getting the units from the file. However, when adding the geometry, the units and size of the geometry only seem to work when, instead of defining existing project, site, building, story, and units. It has not been possible to figure out the error, and thus the created geometry, when opened in BlenderBIM, is significantly bigger than intended.  

Secondly, it was a wish that the height of the modeled tree was dependent on the tree picked to be placed. Since the geometry placement and scaling in general were off, this was not implemented.  

Third, a whished feature of the script was the option of being able to create differently polygon-shaped bases of the tree geometry, but again, since the geometry placement and scaling, in general, was off, this was not implemented.  

Finally, the way the geometry addition was made by creating an empty IFC file, with the existing project, site, building, and story, that the geometry was added to. It was originally wanted to take a more complex IFC file and add trees to this since it would be more representative of how the tool would be used in practice. However due to limitations in understanding the way IfcOpenshell places geometry not in the project origin, this was not implemented. 
