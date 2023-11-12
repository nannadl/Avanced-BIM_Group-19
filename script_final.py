import ifcopenshell
from ifcopenshell.api import run
import pandas as pd

# Get model
# Change path to ifc model path
ifc_file =r'C:\Users\nanna\OneDrive - Danmarks Tekniske Universitet\Skrivebord\Empty_file_final.ifc'
ifcfile = ifcopenshell.open(ifc_file)

# Getting IFC project entity
# project = run("root.create_entity", ifcfile, ifc_class="IfcProject", name="Tree Project")
project = ifcfile.by_type("IfcProject")

# Assigning without arguments defaults to metric units
# run("unit.assign_unit", ifcfile)
# global_unit_assignments = ifcfile.by_type("IfcUnitAssignment")
# global_length_unit_definition = [u for ua in global_unit_assignments for u in ua.Units if u.is_a() in ('IfcSIUnit', 'IfcConversionBasedUnit') and u.UnitType=='LENGTHUNIT'][-1]
# print(global_unit_assignments)

project = ifcfile.by_type("IfcProject")[0]
project_units = project.UnitsInContext.Units

project_length_unit_definition = [u for u in project_units if u.is_a() in ('IfcSIUnit', 'IfcConversionBasedUnit') and u.UnitType=='LENGTHUNIT'][-1]

# global_unit_assignments = ifcfile.by_type("IfcUnitAssignment")
# print(global_unit_assignments)

# creating a context for our geometry
context = run("context.add_context", ifcfile, context_type="Model")

# creating 3d 'body' context
body = run("context.add_context", ifcfile, context_type="Model",context_identifier="Body", target_view="MODEL_VIEW", parent=context)

# # Creating site, building and storey
# site = run("root.create_entity", ifcfile, ifc_class="IfcSite", name="My Site")
# building = run("root.create_entity", ifcfile, ifc_class="IfcBuilding", name="Building A")
# storey = run("root.create_entity", ifcfile, ifc_class="IfcBuildingStorey", name="Ground Floor")

site = ifcfile.by_type('IfcSite')
building = ifcfile.by_type('IfcBuilding')
storey = ifcfile.by_type('IfcBuildingStorey')


# # Since the site is our top level location, assign it to the project
# # Then place our building on the site, and our storey in the building
# run("aggregate.assign_object", ifcfile, relating_object=project, product=site)
# run("aggregate.assign_object", ifcfile, relating_object=site, product=building)
# run("aggregate.assign_object", ifcfile, relating_object=building, product=storey)

# Let's create a new wall
tree = run("root.create_entity", ifcfile, ifc_class="IfcWall")

# Give our wall a local origin at (0, 0, 0)
run("geometry.edit_object_placement", ifcfile, product=tree)

height = 6

#pyramide ting ting
vertices = [[(0,0,0), (0,2,0), (2,2,0), (2,0,0), (1,1,height)]]
faces = [[(0,1,2,3), (0,4,1), (1,4,2), (2,4,3), (3,4,0)]]
representation = run("geometry.add_mesh_representation", ifcfile, context=body, vertices=vertices, faces=faces)

# Assign our new body geometry back to our wall
run("geometry.assign_representation", ifcfile, product=tree, representation=representation)

# Place our wall in the ground floor
run("spatial.assign_container", ifcfile, relating_structure=storey[0], product=tree)

# Import your directory (Change file path)
df = pd.read_excel(r'C:\Users\nanna\OneDrive - Danmarks Tekniske Universitet\Skrivebord\41934 Videregående Bygnings Informations Modellering (BIM)\Assignment 3\TreeTypeData.xlsx')

#Choose ID for desired tree
print(df)

ID=12

# Ectracting Tree name
# Extract the cell value from a specific row and column
row_index = ID - 1  # Subtract 1 to convert ID to a 0-based index
column_name = 'Name '  # Replace with the actual column name

cell_value = df.iloc[row_index][column_name]
print(f"The cell value for ID {ID} in column '{column_name}' is {cell_value}")
print(cell_value)

# Ectracting Latin name
# Extract the cell value from a specific row and column
column_name1 = 'Latin Name'  # Replace with the actual column name

cell_value1 = df.iloc[row_index][column_name1]
print(f"The cell value for ID {ID} in column '{column_name1}' is {cell_value1}")

# Ectracting Evergreen
# Extract the cell value from a specific row and column
column_name2 = 'Evergreen'  # Replace with the actual column name

cell_value2 = df.iloc[row_index][column_name2]

# Define a dictionary to map values to strings
value_to_string = {0: "No", 1: "Yes"}

# Replace the value using the dictionary
cell_value21 = value_to_string.get(cell_value2, "Invalid Value")

print(f"The cell value for ID {ID} in column '{column_name2}' is {cell_value21}")

# Extracting Crown Radius
column_name3 = "Crown Radius"  # Replace with the actual column name

cell_value3 = df.iloc[row_index][column_name3]
print(f"The cell value for ID {ID} in column '{column_name3}' is {cell_value3}")

#Extracting the height 
# Extract the cell value from a specific row and column
column_name4 = 'Avg. Height '  # Replace with the actual column name

cell_value4 = df.iloc[row_index][column_name4]
print(f"The cell value for ID {ID} in column '{column_name4}' is {cell_value4}")

# Adding psets named "Tree properties" to tree:
pset = ifcopenshell.api.run("pset.add_pset", ifcfile, product=tree, name="Tree properties")
# Adding pset properties; Tree type, Latin name, Evergreen, Crown radius and avg. height
ifcopenshell.api.run("pset.edit_pset", ifcfile, pset=pset, properties={"Tree type": cell_value, "Latin name": cell_value1, "Evergreen": cell_value21, "Crown radius": cell_value3, "Avg. height": cell_value4})

# Saving in file
ifcfile.write(ifc_file)
