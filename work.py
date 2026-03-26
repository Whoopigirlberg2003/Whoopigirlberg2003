def process_document(local_path, user_id):
    raw = textract_adapter.extract(local_path)

    rows = normalize_textract(raw)

    final = []

    for row in rows:
        asset = mercados_adapter.enrich_asset(row)

        if not asset:
            asset = brfinance_adapter.enrich_asset(row)

        row.update(asset)

        decision = decide_create_or_update(row)

        final.append({
            "row": row,
            "decision": decision
        })

    return final
