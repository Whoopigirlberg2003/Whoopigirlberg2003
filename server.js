const express = require("express");
const app = express();

app.use(express.json());

app.post("/enrich/asset", async (req, res) => {
  const { asset_description } = req.body;

  // TODO: call brFinance lib here (lib/index.ts compiled)
  // For now stub:

  res.json({
    asset_description,
    ticker: null,
    source: "brfinance"
  });
});

app.listen(3001, () => {
  console.log("brFinance API running on 3001");
});
