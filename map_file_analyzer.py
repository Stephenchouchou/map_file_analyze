import os
import re
import pandas as pd

def parse_map_file(map_file_path):
    """
    Parse the given .map file to extract memory usage information.
    :param map_file_path: Path to the .map file.
    :return: A list of tuples containing file names and their memory usage.
    """
    usage_by_file = {}

    with open(map_file_path, 'r') as f:
        lines = f.readlines()

    for line in lines:
        # Match lines with memory usage data (e.g., `.text` sections)
        match = re.match(r'\s*(0x[0-9a-f]+)\s+(0x[0-9a-f]+)\s+(\S+)', line)
        if match:
            address, size, symbol = match.groups()
            size = int(size, 16)
            file_name = symbol.split('/')[-1] if '/' in symbol else symbol

            # Accumulate usage by file
            if file_name not in usage_by_file:
                usage_by_file[file_name] = 0
            usage_by_file[file_name] += size

    return usage_by_file

def generate_memory_report(map_file_path, output_csv_path):
    """
    Generate a memory usage report from a .map file and save it as a CSV.
    :param map_file_path: Path to the .map file.
    :param output_csv_path: Path to save the CSV report.
    """
    usage_by_file = parse_map_file(map_file_path)

    # Sort results by size in descending order
    sorted_files = sorted(usage_by_file.items(), key=lambda x: x[1], reverse=True)

    # Create a DataFrame for better visualization and export
    df = pd.DataFrame(sorted_files, columns=["File", "Size"])

    # Save to CSV
    df.to_csv(output_csv_path, index=False)

    print(f"Memory usage report saved to: {output_csv_path}")

def process_all_map_files(input_dir, output_dir):
    """
    Process all .map files in the input directory and generate reports in the output directory.
    :param input_dir: Path to the directory containing .map files.
    :param output_dir: Path to the directory to save CSV reports.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for file_name in os.listdir(input_dir):
        if file_name.endswith('.map'):
            map_file_path = os.path.join(input_dir, file_name)  # 修正路徑組合
            output_csv_path = os.path.join(output_dir, f"{os.path.splitext(file_name)[0]}_memory_usage_report.csv")
            generate_memory_report(map_file_path, output_csv_path)

if __name__ == "__main__":
    # Example usage
    input_dir = "./input"  # Path to the directory containing .map files
    output_dir = "./output"  # Path to save the output CSV files

    process_all_map_files(input_dir, output_dir)
