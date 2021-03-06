#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .electron import Electron
from .link import Link, rpc
from . import utils
from . import errors
from .logger import Logger
from .structures import CircularOrderedDict, CircularOrderedSet
from .custom_queue import ThreadingQueue
from .custom_threading import Thread, ThreadPool, should_stop

text_logo = """\n
         \033[93m◼◼◼\033[0m            \033[93m◼◼\033[0m    \033[93m◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼\033[0m    \033[93m◼◼◼\033[0m         \033[93m◼◼◼       ◼◼◼\033[0m           \033[93m◼◼\033[0m                \033[93m◼◼◼\033[0m
       \033[93m◼◼◼\033[0m             \033[93m◼◼◼◼\033[0m           \033[93m◼◼\033[0m          \033[93m◼◼◼\033[0m           \033[93m◼◼◼◼      ◼◼◼\033[0m          \033[93m◼◼◼◼\033[0m             \033[93m◼◼◼\033[0m
     \033[93m◼◼◼\033[0m             \033[93m◼◼◼  ◼◼◼\033[0m         \033[93m◼◼\033[0m        \033[93m◼◼◼\033[0m             \033[93m◼◼◼◼◼     ◼◼◼\033[0m        \033[93m◼◼◼  ◼◼◼\033[0m         \033[93m◼◼◼\033[0m
   \033[93m◼◼◼\033[0m              \033[93m◼◼◼    ◼◼◼\033[0m        \033[93m◼◼\033[0m      \033[93m◼◼◼\033[0m               \033[93m◼◼◼ ◼◼◼   ◼◼◼\033[0m       \033[93m◼◼◼    ◼◼◼\033[0m      \033[93m◼◼◼\033[0m
 \033[93m◼◼◼\033[0m               \033[93m◼◼◼      ◼◼◼\033[0m       \033[93m◼◼\033[0m    \033[93m◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼\033[0m  \033[93m◼◼◼  ◼◼◼  ◼◼◼\033[0m      \033[93m◼◼◼      ◼◼◼\033[0m   \033[93m◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼\033[0m
   \033[93m◼◼◼\033[0m            \033[93m◼◼◼        ◼◼◼\033[0m      \033[93m◼◼\033[0m      \033[93m◼◼◼\033[0m               \033[93m◼◼◼    ◼◼ ◼◼◼\033[0m     \033[93m◼◼◼        ◼◼◼\033[0m    \033[93m◼◼◼\033[0m
     \033[93m◼◼◼\033[0m         \033[93m◼◼◼          ◼◼◼\033[0m     \033[93m◼◼\033[0m        \033[93m◼◼◼\033[0m             \033[93m◼◼◼     ◼◼◼◼◼\033[0m    \033[93m◼◼◼          ◼◼◼\033[0m     \033[93m◼◼◼\033[0m
       \033[93m◼◼◼\033[0m      \033[93m◼◼◼            ◼◼◼\033[0m    \033[93m◼◼\033[0m          \033[93m◼◼◼\033[0m           \033[93m◼◼◼      ◼◼◼◼\033[0m   \033[93m◼◼◼            ◼◼◼\033[0m      \033[93m◼◼◼\033[0m
         \033[93m◼◼◼\033[0m   \033[93m◼◼◼              ◼◼◼\033[0m   \033[93m◼◼\033[0m            \033[93m◼◼◼\033[0m         \033[93m◼◼◼       ◼◼◼\033[0m  \033[93m◼◼◼              ◼◼◼\033[0m       \033[93m◼◼◼\033[0m
"""
__version__ = '2.0.0a0'
__version_name__ = 'Beryllium'