p%c: p%.c prime.h prime.c
	gcc -o $@ $< prime.c -lm

p%r: p%.rs prime_sieve.rs
	rustc -o $@ $<
