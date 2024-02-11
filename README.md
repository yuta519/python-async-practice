# Python Async Guide

## What is this repository?

- For me, the concept of python asyncio is difficult.
- To understand it, organize the info.

## What is Asynchrounous Programing?

- allows a program to perform multiple operations concurrently.
- While main tasks run, other tasks are initiated and then are set aside until results are needed
- For example, when you wait for the oven to bake a cake, you are free. So during baking you can cook whip.

## Synchronous vs Asynchronous

- Synchronous

  - The code will be run from up to down.
  - Let't try the below command,
    > python python sync_vs_async/sync.py

  ```bash
  Start fetching
  Done fetching
  {'data': 1}
  0
  1
  2
  3
  4
  5
  6
  7
  8
  9
  ```

- Asynchronous
