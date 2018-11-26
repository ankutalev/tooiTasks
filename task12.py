import os
import collections
import math


class TfidfCalculator:
    __dir_name: str = "."  # directory where files located
    __files_in_work_dir: [str] = []
    __word_counters: {str, collections.Counter} = {}
    __tf_indexes: {str: {str: float}} = {}
    __idf_indexes: {str: {str: float}} = {}

    def __init__(self, dir_name: str):
        self.__dir_name = dir_name
        self.__files_in_work_dir = os.listdir(dir_name)
        print(self.__files_in_work_dir)
        self.__files_in_work_dir = [os.path.join(self.__dir_name, f) for f in self.__files_in_work_dir if
                                    os.path.isfile(os.path.join(self.__dir_name, f))]
        for f in self.__files_in_work_dir:
            self.__word_counters[f] = collections.Counter()

    def info(self):
        print("Work directory ", self.__dir_name)
        print("Files for calc ", self.__files_in_work_dir)

    def __calc_tf_index(self):
        for file_name in self.__files_in_work_dir:
            file = open(file_name, "r")
            words_in_file: int = 0
            self.__tf_indexes[file_name] = {}
            for line in file:
                words = line.split(" ")
                words_in_file += len(words)
                for word in words:
                    self.__word_counters[file_name][word] += 1

            for word in self.__word_counters[file_name]:
                self.__tf_indexes[file_name][word] = self.__word_counters[file_name][word] / words_in_file
            file.close()
        print(self.__tf_indexes)

    def __calc_idf_index(self):
        for file_name in self.__files_in_work_dir:
            file = open(file_name, "r")
            presence_in_files = 0
            self.__idf_indexes[file_name] = {}
            for line in file:
                words = line.split(" ")
                for word in words:
                    for counter in self.__word_counters.values():
                        if counter[word] != 0:
                            presence_in_files += 1
                    self.__idf_indexes[file_name][word] = math.log(len(self.__files_in_work_dir) / presence_in_files,
                                                                   10)
                    presence_in_files = 0
            file.close()
        print(self.__idf_indexes)

    def calc_tf_idf(self):
        self.__calc_tf_index()
        self.__calc_idf_index()
        for file in self.__files_in_work_dir:
            for word in self.__idf_indexes[file]:
                print("IN FILE ", file, "FOR WORD ", word, " TF_IDF INDEX IS",
                      self.__idf_indexes[file][word] * self.__tf_indexes[file][word])


x = TfidfCalculator("texts")
x.info()
x.calc_tf_idf()
