
include_directories(
    ${Boost_INCLUDE_DIRS}
    ${OCC_INCLUDE_DIR}
    ${PYTHON_INCLUDE_DIRS}
    ${ZLIB_INCLUDE_DIR}
    ${XercesC_INCLUDE_DIRS}
)

set(Library_LIBS
    FreeCADApp
)

SET(Library_SRCS
    AppLibrary.cpp
    PreCompiled.cpp
    PreCompiled.h
)

add_library(Library SHARED ${Library_SRCS})
target_link_libraries(Library ${Library_LIBS})


SET_BIN_DIR(Library Library /Mod/Library)
SET_PYTHON_PREFIX_SUFFIX(Library)

install(TARGETS Library DESTINATION ${CMAKE_INSTALL_LIBDIR})
