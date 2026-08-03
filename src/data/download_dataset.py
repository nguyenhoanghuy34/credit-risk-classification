from pathlib import Path

from datasets import load_dataset


def download_credit_dataset(output_dir: str | Path) -> None:
    """
    Download the credit scoring dataset from Hugging Face
    and save it as CSV files.
    """

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    dataset = load_dataset(
        "spectrallabs/credit-scoring-training-dataset"
    )

    for split_name, split in dataset.items():
        df = split.to_pandas()

        output_file = output_dir / f"{split_name}.csv"
        df.to_csv(output_file, index=False)

        print(f"Saved: {output_file}")


if __name__ == "__main__":
    project_root = Path(__file__).resolve().parents[2]

    raw_dir = project_root / "datasets" / "raw"

    download_credit_dataset(raw_dir)