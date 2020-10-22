import pandas as pd

path = "./Dataset/melb_data.csv"
csv = pd.read_csv(path)
print(csv.describe())
# Suburb,    Address,      Rooms,Type,Price,   Method,SellerG,Date,    Distance,Postcode,Bedroom2,Bathroom,Car,Landsize,BuildingArea,YearBuilt,CouncilArea,Lattitude,Longtitude,Regionname,            Propertycount
# Abbotsford,98 Charles St,2     ,h,  1636000.0,S,    Nelson, 8/10/2016,2.5,    3067.0,   2.0,     1.0,    2.0, 256.0,  107.0,        1890.0,  Yarra,      -37.806,  144.9954,  Northern Metropolitan, 4019.0
