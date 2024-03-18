p%c: p%.c
	gcc -o $@ $< -lm

p%r: p%.rs
	rustc -o $@ $<