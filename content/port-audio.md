Title: Build and Use PortAudio on Linux (using CMake)
Date: 2021-11-13 08:26
Modified: 2021-11-13 08:26
Category: Linux
Tags: audio, linux, programming
Slug: port-audio-1
Authors: Will Frank
Summary: How to install, build, and use the PortAudio library on Linux.

## PortAudio - portable audio I/O library
PortAudio is a portable audio I/O library designed for cross-platform support of
audio. It uses either a callback mechanism to request audio processing, or
blocking read/write calls to buffer data between the native audio subsystem and
the client. Audio can be processed in various formats, including 32 bit floating
point, and will be converted to the native format internally.

## Installing the ALSA Development Kit
The OSS sound API is very old and not well supported. It is recommended that you
use the ALSA sound API. The PortAudio configure script will look for the ALSA
SDK. You can install the ALSA SDK on Ubuntu using:
```shell
sudo apt-get install libasound-dev
```
You might need to use yum, or some other package manager, instead of apt-get on
your machine.

If you do not install ALSA then you might get a message when testing that says
you have no audio devices.

You can find out more about ALSA here: <http://www.alsa-project.org/>

## Installing PortAudio
1. Get the latest stable release of PortAudio from [here](http://files.portaudio.com/download.html).
At the time of writing this is v19.7.0.
2. Extract the tarball `tar -xvzf pa_stable_v190700_20210406.tgz` to your
preferred location. I put it in `/opt/portaudio/`.
Alternatively, get the latest development version from GitHub:
```shell
git clone https://github.com/PortAudio/portaudio.git
```
3. PortAudio can be built and installed with CMake. You should obtain a recent 
version of CMake from <http://www.cmake.org> if you do not have one already.
```shell
cmake {portaudio path} -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/install_location
make
make install
```
Alternatively, standard GNU autotools configure/make can be used to build
PortAudio in Linux environments.
```shell
{portaudio path}/configure --prefix=/install_location
make
make install
```
On my system running Ubuntu 20.04.3 LTS, I installed PortAudio in `/usr/local/lib/`.

## Building with PortAudio using CMake
PortAudio defines the following CMake targets:

* `portaudio_static` for a static library
* `portaudio` for a dynamic library

To use the CMake package finder you need to tell CMake where to find PortAudio.
```shell
list(APPEND CMAKE_PREFIX_PATH /usr/local/lib/portaudio/)
```
then you may need to include some of the platform independent code headers if
you wish to use them.
```shell
target_include_directories(portaudio_test PRIVATE /opt/portaudio/src/common/)
```

A complete example `CMakeLists.txt` is:
```shell
cmake_minimum_required(VERSION 2.8)

project(portaudio_test)

# Set the build directory
set(CMAKE_BINARY_DIR ${CMAKE_SOURCE_DIR}/bin)
set(EXECUTABLE_OUTPUT_PATH ${CMAKE_BINARY_DIR})
set(LIBRARY_OUTPUT_PATH ${CMAKE_BINARY_DIR})

include_directories("${PROJECT_SOURCE_DIR}")

list(APPEND CMAKE_PREFIX_PATH /usr/local/lib/portaudio/)
find_package( portaudio REQUIRED )

add_executable(portaudio_test ${PROJECT_SOURCE_DIR}/portaudio_test.cpp)
target_include_directories(portaudio_test PRIVATE /opt/portaudio/src/common/)
target_link_libraries(portaudio_test portaudio)
```
## References
* [PortAudio](http://files.portaudio.com/)
* [https://github.com/PortAudio/portaudio](https://github.com/PortAudio/portaudio)
* [PortAudio on Windows, OS X or Linux via. CMake](http://www.portaudio.com/docs/v19-doxydocs/compile_cmake.html)