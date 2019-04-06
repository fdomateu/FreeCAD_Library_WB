
add_subdirectory(App)
if(BUILD_GUI)
    add_subdirectory(Gui)
endif(BUILD_GUI)

set(Library_Scripts
    Init.py
)

if(BUILD_GUI)
    list (APPEND Library_Scripts InitGui.py)
endif(BUILD_GUI)

add_custom_target(LibraryScripts ALL
    SOURCES ${Library_Scripts}
)

fc_target_copy_resource_flat(LibraryScripts
    ${CMAKE_CURRENT_SOURCE_DIR}
    ${CMAKE_BINARY_DIR}/Mod/Library
    ${Library_Scripts}
)

install(
    FILES
        ${Library_Scripts}
    DESTINATION
        Mod/Library
)
