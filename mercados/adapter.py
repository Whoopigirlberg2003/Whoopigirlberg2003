# app/services/adapters/mercados.py

class MercadosAdapter:
    def enrich_asset(self, row: dict):
        name = row.get("asset_description")

        # TODO: call mercados.b3 / cvm etc
        return {
            "ticker": None,
            "asset_type": "unknown",
            "source": "mercados"
        }
