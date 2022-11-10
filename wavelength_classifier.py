#
# Student Name: Craig Lassiter
# Date:8/22/2022
# Wavelength Classifier
# Determine the classification of the wavelength


wavelength = int(input('Enter the wavelength (in nm): '))
# and display the result.
# Get the wavelength.
if wavelength <= 9:
    print('Below range')
elif wavelength < 401:
    print('Infrared')
elif 401 <= wavelength <= 700:
    print('Visible light')
elif 701 <= wavelength <= 1000:
    print('Ultraviolet')
elif wavelength >= 1001:
    print('Above range')

