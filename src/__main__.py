import argparse
from pathlib import Path
import sys
import torch
from llm_sdk import Small_LLM_Model

LLM_SDK_DIR = Path(__file__).resolve().parent.parent / "llm_sdk"
sys.path.insert(0, str(LLM_SDK_DIR))


def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        type=Path,
        default=Path("data/input/function_calling_tests.json"),
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("data/output/function_calling_results.json"),
    )
    parser.add_argument(
        "--functions_definition",
        type=Path,
        default=Path("data/input/functions_definition.json"),
    )
    return parser.parse_args()


def main() -> int:
    """Run the application."""
    args = parse_arguments()
    model = Small_LLM_Model()
    prompt = "how are you"
    input_ids = model.encode(prompt)
    logits = model.get_logits_from_input_ids(input_ids[0].tolist())
    next_token_id = torch.tensor(logits).argmax().item()
    print(f"Most likely next token: {model.decode([next_token_id])!r}")
    return 0


main()