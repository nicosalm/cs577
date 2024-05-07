CFLAGS=-O2 -march=native
build: paging.c
	gcc $(CFLAGS) paging.c -o paging 

run: paging
	./paging

clean:
	rm -f paging *.o
