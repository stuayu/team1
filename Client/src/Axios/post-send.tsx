export {}
// POST送信
fetch('[]', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      name: 'Hubot',
      login: 'hubot',
    })
  }).then(function(response) {
    // レスポンス結果
  }, function(error) {
    // エラー内容
  });