# Specify the file size in bytes (64 MB)
file_size = 64 * 1024 * 1024  # 64 MB

# Specify the file name
file_name = "data_file"

# Create a file with the specified size
with open(file_name, "wb") as f:
    f.write(b'\0' * file_size)

# Verify the file size
with open(file_name, "rb") as f:
    result = f.read()
    assert len(result) == file_size

print(f"File '{file_name}' created successfully with size {file_size} bytes.")