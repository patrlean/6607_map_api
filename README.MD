# Address Geocoding Conversion Tool

## Project Overview
This is a Python tool that uses the Google Maps API to convert addresses into latitude and longitude coordinates. The tool can batch process address data in Excel files and output a new Excel file containing geographic coordinate information.

## Features
- Batch processing of addresses in Excel files
- Automatic retrieval of latitude and longitude coordinates for addresses
- Progress bar showing processing status
- Error handling and logging
- Support for API request rate limiting

## Requirements
- Python 3.x
- Required packages (see requirements.txt)

## Installation
1. Clone or download this project
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration
Configure the `config.py` file before use:
- `GOOGLE_MAPS_API_KEY`: Your Google Maps API key
- `INPUT_FILE`: Path to input Excel file (default is "addr.xlsx")
- `OUTPUT_FILE`: Path to output Excel file (default is "addr_lat_lgt.xlsx")

## Input File Format
The input Excel file must contain a column named `addr` which contains the addresses to be converted.

## Usage
1. Prepare an Excel file containing address information
2. Configure the `config.py` file
3. Run the program:
   ```bash
   python main.py
   ```

## Output
The program will add two columns to the output file:
- `lat`: Latitude
- `lgt`: Longitude

## Important Notes
- Ensure you have a valid Google Maps API key
- Be aware of Google Maps API usage limits and billing
- Consider API rate limits when processing large amounts of data


