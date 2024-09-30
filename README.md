# Project Euler solutions

## Introduction

Welcome to my collection of solutions to Project Euler problems!

[Project Euler](https://projecteuler.net/) is a website where you can tackle a variety of mathematically-oriented problems by writing small computer programs.

Most problems I initially solved using Python. However, for some of them, I later rewrote the programs in C or Rust to achieve faster execution times, or simply for the enjoyment of the challenge.

After solving a problem, I often compared my solution with those of others. In addition to the problem forums on the Project Euler website, I found the following resources particularly helpful:
- The now defunct mathblog.dk of Kristian Edlund and Bjarki Ágúst Guðmundsson. The last good version of this site is at https://web.archive.org/web/20180115175817/http://www.mathblog.dk/project-euler-solutions
- https://blog.dreamshire.com/category/project-euler-solutions/

## Running the solutions

### C
Building and running a solution
```
make p007c
./p007c
```

Building and running the unit tests of a solution
```
make p026_testc
./p026_testc
```

### Python
Running a solution
```
python3 py.p058
```

Running the unit tests of a solution
```
pytest p058_test.py
```

### Rust
Building the release target of a solution and running it
```
cargo run --release --bin p096r
```

Running the unit tests of a solution
```
cargo test --bin p096r
```

Happy puzzle-solving!  
Stefaan Rillaert
