if(MSVC)
    add_definitions(-DFCAppLibrary -DHAVE_ACOSH -DHAVE_ASINH -DHAVE_ATANH)
else(MSVC)
    add_definitions(-DHAVE_LIMITS_H -DHAVE_CONFIG_H)
endif(MSVC)

include_directories(
    ${CMAKE_BINARY_DIR}
    ${CMAKE_SOURCE_DIR}/src
    ${CMAKE_BINARY_DIR}/src
    ${CMAKE_CURRENT_BINARY_DIR}
    ${Boost_INCLUDE_DIRS}
    ${OCC_INCLUDE_DIR}
    ${QT_INCLUDE_DIR}
    ${ZLIB_INCLUDE_DIR}
    ${PYTHON_INCLUDE_DIRS}
    ${XercesC_INCLUDE_DIRS}
    ${QT_INCLUDE_DIR}
)

set(Library_LIBS
    ${OCC_LIBRARIES}
    ${OCC_DEBUG_LIBRARIES}
    FreeCADApp
)

SET(Library_SRCS
    AppLibrary.cpp
    PreCompiled.cpp
    PreCompiled.h
)

add_library(Library SHARED ${Library_SRCS})
target_link_libraries(Library ${Library_LIBS})


fc_target_copy_resource(Library 
    ${CMAKE_SOURCE_DIR}/src/Tools/Library
    ${CMAKE_BINARY_DIR}/Mod/Library
    Init.py)

SET_BIN_DIR(Library Library /Mod/Library)
SET_PYTHON_PREFIX_SUFFIX(Library)

install(TARGETS Library DESTINATION ${CMAKE_INSTALL_LIBDIR})
