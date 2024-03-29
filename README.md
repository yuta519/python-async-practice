# Python Async Guide

## What is this repository?

- For me, the concept of python asyncio is difficult.
- To understand it, organize the info.

## What is Asynchrounous Programing?

- Allows a program to perform multiple operations concurrently.
- While main tasks run, other tasks are initiated and then are set aside until results are needed
- For example, when you wait for the oven to bake a cake, you are free. So during baking you can cook whip.

## Synchronous vs Asynchronous

- Synchronous

  - The code will be run from up to down.
  - Let't consider the example: `sync_vs_async/sync.py`

    - In the code, there are 2 tasks, the one is `fetch_data` and the other is `print_numbers`
    - On synchronous programming after `fetch_data` is done, `print_numbers` starts and it totally takes 12 seconds to finish the code.
    - try the below command,

    > python sync_vs_async/sync.py

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

    ![Diagram of sync programming](assets/sync.png)

- Asynchronous

  - Asynchronous programming works differently.
  - Let't consider the example: `sync_vs_async/async.py`

    - Now, each functions have a keyword `async` before `def`.
    - In main function, `fetch_data` and `print_numbers` are created as tasks.
    - The tasks are defined but these are not yet executed at this point. When the first `await` appears, these tasks will be run.
    - try the below command,

    > python sync_vs_async/async.py

    ```
    tasks1 and 2 created, but not yet executed
    Start fetching
    0
    1
    Done fetching
    2
    3
    4
    5
    6
    7
    8
    9
    {'data': 1}
    ```

    - You can see this code run tasks concurrently like the below diagram.

    ![Diagram of async programming](assets/async.png)

## asyncio terms

- Single Threading
  - To excuete tasks concurrently, multi threading and multi processing are required.
  - However, asyncio is working single threading.
  - How? This is because `Event Loop` enables tasks work concurrently.
- Event Loop
  - a core of async, which waits for a message and event and dispaches them.
  - a concept to wait for events and dipatch them in a program.
  - responsible for managing the execution of asynchronous tasks.
  - [This article](https://www.pythontutorial.net/python-concurrency/python-event-loop/) helps you understand what event loop is.
    ![Event loop](https://www.pythontutorial.net/wp-content/uploads/2022/07/python-event-loop.svg)
- Coroutine
  - a core concept of asyncio, which is allowed to suspend and resume the execution
  - in general, python functions which works asynchornously
  - define with `async def`

## How to use coroutine for async programming

- To run a coroutine
  - Declare coroutine with `async def`, which does nothing at the point of declaration.
  - To pause and resume this execution, `await` keyword is required.

```python
import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)
  """_summary_
  """

async def main():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())
```

- In the above example:
  - 2 corountines are defined, `say_after` and `main`.
  - The `main` runs twice `say_after` with `await` keyword.
  - So when you run this code, you will see 'hello' after 1 sec and 'world' 2 secs after your execution.
  - In addition, `asyncio.run()` is used to run the coroutine `main`.
