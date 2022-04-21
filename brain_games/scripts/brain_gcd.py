# !/usr/bin/env python
from brain_games.engine import start
from brain_games.games import brain_gcd


def main():
    start(brain_gcd)
