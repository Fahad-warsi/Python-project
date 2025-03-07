import streamlit as st
import pandas as pd

st.title("🌟WELCOME TO UNIT-CONVERTER🌟")

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["📏 LENGTH", "🌡️ TEMPERATURE", "📐 AREA", "⚖️ MASS", "🧪 VOLUME", "⏰ TIME"])
with tab1:
    st.write(f"📏 Convert different length units below:")
    from_unit = st.selectbox("From unit:",("Centimeter", "Meter", "Kilometer", "Inch", "Foot", "Yard", "Millimeter", "Micrometer", "Nanometer", "Mile", "Nautical-mile"))
    user_input = st.number_input("Enter an value:", min_value = 0.0, format = "%.6f")
    to_unit = st.selectbox("To unit:",("Centimeter", "Meter", "Kilometer", "Inch", "Foot", "Yard", "Millimeter", "Micrometer", "Nanometer", "Mile", "Nautical-mile"))
    
        
        # Conversion logic
    length_conversion_factors = {
    "Centimeter": {"Centimeter": 1,"Meter": 0.01, "Kilometer": 0.00001, "Inch": 0.3937, "Foot": 0.0328, "Yard": 0.0109, "Millimeter": 10, "Micrometer": 10000, "Nanometer": 10000000, "Mile": 0.0000062137, "Nautical-mile": 0.0000053996},
    "Meter": {"Meter":1,"Centimeter": 100, "Kilometer": 0.001, "Inch": 39.3701, "Foot": 3.28084, "Yard": 1.09361, "Millimeter": 1000, "Micrometer": 1000000, "Nanometer": 1000000000, "Mile": 0.000621371, "Nautical-mile": 0.000539957},
    "Kilometer": {"Kilometer":1,"Centimeter": 100000, "Meter": 1000, "Inch": 39370.1, "Foot": 3280.84, "Yard": 1093.61, "Millimeter": 1000000, "Micrometer": 1000000000, "Nanometer": 1000000000000, "Mile": 0.621371, "Nautical-mile": 0.539957},
    "Inch": {"Inch":1,"Centimeter": 2.54, "Meter": 0.0254, "Kilometer": 0.0000254, "Foot": 0.0833333, "Yard": 0.0277778, "Millimeter": 25.4, "Micrometer": 25400, "Nanometer": 25400000, "Mile": 0.0000157828, "Nautical-mile": 0.0000137149},
    "Foot": {"Foot":1,"Centimeter": 30.48, "Meter": 0.3048, "Kilometer": 0.0003048, "Inch": 12, "Yard": 0.333333, "Millimeter": 304.8, "Micrometer": 304800, "Nanometer": 304800000, "Mile": 0.000189394, "Nautical-mile": 0.000164579},
    "Yard": {"Yard":1,"Centimeter": 91.44, "Meter": 0.9144, "Kilometer": 0.0009144, "Inch": 36, "Foot": 3, "Millimeter": 914.4, "Micrometer": 914400, "Nanometer": 914400000, "Mile": 0.000568182, "Nautical-mile": 0.000493737},
    "Millimeter": {"Millimeter":1,"Centimeter": 0.1, "Meter": 0.001, "Kilometer": 0.000001, "Inch": 0.0393701, "Foot": 0.00328084, "Yard": 0.00109361, "Micrometer": 1000, "Nanometer": 1000000, "Mile": 0.000000621371, "Nautical-mile": 0.000000539957},
    "Micrometer": { "Micrometer":1,"Centimeter": 0.0001, "Meter": 0.000001, "Kilometer": 0.000000001, "Inch": 0.0000393701, "Foot": 0.00000328084, "Yard": 0.00000109361, "Millimeter": 0.001, "Nanometer": 1000, "Mile": 0.000000000621371, "Nautical-mile": 0.000000000539957},
    "Nanometer": {"Nanometer":1,"Centimeter": 0.0000001, "Meter": 0.000000001, "Kilometer": 0.000000000001, "Inch": 0.0000000393701, "Foot": 0.00000000328084, "Yard": 0.00000000109361, "Millimeter": 0.000001, "Micrometer": 0.001, "Mile": 0.000000000000621371, "Nautical-mile": 0.000000000000539957},
    "Mile": {"Mile":1,"Centimeter": 160934, "Meter": 1609.34, "Kilometer": 1.60934, "Inch": 63360, "Foot": 5280, "Yard": 1760, "Millimeter": 1609340, "Micrometer": 1609340000, "Nanometer": 1609340000000, "Nautical-mile": 0.868976},
    "Nautical-mile": {"Nautical-mile":1,"Centimeter": 185200, "Meter": 1852, "Kilometer": 1.852, "Inch": 72913.4, "Foot": 6076.12, "Yard": 2025.37, "Millimeter": 1852000, "Micrometer": 1852000000, "Nanometer": 1852000000000, "Mile": 1.15078}
}

    
    if user_input > 0:
        if from_unit in length_conversion_factors and to_unit in length_conversion_factors[from_unit]:
            result = user_input * length_conversion_factors[from_unit][to_unit]
            
            # Show result
            st.success(f"✅ **{user_input} {from_unit} = {result:.6f} {to_unit}**")

            # Data for full table display
            converted_values = {unit: user_input * factor for unit, factor in length_conversion_factors[from_unit].items()}

        if st.checkbox("📊 Show all conversion",key="length_conversion_checkbox"):
            # Create DataFrame
            df = pd.DataFrame(list(converted_values.items()), columns=["To_unit", "Value"])
            df.insert(0, "S.No", range(1, len(df) + 1))
            df.set_index("S.No", inplace=True)

            st.title("Other Conversion")
            # Show table
            st.dataframe(df, use_container_width=True)
      
            
    
#Temperature conversion    
with tab2:
    st.write(f"🌡️ Convert different Temperature units below:")
    temperature_from_unit = st.selectbox("From unit:", (["Degree Celsius","Fahrenheit","Kelvin"]))
    temperature_user_input = st.number_input("Enter an temperature value:",min_value=0.0, format="%.6f")
    temperature_to_unit = st.selectbox("To unit:", (["Degree Celsius","Fahrenheit","Kelvin"]))
    
    temperature_conversion_factors = {
    "Degree Celsius": {
        "Fahrenheit": lambda c: (c * 9/5) + 32,
        "Kelvin": lambda c: c + 273.15,
        "Degree Celsius": lambda c: 1
    },
    "Fahrenheit": {
        "Degree Celsius": lambda f: (f - 32) * 5/9,
        "Kelvin": lambda f: (f - 32) * 5/9 + 273.15,
        "Fahrenheit": lambda f: 1
    },
    "Kelvin": {
        "Degree Celsius": lambda k: k - 273.15,
        "Fahrenheit": lambda k: (k - 273.15) * 9/5 + 32,
        "Kelvin": lambda k: 1
    }
    }
    if temperature_user_input > 0:
        if temperature_from_unit in temperature_conversion_factors and temperature_to_unit in temperature_conversion_factors[temperature_from_unit]:
            try:
                conversion_function = temperature_conversion_factors[temperature_from_unit][temperature_to_unit]
                result = conversion_function(temperature_user_input)
                # Show result
                st.success(f"✅ **{temperature_user_input} {temperature_from_unit} = {result:.2f} {temperature_to_unit}**")
            except:
                st.write("Invalid units selected. Please check your input")
        
        if st.checkbox("📊 Show all conversions", key="temperature_conversion_checkbox"):       
             # Calculate converted values
            converted_values = {unit: factor(temperature_user_input) for unit, factor in temperature_conversion_factors[temperature_from_unit].items()}  
            # Create DataFrame
            df = pd.DataFrame(list(converted_values.items()), columns=["To_unit", "Value"])
            df.insert(0, "S.No", range(1, len(df) + 1))
            df.set_index("S.No", inplace=True)

            st.title("Other Conversion")
            # Show table
            st.dataframe(df, use_container_width=True)
            
#For AREA Conversion
with tab3:
    st.write(f"📐 Convert different Area units below:")
    area_from_unit = st.selectbox("From unit: ", ["Square-Meter","Square-Centimeter","Square-Kilometer","Square-Inch","Square-Foot","Square-Yard","Hectare","Acre","Square-Mile"])
    area_user_input = st.number_input("Enter Area value:", min_value = 0.0, format="%.6f")
    area_to_unit = st.selectbox("To unit: ", ["Square-Meter","Square-Centimeter","Square-Kilometer","Square-Inch","Square-Foot","Square-Yard","Hectare","Acre","Square-Mile"])
    
    area_conversion_factors = {
        "Square-Meter": {"Square-Centimeter": 10000, "Square-Kilometer": 0.000001, "Square-Inch": 1550.0031, "Square-Foot": 10.7639, "Square-Yard": 1.19599, "Hectare": 0.0001, "Acre": 0.000247105, "Square-Mile": 3.86102e-7, "Square-Meter": 1},
        "Square-Centimeter": {"Square-Meter": 0.0001, "Square-Kilometer": 1e-10, "Square-Inch": 0.155, "Square-Foot": 0.00107639, "Square-Yard": 0.000119599, "Hectare": 1e-8, "Acre": 2.47105e-8, "Square-Mile": 3.86102e-11, "Square-Centimeter": 1},
        "Square-Kilometer": {"Square-Meter": 1e6, "Square-Centimeter": 1e10, "Square-Inch": 1.55e9, "Square-Foot": 1.076e7, "Square-Yard": 1.196e6, "Hectare": 100, "Acre": 247.105, "Square-Mile": 0.386102, "Square-Kilometer": 1},
        "Square-Inch": {"Square-Meter": 0.00064516, "Square-Centimeter": 6.4516, "Square-Kilometer": 6.4516e-10, "Square-Foot": 0.00694444, "Square-Yard": 0.000771605, "Hectare": 6.4516e-8, "Acre": 1.59423e-7, "Square-Mile": 2.49098e-10, "Square-Inch": 1},
        "Square-Foot": {"Square-Meter": 0.092903, "Square-Centimeter": 929.03, "Square-Kilometer": 9.2903e-8, "Square-Inch": 144, "Square-Yard": 0.111111, "Hectare": 9.2903e-6, "Acre": 0.0000229568, "Square-Mile": 3.58701e-8, "Square-Foot": 1},
        "Square-Yard": {"Square-Meter": 0.836127, "Square-Centimeter": 8361.27, "Square-Kilometer": 8.36127e-7, "Square-Inch": 1296, "Square-Foot": 9, "Hectare": 8.36127e-5, "Acre": 0.000206612, "Square-Mile": 3.22831e-7, "Square-Yard": 1},
        "Hectare": {"Square-Meter": 10000, "Square-Centimeter": 1e8, "Square-Kilometer": 0.01, "Square-Inch": 1.55e7, "Square-Foot": 107639, "Square-Yard": 11959.9, "Acre": 2.47105, "Square-Mile": 0.00386102, "Hectare": 1},
        "Acre": {"Square-Meter": 4046.86, "Square-Centimeter": 4.04686e7, "Square-Kilometer": 0.00404686, "Square-Inch": 6.273e6, "Square-Foot": 43560, "Square-Yard": 4840, "Hectare": 0.404686, "Square-Mile": 0.0015625, "Acre": 1},
        "Square-Mile": {"Square-Meter": 2.59e6, "Square-Centimeter": 2.59e10, "Square-Kilometer": 2.59, "Square-Inch": 4.014e9, "Square-Foot": 2.788e7, "Square-Yard": 3.098e6, "Hectare": 259, "Acre": 640, "Square-Mile": 1}
    }
    
    #calculating area unit
    if area_user_input > 0:
        try:
            if area_from_unit in area_conversion_factors and area_to_unit in area_conversion_factors[area_from_unit]:
                result = area_user_input * area_conversion_factors[area_from_unit][area_to_unit]
            #       Show result
                st.success(f"✅ **{area_user_input} {area_from_unit} = {result:.6f} {area_to_unit}**")
        except:
            st.write("Invalid units selected. Please check your input")
        
        if st.checkbox("📊 Show all conversions",key="area_conversion_checkbox"):        
            # Data for full table display
            converted_values = {unit: area_user_input * factor for unit, factor in area_conversion_factors[area_from_unit].items()}

                    # Create DataFrame
            df = pd.DataFrame(list(converted_values.items()), columns=["To_unit", "Value"])
            df.insert(0, "S.No", range(1, len(df) + 1))
            df.set_index("S.No", inplace=True)

            st.title("Other Conversion")
                    # Show table
            st.dataframe(df, use_container_width=True)
            
            
#Conversion for Mass unit
with tab4:
    st.write(f"⚖️ Convert different Mass units below:")
    mass_from_unit = st.selectbox("From unit:", (["Kilogram","Gram","Milligram","Metric-Ton","Pound","Ounce","Stone","US-Ton","Imperial-Ton"]))
    mass_user_input = st.number_input("Enter an mass value:",min_value=0.0, format="%.6f")
    mass_to_unit = st.selectbox("To unit:", (["Kilogram","Gram","Milligram","Metric-Ton","Pound","Ounce","Stone","US-Ton","Imperial-Ton"]))
            
    mass_conversion_factors = {"Kilogram": {"Kilogram": 1, "Gram": 1000, "Milligram": 1e6, "Metric-Ton": 0.001, "Pound": 2.20462, "Ounce": 35.274, "Stone": 0.157473, "US-Ton": 0.00110231, "Imperial-Ton": 0.000984207}, 
                               "Gram": {"Gram": 1, "Kilogram": 0.001, "Milligram": 1000, "Metric-Ton": 1e-6, "Pound": 0.00220462, "Ounce": 0.035274, "Stone": 0.000157473, "US-Ton": 1.10231e-6, "Imperial-Ton": 9.84207e-7}, 
                               "Milligram": {"Milligram":1,"Kilogram": 1e-6, "Gram": 0.001, "Metric-Ton": 1e-9, "Pound": 2.20462e-6, "Ounce": 3.5274e-5, "Stone": 1.57473e-7, "US-Ton": 1.10231e-9, "Imperial-Ton": 9.84207e-10}, 
                               "Metric-Ton": {"Metric-Ton":1,"Kilogram": 1000, "Gram": 1e6, "Milligram": 1e9, "Pound": 2204.62, "Ounce": 35274, "Stone": 157.473, "US-Ton": 1.10231, "Imperial-Ton": 0.984207}, 
                               "Pound": {"Pound":1,"Kilogram": 0.453592, "Gram": 453.592, "Milligram": 453592, "Metric-Ton": 0.000453592, "Ounce": 16, "Stone": 0.0714286, "US-Ton": 0.0005, "Imperial-Ton": 0.000446429}, 
                               "Ounce": {"Ounce":1,"Kilogram": 0.0283495, "Gram": 28.3495, "Milligram": 28349.5, "Metric-Ton": 2.83495e-5, "Pound": 0.0625, "Stone": 0.00446429, "US-Ton": 3.125e-5, "Imperial-Ton": 2.79018e-5}, 
                               "Stone": {"Stone":1,"Kilogram": 6.35029, "Gram": 6350.29, "Milligram": 6.35029e6, "Metric-Ton": 0.00635029, "Pound": 14, "Ounce": 224, "US-Ton": 0.007, "Imperial-Ton": 0.00625}, 
                               "US-Ton": {"US-Ton":1,"Kilogram": 907.185, "Gram": 907185, "Milligram": 9.07185e8, "Metric-Ton": 0.907185, "Pound": 2000, "Ounce": 32000, "Stone": 142.857, "Imperial-Ton": 0.892857}, 
                               "Imperial-Ton": {"Imperial-Ton":1,"Kilogram": 1016.05, "Gram": 1.01605e6, "Milligram": 1.01605e9, "Metric-Ton": 1.01605, "Pound": 2240, "Ounce": 35840, "Stone": 160, "US-Ton": 1.12}}
    
    if mass_user_input > 0:
        try:
            if mass_from_unit in mass_conversion_factors and mass_to_unit in mass_conversion_factors[mass_from_unit]:
                result = mass_user_input * mass_conversion_factors[mass_from_unit][mass_to_unit]
                st.success(f"✅ **{mass_user_input} {mass_from_unit} = {result:.6f} {mass_to_unit}**")
        except:
            st.write("Invalid unit selected. Please check your input")
    
        if st.checkbox("📊 Show all Conversion",key="mass_conversion_checkbox"):
            # Data for full table display
            converted_values = {unit: mass_user_input * factor for unit, factor in mass_conversion_factors[mass_from_unit].items()}
                    # Create DataFrame
            df = pd.DataFrame(list(converted_values.items()), columns=["To_unit", "Value"])
            df.insert(0, "S.No", range(1, len(df) + 1))
            df.set_index("S.No", inplace=True)

            st.title("Other Conversion")
                    # Show table
            st.dataframe(df, use_container_width=True)
            
#convsersion for Volume
with tab5:
    st.write(f"🧪 Convert different Volume units below:")
    volume_from_unit = st.selectbox("From unit:",(["Liter","Milliliter","Teaspoon", "Tablespoon","Imperial-Gallon","Imperial-Fluid-Ounce","Imperial-Pint","Imperial-Quart","US-Fluid-Ounce","US-Gallon","US-Quart","US-Pint","Cubic-Meter","Cubic-Centimeter","Cubic-Inch","Cubic-Foot"]))
    volume_user_input = st.number_input("Enter an volume value:",min_value=0.0, format="%.6f")
    volume_to_unit = st.selectbox("To unit:", (["Liter","Milliliter","Teaspoon", "Tablespoon","Imperial-Gallon","Imperial-Fluid-Ounce","Imperial-Pint","Imperial-Quart","US-Fluid-Ounce","US-Gallon","US-Quart","US-Pint","Cubic-Meter","Cubic-Centimeter","Cubic-Inch","Cubic-Foot"]))
    
    volume_conversion_factors = {
    "Liter": {"Liter":1,"Milliliter": 1000, "Cubic-Meter": 0.001, "Cubic-Centimeter": 1000, "Cubic-Inch": 61.0237, "Cubic-Foot": 0.0353147, "US-Gallon": 0.264172, "US-Quart": 1.05669, "US-Pint": 2.11338, "US-Fluid-Ounce": 33.814, "Imperial-Gallon": 0.219969, "Imperial-Quart": 0.879877, "Imperial-Pint": 1.75975, "Imperial-Fluid-Ounce": 35.1951, "Teaspoon": 202.884, "Tablespoon": 67.628},
    "Milliliter": {"Milliliter":1,"Liter": 0.001, "Cubic-Meter": 1e-6, "Cubic-Centimeter": 1, "Cubic-Inch": 0.0610237, "Cubic-Foot": 0.0000353147, "US-Gallon": 0.000264172, "US-Quart": 0.00105669, "US-Pint": 0.00211338, "US-Fluid-Ounce": 0.033814, "Imperial-Gallon": 0.000219969, "Imperial-Quart": 0.000879877, "Imperial-Pint": 0.00175975, "Imperial-Fluid-Ounce": 0.0351951, "Teaspoon": 0.202884, "Tablespoon": 0.067628},
    "Cubic-Meter": {"Cubic-Meter":1,"Liter": 1000, "Milliliter": 1e6, "Cubic-Centimeter": 1e6, "Cubic-Inch": 61023.7, "Cubic-Foot": 35.3147, "US-Gallon": 264.172, "US-Quart": 1056.69, "US-Pint": 2113.38, "US-Fluid-Ounce": 33814, "Imperial-Gallon": 219.969, "Imperial-Quart": 879.877, "Imperial-Pint": 1759.75, "Imperial-Fluid-Ounce": 35195.1, "Teaspoon": 202884, "Tablespoon": 67628},
    "Cubic-Centimeter": {"Cubic-Centimeter":1,"Liter": 0.001, "Milliliter": 1, "Cubic-Meter": 1e-6, "Cubic-Inch": 0.0610237, "Cubic-Foot": 0.0000353147, "US-Gallon": 0.000264172, "US-Quart": 0.00105669, "US-Pint": 0.00211338, "US-Fluid-Ounce": 0.033814, "Imperial-Gallon": 0.000219969, "Imperial-Quart": 0.000879877, "Imperial-Pint": 0.00175975, "Imperial-Fluid-Ounce": 0.0351951, "Teaspoon": 0.202884, "Tablespoon": 0.067628},
    "Cubic-Inch": {"Cubic-Inch":1,"Liter": 0.0163871, "Milliliter": 16.3871, "Cubic-Meter": 0.0000163871, "Cubic-Centimeter": 16.3871, "Cubic-Foot": 0.000578704, "US-Gallon": 0.004329, "US-Quart": 0.017316, "US-Pint": 0.034632, "US-Fluid-Ounce": 0.554113, "Imperial-Gallon": 0.00360465, "Imperial-Quart": 0.0144186, "Imperial-Pint": 0.0288372, "Imperial-Fluid-Ounce": 0.576744, "Teaspoon": 3.32468, "Tablespoon": 1.10823},
    "Cubic-Foot": {"Cubic-Foot":1,"Liter": 28.3168, "Milliliter": 28316.8, "Cubic-Meter": 0.0283168, "Cubic-Centimeter": 28316.8, "Cubic-Inch": 1728, "US-Gallon": 7.48052, "US-Quart": 29.9221, "US-Pint": 59.8442, "US-Fluid-Ounce": 957.506, "Imperial-Gallon": 6.22884, "Imperial-Quart": 24.9153, "Imperial-Pint": 49.8307, "Imperial-Fluid-Ounce": 996.614, "Teaspoon": 5745.04, "Tablespoon": 1915.01},
    "US-Gallon": {"US-Gallon":1,"Liter": 3.78541, "Milliliter": 3785.41, "Cubic-Meter": 0.00378541, "Cubic-Centimeter": 3785.41, "Cubic-Inch": 231, "Cubic-Foot": 0.133681, "US-Quart": 4, "US-Pint": 8, "US-Fluid-Ounce": 128, "Imperial-Gallon": 0.832674, "Imperial-Quart": 3.3307, "Imperial-Pint": 6.66139, "Imperial-Fluid-Ounce": 133.228, "Teaspoon": 768, "Tablespoon": 256},
    "US-Quart": {"US-Quart":1,"Liter": 0.946353, "Milliliter": 946.353, "Cubic-Meter": 0.000946353, "Cubic-Centimeter": 946.353, "Cubic-Inch": 57.75, "Cubic-Foot": 0.0334201, "US-Gallon": 0.25, "US-Pint": 2, "US-Fluid-Ounce": 32, "Imperial-Gallon": 0.208169, "Imperial-Quart": 0.832674, "Imperial-Pint": 1.66535, "Imperial-Fluid-Ounce": 33.307, "Teaspoon": 192, "Tablespoon": 64},
    "US-Pint": {"US-Pint":1,"Liter": 0.473176, "Milliliter": 473.176, "Cubic-Meter": 0.000473176, "Cubic-Centimeter": 473.176, "Cubic-Inch": 28.875, "Cubic-Foot": 0.0167101, "US-Gallon": 0.125, "US-Quart": 0.5, "US-Fluid-Ounce": 16, "Imperial-Gallon": 0.104084, "Imperial-Quart": 0.416337, "Imperial-Pint": 0.832674, "Imperial-Fluid-Ounce": 16.6535, "Teaspoon": 96, "Tablespoon": 32},
    "US-Fluid-Ounce": {"US-Fluid-Ounce":1,"Liter": 0.0295735, "Milliliter": 29.5735, "Cubic-Meter": 0.0000295735, "Cubic-Centimeter": 29.5735, "Cubic-Inch": 1.80469, "Cubic-Foot": 0.00104438, "US-Gallon": 0.0078125, "US-Quart": 0.03125, "US-Pint": 0.0625, "Imperial-Gallon": 0.00650527, "Imperial-Quart": 0.0260211, "Imperial-Pint": 0.0520421, "Imperial-Fluid-Ounce": 1.04084, "Teaspoon": 6, "Tablespoon": 2},
    "Imperial-Gallon": {"Imperial-Gallon":1,"Liter": 4.54609, "Milliliter": 4546.09, "Cubic-Meter": 0.00454609, "Cubic-Centimeter": 4546.09, "Cubic-Inch": 277.419, "Cubic-Foot": 0.160544, "US-Gallon": 1.20095, "US-Quart": 4.8038, "US-Pint": 9.6076, "US-Fluid-Ounce": 153.722, "Imperial-Quart": 4, "Imperial-Pint": 8, "Imperial-Fluid-Ounce": 160, "Teaspoon": 922.33, "Tablespoon": 307.443},
    "Imperial-Quart": {"Imperial-Quart":1,"Liter": 1.13652, "Milliliter": 1136.52, "Cubic-Meter": 0.00113652, "Cubic-Centimeter": 1136.52, "Cubic-Inch": 69.3549, "Cubic-Foot": 0.0401359, "US-Gallon": 0.300237, "US-Quart": 1.20095, "US-Pint": 2.4019, "US-Fluid-Ounce": 38.4304, "Imperial-Gallon": 0.25, "Imperial-Pint": 2, "Imperial-Fluid-Ounce": 40, "Teaspoon": 230.582, "Tablespoon": 76.8608},
    "Imperial-Pint": {"Imperial-Pint":1,"Liter": 0.568261, "Milliliter": 568.261, "Cubic-Meter": 0.000568261, "Cubic-Centimeter": 568.261, "Cubic-Inch": 34.6774, "Cubic-Foot": 0.020068, "US-Gallon": 0.150119, "US-Quart": 0.600475, "US-Pint": 1.20095, "US-Fluid-Ounce": 19.2152, "Imperial-Gallon": 0.125, "Imperial-Quart": 0.5, "Imperial-Fluid-Ounce": 20, "Teaspoon": 115.291, "Tablespoon": 38.4304},
    "Imperial-Fluid-Ounce": {"Imperial-Fluid-Ounce":1,"Liter": 0.0284131, "Milliliter": 28.4131, "Cubic-Meter": 0.0000284131, "Cubic-Centimeter": 28.4131, "Cubic-Inch": 1.73387, "Cubic-Foot": 0.0010034, "US-Gallon": 0.00750594, "US-Quart": 0.0300237, "US-Pint": 0.0600475, "US-Fluid-Ounce": 0.96076, "Imperial-Gallon": 0.00625, "Imperial-Quart": 0.025, "Imperial-Pint": 0.05, "Teaspoon": 5.76456, "Tablespoon": 1.92152},
    "Teaspoon": {"Teaspoon":1,"Liter": 0.00492892, "Milliliter": 4.92892, "Cubic-Meter": 0.00000492892, "Cubic-Centimeter": 4.92892, "Cubic-Inch": 0.300781, "Cubic-Foot": 0.000174063, "US-Gallon": 0.00130208, "US-Quart": 0.00520833, "US-Pint": 0.0104167, "US-Fluid-Ounce": 0.166667, "Imperial-Gallon": 0.00108421, "Imperial-Quart": 0.00433684, "Imperial-Pint": 0.00867369, "Imperial-Fluid-Ounce": 0.173474},
    "Tablespoon": { "Tablespoon":1,"Liter": 0.0147868, "Milliliter": 14.7868, "Cubic-Meter": 0.0000147868, "Cubic-Centimeter": 14.7868, "Cubic-Inch": 0.902344, "Cubic-Foot": 0.00052219, "US-Gallon": 0.00390625, "US-Quart": 0.015625, "US-Pint": 0.03125, "US-Fluid-Ounce": 0.5, "Imperial-Gallon": 0.00325263, "Imperial-Quart": 0.0130105, "Imperial-Pint": 0.0260211, "Imperial-Fluid-Ounce": 0.520421}
}

    if volume_user_input > 0:
        if volume_from_unit in volume_conversion_factors and volume_to_unit in volume_conversion_factors[volume_from_unit]:
            try:
                result = volume_user_input * volume_conversion_factors[volume_from_unit][volume_to_unit]
                st.success(f"✅ **{volume_user_input} {volume_from_unit} = {result:.6f} {volume_to_unit}**")
            except:
                st.write("Invalid unit selected. Please check your input")
        
        if st.checkbox("📊 Show All conversion", key="volume_conversion_checkbox"):
            # Data for full table display
            converted_values = {unit: volume_user_input* factor for unit, factor in volume_conversion_factors[volume_from_unit].items()}
                    # Create DataFrame
            df = pd.DataFrame(list(converted_values.items()), columns=["To_unit", "Value"])
            df.insert(0, "S.No", range(1, len(df) + 1))
            df.set_index("S.No", inplace=True)

            st.title("Other Conversion")
                    # Show table
            st.dataframe(df, use_container_width=True)
            
#Conversion for Time 
with tab6:
    st.write(f"⏰ Convert different Time unit below:")
    time_from_unit = st.selectbox("From unit:",(["Second","Millisecond","Minute","Hour","Day", "Week","Month","Year"]))
    time_user_input = st.number_input("Enter an time value:", min_value = 0.0, format="%.6f")
    time_to_unit = st.selectbox("To unit:",(["Second","Millisecond","Minute","Hour","Day", "Week","Month","Year"]))
    
    time_conversion_factors = {
    "Second": {"Second":1,"Millisecond": 1000, "Minute": 0.0166667, "Hour": 0.000277778, "Day": 0.0000115741, "Week": 0.00000165344, "Month": 3.80517e-7, "Year": 3.16881e-8},
    "Millisecond": {"Millisecond":1,"Second": 0.001, "Minute": 0.0000166667, "Hour": 2.77778e-7, "Day": 1.15741e-8, "Week": 1.65344e-9, "Month": 3.80517e-10, "Year": 3.16881e-11},
    "Minute": {"Minute":1,"Second": 60, "Millisecond": 60000, "Hour": 0.0166667, "Day": 0.000694444, "Week": 0.0000992063, "Month": 0.000022831, "Year": 0.00000190129},
    "Hour": {"Hour":1,"Second": 3600, "Millisecond": 3.6e6, "Minute": 60, "Day": 0.0416667, "Week": 0.00595238, "Month": 0.00136986, "Year": 0.000114155},
    "Day": {"Day":1,"Second": 86400, "Millisecond": 8.64e7, "Minute": 1440, "Hour": 24, "Week": 0.142857, "Month": 0.0328767, "Year": 0.00273785},
    "Week": { "Week":1,"Second": 604800, "Millisecond": 6.048e8, "Minute": 10080, "Hour": 168, "Day": 7, "Month": 0.230137, "Year": 0.0191649},
    "Month": {"Month":1,"Second": 2.628e6, "Millisecond": 2.628e9, "Minute": 43800, "Hour": 730.001, "Day": 30.4167, "Week": 4.34524, "Year": 0.0833333},
    "Year": {"Year":1,"Second": 3.154e7, "Millisecond": 3.154e10, "Minute": 525600, "Hour": 8760, "Day": 365, "Week": 52.1429, "Month": 12}
}
    if time_user_input > 0:
        if time_from_unit in time_conversion_factors and time_to_unit in time_conversion_factors[time_from_unit]:
            try:
                result = time_user_input * time_conversion_factors[time_from_unit][time_to_unit]
                st.success(f"✅ **{time_user_input} {time_from_unit} = {result:.4f} {time_to_unit}**")
            except:
                st.write("Invalid unit selected. Please check your input")
        
            if st.checkbox("📊 Show All conversion", key="time_conversion_checkbox"):
                # Data for full table display
                converted_values = {unit: time_user_input * factor for unit, factor in time_conversion_factors[time_from_unit].items()}
                        # Create DataFrame
                df = pd.DataFrame(list(converted_values.items()), columns=["To_unit", "Value"])
                df.insert(0, "S.No", range(1, len(df) + 1))
                df.set_index("S.No", inplace=True)

                st.title("Other Conversion")
                        # Show table
                st.dataframe(df, use_container_width=True)
 
st.markdown("---")                
st.markdown(
    """
    <style>
        .footer{
            position: fixed,
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #f1f1f1;
            color: black;
            padding: 10px;
            text-align: center;
        }
    </style>
    <div class="footer">
        Develop by <strong>Fahad Warsi</strong>
    </div>
    """,
    unsafe_allow_html=True
    
)
