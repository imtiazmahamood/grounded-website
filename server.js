const express = require('express');
const app = express();
app.use(express.static(__dirname));
const PORT = process.env.PORT || 8080;
app.listen(PORT, '0.0.0.0', () => {
  console.log(`Server running on port ${PORT}`);
});
