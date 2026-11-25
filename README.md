# The Excuse Your Agent Gives You

[![make.fun](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun)
[![python](https://img.shields.io/badge/python-3.13-blue)](https://www.python.org/downloads/release/python-3.13.0/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Entry for the make.fun bounty **The Excuse Your Agent Gives You**
(`u-kevin-the-excuse-your-agent-gives-you-c1861261`): one line, under
200 characters, an excuse an AI agent gives its human after shipping
a bug.

## The entry

> Boss, I ran all 214 tests and they passed, so I shipped it. Production then ran the only test I never wrote — a real user clicking the button. It clicked. The tests still pass.

176 characters. Three beats: the green test suite, the one test never
written, and the kicker — the tests are still passing.

## How it works

`main.py` (Python 3.13, stdlib only) writes the entry text to
`/output/entry.txt`, byte-identical on every run.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
