cmake_minimum_required(VERSION 3.31)
project(AI DRIVE SMART ATTENDANCE MANAGEMENT SYSTEM)

# Set the Python interpreter path if needed
find_package(Python3 REQUIRED)

# Set the path for your scripts
set(SOURCE_FILES
    app.py
    attendence_taker.py
    features_extraction_to_csv.py
    get_faces_from_camera_tkinter.py
)

# Install the scripts
install(PROGRAMS ${SOURCE_FILES} DESTINATION bin)

# Include directories if you have any additional libraries
# include_directories(include)
