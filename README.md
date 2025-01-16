# Memory Usage Report Generator

本工具用於解析 `.map` 檔案，以檢視和整理各個檔案在程式中的記憶體使用量，並輸出為 CSV 報表。

---

## 特色

  - **自動抓取** `.map` 檔中的記憶體資訊 (例如 `.text` 區段)。
  - 根據各檔案所佔用的記憶體 **加總並排名**。
  - 將結果輸出為 **CSV 報表**，方便後續分析或整合。

---

## 安裝與環境需求

  1. **Python 3**（推薦使用 Python 3.7 以上版本）
  2. **pandas**：用於生成與輸出 CSV 報表。

### 安裝 pandas

```bash
pip install pandas
```

---

### 使用方式
  1.**放置 .map 檔**

  將欲分析的 .map 檔放在指定的輸入資料夾（例如範例中的 ./input）。
  
  2.**執行程式**
  執行下列指令：
  ```bash
  python map_file_analyzer.py
  ```
  預設程式會將分析後的 CSV 報表輸出到 ./output 資料夾。
  
   3.**檢視結果**

   程式完成後，會在輸出資料夾中生成對應的 _memory_usage_report.csv 報表，可使用 Excel、CSV Viewer 或任何文字編輯器檢視。


---


### 主要函式說明
  - parse_map_file(map_file_path)
  
  功能：解析指定的 .map 檔，從中擷取記憶體使用資訊並彙整。
  輸入：.map 檔路徑。
  輸出：各個檔案與其對應的記憶體使用量（以 dictionary 或 list of tuples 形式）。
  - generate_memory_report(map_file_path, output_csv_path)
  
  功能：讀取 .map 檔，生成記憶體使用報表並輸出到 CSV。
  輸入：
  .map 檔路徑
  輸出的 CSV 檔路徑
  輸出：無（直接產出 CSV 檔）。
  - process_all_map_files(input_dir, output_dir)
  
  功能：批次處理資料夾中的所有 .map 檔，並將結果儲存至指定的輸出資料夾。
  輸入：
  輸入資料夾路徑
  輸出資料夾路徑
  輸出：無（直接產出多個 CSV 報表）

---

### 檔案結構範例
```shell
.
├── input
│   ├── demo1.map
│   └── demo2.map
├── output
│   ├── demo1_memory_usage_report.csv
│   └── demo2_memory_usage_report.csv
└── map_file_analyzer.py
```
