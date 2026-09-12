
import pygame as pg
import typing


events: dict[int, list[typing.Callable]] = {}


def add(hook: int, event: typing.Callable[[int], None]):
    global events

    event_list = events.get(hook)
    if event_list:
        events[hook].append(event)
    else:
        events[hook] = [event]

def remove(hook: int, event: typing.Callable):
    global events
    events[hook].remove(event)

def clear(hook: int):
    global events
    events[hook] = []

def update_events():
    global events

    for event in pg.event.get():
        if event.type in events:
            for called in events[event.type]:
                called(event)

