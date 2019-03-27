
if(MSVC)
    add_definitions(-DHAVE_ACOSH -DHAVE_ATANH -DHAVE_ASINH)
else(MSVC)
    add_definitions(-DHAVE_LIMITS_H -DHAVE_CONFIG_H)
endif(MSVC)

include_directories(
    ${CMAKE_BINARY_DIR}
    ${CMAKE_SOURCE_DIR}/src
    ${CMAKE_CURRENT_BINARY_DIR}
    ${Boost_INCLUDE_DIRS}
    ${OCC_INCLUDE_DIR}
    ${COIN3D_INCLUDE_DIRS}
    ${ZLIB_INCLUDE_DIR}
    ${PYTHON_INCLUDE_DIRS}
    ${XercesC_INCLUDE_DIRS}
    ${EIGEN3_INCLUDE_DIR}
)

set(LibraryGui_LIBS
    Library
    PartDesignGui
    SketcherGui
    PartGui
    SketcherGui
    FreeCADGui
)

if (BUILD_QT5)
    qt5_add_resources(Library_QRC_SRCS Resources/Library.qrc)
else()
    qt4_add_resources(Library_QRC_SRCS Resources/Library.qrc)
endif()

SET(LibraryGui_SRCS
    ${Library_QRC_SRCS}
    AppLibraryGui.cpp
    Command.cpp
    PreCompiled.cpp
    PreCompiled.h
    Workbench.cpp
    Workbench.h
)

add_library(LibraryGui SHARED ${LibraryGui_SRCS})
target_link_libraries(LibraryGui ${LibraryGui_LIBS})

fc_target_copy_resource(LibraryGui 
    ${CMAKE_SOURCE_DIR}/src/Tools/Library
    ${CMAKE_BINARY_DIR}/Mod/Library
    InitGui.py)

SET_BIN_DIR(LibraryGui LibraryGui /Mod/Library)
SET_PYTHON_PREFIX_SUFFIX(LibraryGui)
    
install(TARGETS LibraryGui DESTINATION ${CMAKE_INSTALL_LIBDIR})
