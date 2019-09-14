#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
from conans.tools import download, unzip

class CeresSolverConan(ConanFile):
    name = "ceres-solver"
    version = "1.14.0"
    license = "New BSD"
    url = "https://github.com/ceres-solver/ceres-solver/"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    requires = "eigen/3.3.7@conan/stable", "glog/0.4.0@bincrafters/stable", "gflags/2.2.2@bincrafters/stable"

    def source(self):
        zip_name = self.version+".zip"
        download("https://github.com/ceres-solver/ceres-solver/archive/"+self.version+".zip", zip_name)
        unzip(zip_name)

    def build(self):
        cmake = CMake(self)
        cmake.definitions["BUILD_TESTING"] = False
        cmake.definitions["BUILD_EXAMPLES"] = False
        cmake.definitions["MINIGLOG"] = True

        cmake.configure( source_folder='ceres-solver-'+self.version)
        cmake.build()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
        if not self.cpp_info.libs:
            raise Exception("No libs collected")
