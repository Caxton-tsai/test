class io:
    suppurt=["console","file"]
    def read(src):
        if src not in io.suppurt:
            print("not support "+a)
        else:
            print("read from ",src)

print(io.suppurt)
b="file"
io.read(b)
a="20ff"
io.read(a)