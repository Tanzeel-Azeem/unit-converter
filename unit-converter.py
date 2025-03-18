import streamlit 

streamlit.title(" Unit Converter App 😄🤩")
streamlit.markdown("### An App where you can convert Lenght, Weight, Time and Temprature")
streamlit.write (" Select a Category, Convert it and get the Result ")

#                             ALL THE MAIN CATREGORIES ARE HERE                          
category = streamlit.selectbox("Choose your Category", ["lenght", "Weight", "Time", "Temprature"])


def convert_func ( category, value, unit  ) :

    if (category == "lenght" ):
        if unit == "kilometer to mile":
            return value * 0.621371
        elif (unit == "mile to kilometer"):
            return value  * 1.60934
        elif (unit == "kilometer to feet"):
            return value * 3280.84
        elif (unit == "feet to kilometer"):
            return value * 0.0003048
        elif (unit == "mile to feet"):
            return value * 5280
        elif (unit == "feet to mile"):
            return value * 0.000189394  
        
        #           WEIGHT 
        
    elif (category == "Weight"):
        if (unit == "kilogram to pound"):
            return value * 2.20462
        elif (unit == "pound to kilogram"):
            return value * 0.453592
        elif (unit == "kilogram to gram"):
            return value * 1000
        elif (unit == "gram to kilogram"):
            return value * 0.001
        elif (unit == "pound to gram"):
            return value * 453.592
        elif (unit == "gram to pound"):
            return value / 453.592
        
            # TIME

    elif (category == "Time"):
        if (unit == "hour to minutes"):
            return value * 60
        elif (unit == "minutes to hour"):
            return value / 60
        elif (unit == "minutes to second"):
            return value * 60
        elif (unit == "second to minutes"):
            return value / 60
        elif (unit == "hour to second"):
            return value * 3600
        elif (unit == "second to hour"):   
            return value / 3600     

#           TEMPRATURE
    elif ( category == "Temprature"):
        if ( unit == "celcius to fahrenheit"):
            return (value * 9/5) + 32 
        elif (unit == "fahrenheit  to celcius"):
            return (value - 32) * 5/9
 



if (category == "lenght"):
    unit = streamlit.selectbox ("📏 Please Select one", ['kilometer to mile', 'mile to kilometer', 'kilometer to feet', 'feet to kilometer', 'mile to feet', 'feet to mile' ])

elif ( category == "Weight"):
    unit = streamlit.selectbox ("⚖ Please select one", ['kilogram to pound', 'pound to kilogram', 'kilogram to gram', 'gram to kilogram', 'pound to gram', 'gram to pound'])

elif (category == "Time"):
    unit = streamlit.selectbox ("⏳ Please Select one", ['hour to minutes', 'minutes to hour', 'minutes to second', 'second to minutes', 'hour to second', 'second to hour'])

elif (category == "Temprature"):
    unit = streamlit.selectbox ("🌡 Please Select one", ['celcius to fahrenheit', 'fahrenheit  to celcius'])


value = streamlit.number_input("Please Enter the value to Convert")

if (streamlit.button("Convert")):
    result = convert_func (category, value, unit )
    streamlit.success( f"The Result is {result: .2f}  🤩🎉✨" )
    streamlit.balloons()