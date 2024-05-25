p%c: p%.c prime_sieve.h prime_sieve.c
	gcc -o $@ $< prime_sieve.c -lm

p%r: p%.rs prime_sieve.rs
	rustc -o $@ $<
