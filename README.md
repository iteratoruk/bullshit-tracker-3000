# Bullshit Tracker 3000

![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)

> “Because your time is precious—and evidently everyone else’s interruptions aren’t.”  

A minimalist desktop timer that logs every second wasted on pointless workplace nonsense. Hit one giant button to start/stop, and let Bullshit Tracker 3000 keep a running total for posterity (and passive-aggressive remarks).

## Installation

1. **Clone it** (you probably know how, but here’s the reminder you didn’t ask for):

   ```bash
   git clone https://github.com/iteratoruk/bullshit-tracker-3000.git
   cd bullshit-tracker-3000
   ```

2. **Install with Poetry** (because dependency hell is even more soul destroying than listening to inane drivel)

    ```bash
    poetry install
    ```

3. **Run it** (or don't ... I don't really care)

    ```bash
    poetry run bst3000
    ```

## Data

* All session logs are saved in JSON at
    
    ```bash
    ~/.bst3000/log.json
    ```
  
## Development

1. Add features when you think of more ways to quantify nonsense. 
2. Submit a PR. Your code had better be cleaner than the last time someone asked me to do a "review", and it had better not contain a load of irrelevant crap buried under a single change.

## Contributing

Feel free to:

* Suggest more passive-aggressive UI copy. 
* Add graphs, badges, or charts if you enjoy burying people in data. 
* Introduce dark mode to match the deep sense of foreboding in your soul when someone says "Quick question ..."

## License

This project is licensed under the GNU General Public License v3.0. See [LICENSE](LICENSE) for details.

    “Redistribute and modify all you like. Just don’t waste time complaining about the license.”
