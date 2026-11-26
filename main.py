import os

LINE = "I am out of office until Monday, answering nothing, because the last time I checked email on holiday I fixed a bug from a beach and nobody thanked the sand."

def main():
    assert len(LINE) == 156, f"line is {len(LINE)} chars, expected 156"
    assert LINE.strip() == LINE and LINE.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} chars")

if __name__ == "__main__":
    main()
