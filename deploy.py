from os import system

system("python ./scripts/build_wrapper.py")
system("push-dir --dir=a --branch=gh-pages --cleanup --verbose")
