import io
from typing import Iterable

import pandas as pd


def export_records_to_excel(records: Iterable[dict]) -> bytes:
    """Return Excel file bytes for Streamlit download."""
    df = pd.DataFrame(list(records))
    buf = io.BytesIO()
    with pd.ExcelWriter(buf, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="records")
    return buf.getvalue()

