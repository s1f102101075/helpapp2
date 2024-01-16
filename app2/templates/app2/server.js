const express = require('express');
const cors = require('cors');
const fetch = require('node-fetch');

const app = express();
const port = 3000;

app.use(express.json());
app.use(cors());

app.post('/api/chatgpt', async (req, res) => {
  const question = req.body.question;
  const apiKey = '7f5AQ030gyWL6Cbgu1GNO-fTRvLAyKgQ8Lcu10bMZnvz6UgH3fXxJgooGCP60ToYx6z3PQAc2HUo72fk2GOVMeg'; // 正しいAPIキーを設定してください

  try {
    // 正しいAPIエンドポイントに修正する必要がある。
    const apiEndpoint = 'https://api.openai.iniad.org/api/v1'; // 正しいエンドポイントに修正してください

    // const response = await fetch(apiEndpoint, {
    //   method: 'POST',
    //   headers: {
    //     'Content-Type': 'application/json',
    //     'Authorization': 'Bearer ' + apiKey
    //   },
    //   body: JSON.stringify({ question: question })
    // });
    const response = await fetch('http://127.0.0.1:8000/app2/FAQ/api/chatgpt', {
     method: 'POST',
    headers: {
    'Content-Type': 'application/json',
    'Authorization': apiKey
  },
  body: JSON.stringify({ question: question })
});


    if (!response.ok) {
      // 応答が成功でない場合はエラーを投げる
      throw new Error('API request failed with status ' + response.status);
    }

    const data = await response.json();
    res.json({ answer: data.answer });
  } catch (error) {
    console.error('Error:', error);
    res.status(500).json({ error: 'Internal Server Error', message: error.message });
  }
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});