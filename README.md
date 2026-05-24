# PDF Extractor

Automatically extracts AWB data from Apple packing list/invoice PDFs and logs to Excel.

## Requirements
- Mac with [Homebrew](https://brew.sh)
- Python 3

## Setup (one-time)
Paste this in Terminal:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Karlpogi11/PackingList-Text-Extractor/main/install.sh)"
```
This will install dependencies and download the tool to your Desktop.

## Usage
```bash
./run.sh
```
Then drop PDFs into the `inbox/` folder — they process automatically.

## Output
- `processed/Month YYYY/` — renamed to `SGxxxxxxx.pdf`
- `permits/` — PDFs containing a permit (not logged)
- `errors/` — PDFs with unreadable fields, renamed with missing field names
- `awb_log.xlsx` — extracted data log

## Columns logged
`HAWB` | `InvoiceReference` | `InvoiceTotalAmount` | `DeliveryDate` | `TotalQty` | `ReceivedDate` *(fill manually)* | `OriginalFilename` | `DateLogged`
