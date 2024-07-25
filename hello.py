def fahrenheit_to_celsius(fahrenheit): 
    celsius = (fahrenheit - 32) * 5/9 
    return celsius 
 
# Example usage 
fahrenheit_value = 32 
celsius_value = fahrenheit_to_celsius(fahrenheit_value) 
print(f"{fahrenheit_value} degrees Fahrenheit is equal to {celsius_value:.2f} degrees Celsius.") 
