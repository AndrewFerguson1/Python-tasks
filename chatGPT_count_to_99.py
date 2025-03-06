file_path = "count_to_99.txt"

with open(file_path, "w") as f:
    num = 0.0
    while num <= 99:
        f.write(f"{num:.6f}\n")  # Write number with 6 decimal places
        num += 0.000001

print(f"Finished writing to {file_path}")
